import glob

from database_con import DataBase
from ui_mainwindow import Ui_MainWindow
from PyQt6 import QtWidgets, QtTest, QtGui, QtCore


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        DataBase.first_con()

        self.imgTypes = ("*.jpeg", "*.jpg", "*.png")
        self.imagesPath = []
        self.stagingMem = []

        self.isAnyImageOpened = False
        self.isAnyFolderOpened = False

        self.ui.open_img_btn.clicked.connect(self.open_img_btn_click)
        self.ui.open_folder_btn.clicked.connect(self.open_folder_btn_click)
        self.ui.go_prev_btn.clicked.connect(self.go_prev_btn_click)
        self.ui.go_next_btn.clicked.connect(self.go_next_btn_click)
        self.ui.create_rect_btn.clicked.connect(self.create_rect_btn_click)
        self.ui.save_btn.clicked.connect(self.save_btn_click)
        self.ui.file_list_widg.itemDoubleClicked.connect(
            self.file_list_widg_item_db_clk
        )
        self.ui.lbl_list_widg.installEventFilter(self)

    def prepare(self, t):
        if t == "folder":
            self.isAnyFolderOpened = True
            self.imagesPath.sort()
        elif t == "file":
            self.isAnyFolderOpened = False

        self.isAnyImageOpened = True
        self.imgNavIndex = 0
        self.ui.file_list_widg.clear()
        self.ui.file_list_widg.addItems(self.imagesPath)
        self.ui.file_list_widg.setCurrentRow(self.imgNavIndex)
        self.ui.img_lbl.setPixmap(QtGui.QPixmap(self.imagesPath[self.imgNavIndex]))

    def update_annotations(self, d=False):
        self.labelID = 0
        self.ui.lbl_list_widg.clear()

        if len(self.stagingMem) > 0:
            isFound = False

            for annot in self.stagingMem:
                if not isFound:
                    pixmapImg = QtGui.QPixmap(self.imagesPath[self.imgNavIndex])
                    painter = QtGui.QPainter()
                    painter.begin(pixmapImg)
                    isFound = True

                labelItem = "ID: {} - {}".format(annot[0], annot[1])
                self.ui.lbl_list_widg.addItem(labelItem)

                pt1 = annot[2]
                pt2 = annot[3]

                rect = QtCore.QRect(pt1[0], pt1[1], pt2[0] - pt1[0], pt2[1] - pt1[1])
                painter.setPen(
                    QtGui.QPen(
                        QtCore.Qt.GlobalColor.green, 2, QtCore.Qt.PenStyle.SolidLine
                    )
                )
                painter.setBrush(QtGui.QBrush(QtCore.Qt.BrushStyle.NoBrush))
                painter.drawRect(rect)

                rectCorners = (
                    (pt1[0], pt1[1]),
                    (pt1[0], pt2[1]),
                    (pt2[0], pt2[1]),
                    (pt2[0], pt1[1]),
                )
                painter.setPen(
                    QtGui.QPen(
                        QtCore.Qt.GlobalColor.red, 2, QtCore.Qt.PenStyle.SolidLine
                    )
                )
                painter.setBrush(QtGui.QBrush(QtCore.Qt.GlobalColor.red))

                for corner in rectCorners:
                    painter.drawEllipse(corner[0], corner[1], 5, 5)

            if isFound:
                self.labelID = self.stagingMem[-1][0] + 1
                self.ui.img_lbl.setPixmap(pixmapImg)
                painter.end()

        elif d:
            self.ui.img_lbl.setPixmap(QtGui.QPixmap(self.imagesPath[self.imgNavIndex]))

    def to_staging_area(self, label, pt1, pt2):
        self.stagingMem.append([self.labelID, label, pt1, pt2])
        self.update_annotations()

    def eventFilter(self, source, event):
        if (
            str(event.type()) == "82" and source is self.ui.lbl_list_widg
        ):  # event.type() == ContextMenu

            rightClickMenu = QtWidgets.QMenu()
            editAction = rightClickMenu.addAction("Edit")
            delAction = rightClickMenu.addAction("Delete")
            action = rightClickMenu.exec(event.globalPos())

            if action == editAction:
                curRow = self.ui.lbl_list_widg.currentRow()
                selectedItem = self.ui.lbl_list_widg.takeItem(curRow)
                selectedLabelID = int(selectedItem.text().split()[1])

                newLabel, ret = QtWidgets.QInputDialog.getText(
                    self, "Edit Annotation", "Please enter the new annotation"
                )

                if ret:
                    for index, annot in enumerate(self.stagingMem):
                        if annot[0] == selectedLabelID:
                            self.stagingMem[index][1] = newLabel
                            self.update_annotations()
                            return True

            elif action == delAction:
                curRow = self.ui.lbl_list_widg.currentRow()
                selectedItem = self.ui.lbl_list_widg.takeItem(curRow)
                selectedLabelID = int(selectedItem.text().split()[1])

                for index, annot in enumerate(self.stagingMem):
                    if annot[0] == selectedLabelID:
                        del self.stagingMem[index]
                        self.update_annotations(d=True)
                        return True

            else:
                return False

        return super().eventFilter(source, event)

    def file_list_widg_item_db_clk(self):
        if self.isAnyFolderOpened:
            self.imgNavIndex = self.ui.file_list_widg.currentRow()
            self.ui.img_lbl.setPixmap(QtGui.QPixmap(self.imagesPath[self.imgNavIndex]))
            self.stagingMem = DataBase.pull_data(self.imagesPath[self.imgNavIndex])
            self.update_annotations()

    def open_img_btn_click(self):
        self.ui.open_img_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/image.png); background-color: rgb(129, 129, 129);"
        )
        QtTest.QTest.qWait(15)
        self.ui.open_img_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/image.png);"
        )

        fname = QtWidgets.QFileDialog.getOpenFileName(
            self, "Select Image", "", "Image files (*.jpeg *.jpg *.png)"
        )

        if fname[0]:
            self.imagesPath = [fname[0]]
            self.prepare(t="file")
            self.stagingMem = DataBase.pull_data(self.imagesPath[self.imgNavIndex])
            self.update_annotations()

    def open_folder_btn_click(self):
        self.ui.open_folder_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/folder.png); background-color: rgb(129, 129, 129);"
        )
        QtTest.QTest.qWait(15)
        self.ui.open_folder_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/folder.png);"
        )

        dirName = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Folder")

        if dirName:
            paths = []
            for imgType in self.imgTypes:
                paths.extend(glob.glob(dirName + "/" + imgType))

            if len(paths) > 0:
                self.imagesPath = paths.copy()
                self.prepare(t="folder")
                self.stagingMem = DataBase.pull_data(self.imagesPath[self.imgNavIndex])
                self.update_annotations()

    def go_prev_btn_click(self):
        self.ui.go_prev_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/prev.png); background-color: rgb(129, 129, 129);"
        )
        QtTest.QTest.qWait(20)
        self.ui.go_prev_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/prev.png);"
        )

        if self.isAnyFolderOpened:
            if len(self.imagesPath) > 1:
                self.imgNavIndex -= 1
                if self.imgNavIndex < 0:
                    self.imgNavIndex = len(self.imagesPath) - 1

                self.ui.file_list_widg.setCurrentRow(self.imgNavIndex)
                self.ui.img_lbl.setPixmap(
                    QtGui.QPixmap(self.imagesPath[self.imgNavIndex])
                )
                self.stagingMem = DataBase.pull_data(self.imagesPath[self.imgNavIndex])
                self.update_annotations()

            else:
                QtWidgets.QMessageBox.about(
                    self,
                    "Notice",
                    "There is 1 image in the folder. This button will work non-functional.",
                )

        else:
            QtWidgets.QMessageBox.about(
                self,
                "Notice",
                "If you want to browse through the pictures, you have to open any folder.",
            )

    def go_next_btn_click(self):
        self.ui.go_next_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/next.png); background-color: rgb(129, 129, 129);"
        )
        QtTest.QTest.qWait(20)
        self.ui.go_next_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/next.png);"
        )

        if self.isAnyFolderOpened:
            if len(self.imagesPath) > 1:
                self.imgNavIndex += 1

                if self.imgNavIndex == len(self.imagesPath):
                    self.imgNavIndex = 0

                self.ui.file_list_widg.setCurrentRow(self.imgNavIndex)
                self.ui.img_lbl.setPixmap(
                    QtGui.QPixmap(self.imagesPath[self.imgNavIndex])
                )
                self.stagingMem = DataBase.pull_data(self.imagesPath[self.imgNavIndex])
                self.update_annotations()

            else:
                QtWidgets.QMessageBox.about(
                    self,
                    "Notice",
                    "There is 1 image in the folder. This button will work non-functional.",
                )

        else:
            QtWidgets.QMessageBox.about(
                self,
                "Notice",
                "If you want to browse through the pictures, you have to open any folder.",
            )

    def create_rect_btn_click(self):
        self.ui.create_rect_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/edit.png); background-color: rgb(129, 129, 129);"
        )
        QtTest.QTest.qWait(15)
        self.ui.create_rect_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/edit.png);"
        )

        if self.isAnyImageOpened and not self.ui.img_lbl.isCreateRectBtnClicked:
            self.ui.create_rect_lbl.setText("Cancel Rect")
            self.ui.img_lbl.isCreateRectBtnClicked = True

        elif self.isAnyImageOpened and self.ui.img_lbl.isCreateRectBtnClicked:
            self.ui.img_lbl.isCreateRectBtnClicked = False
            self.ui.create_rect_lbl.setText("Create Rect")

        else:
            QtWidgets.QMessageBox.about(
                self,
                "Notice",
                "If you want to start annotating, you have to open any image.",
            )

    def save_btn_click(self):
        self.ui.save_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/save.png); background-color: rgb(129, 129, 129);"
        )
        QtTest.QTest.qWait(20)
        self.ui.save_btn.setStyleSheet("border-image: url(:/icons/src/icons/save.png);")

        if self.isAnyImageOpened:
            DataBase.sync_db(self.imagesPath[self.imgNavIndex], self.stagingMem)
            QtWidgets.QMessageBox.about(
                self,
                "Notice",
                "Annotations saved.",
            )

        else:
            QtWidgets.QMessageBox.about(
                self,
                "Notice",
                "In order to save data, annotation must be made on any image.",
            )


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
