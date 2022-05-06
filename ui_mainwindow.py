import src.src_rc

from image_label import ImageLabel
from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 762)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/icons/src/icons/main-window.png"),
            QtGui.QIcon.Mode.Normal,
            QtGui.QIcon.State.Off,
        )
        MainWindow.setWindowIcon(icon)
        self.gridLayout_2 = QtWidgets.QGridLayout(MainWindow)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_and_files_layout = QtWidgets.QVBoxLayout()
        self.lbl_and_files_layout.setContentsMargins(30, 0, 10, 0)
        self.lbl_and_files_layout.setSpacing(0)
        self.lbl_and_files_layout.setObjectName("lbl_and_files_layout")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.lbl_list_widg = QtWidgets.QListWidget(MainWindow)
        self.lbl_list_widg.setMinimumSize(QtCore.QSize(250, 1))
        self.lbl_list_widg.setMaximumSize(QtCore.QSize(450, 16777215))
        self.lbl_list_widg.setObjectName("lbl_list_widg")
        self.verticalLayout_9.addWidget(self.lbl_list_widg)
        self.lbl_and_files_layout.addLayout(self.verticalLayout_9)
        spacerItem = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.lbl_and_files_layout.addItem(spacerItem)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.TextFormat.RichText)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.file_list_widg = QtWidgets.QListWidget(MainWindow)
        self.file_list_widg.setMinimumSize(QtCore.QSize(250, 1))
        self.file_list_widg.setMaximumSize(QtCore.QSize(450, 16777215))
        self.file_list_widg.setObjectName("file_list_widg")
        self.verticalLayout_8.addWidget(self.file_list_widg)
        self.lbl_and_files_layout.addLayout(self.verticalLayout_8)
        self.gridLayout.addLayout(self.lbl_and_files_layout, 0, 1, 1, 1)
        self.img_lbl = ImageLabel(MainWindow)
        self.img_lbl.setMinimumSize(QtCore.QSize(1, 1))
        self.img_lbl.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        self.img_lbl.setMouseTracking(True)
        self.img_lbl.setPixmap(QtGui.QPixmap(":/images/src/images/empty.png"))
        self.img_lbl.setScaledContents(True)
        self.img_lbl.setObjectName("img_lbl")
        self.gridLayout.addWidget(self.img_lbl, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 2, 1, 1)
        self.btn_layout = QtWidgets.QVBoxLayout()
        self.btn_layout.setContentsMargins(10, 20, 30, 20)
        self.btn_layout.setSpacing(0)
        self.btn_layout.setObjectName("btn_layout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.open_img_btn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_img_btn.sizePolicy().hasHeightForWidth())
        self.open_img_btn.setSizePolicy(sizePolicy)
        self.open_img_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.open_img_btn.setAutoFillBackground(False)
        self.open_img_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/image.png);"
        )
        self.open_img_btn.setText("")
        self.open_img_btn.setObjectName("open_img_btn")
        self.horizontalLayout_2.addWidget(self.open_img_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.btn_layout.addLayout(self.verticalLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.btn_layout.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.open_folder_btn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.open_folder_btn.sizePolicy().hasHeightForWidth()
        )
        self.open_folder_btn.setSizePolicy(sizePolicy)
        self.open_folder_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.open_folder_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/folder.png);"
        )
        self.open_folder_btn.setText("")
        self.open_folder_btn.setObjectName("open_folder_btn")
        self.horizontalLayout_3.addWidget(self.open_folder_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.open_folder_lbl = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.open_folder_lbl.setFont(font)
        self.open_folder_lbl.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.open_folder_lbl.setObjectName("open_folder_lbl")
        self.verticalLayout_3.addWidget(self.open_folder_lbl)
        self.btn_layout.addLayout(self.verticalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.btn_layout.addItem(spacerItem2)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.create_rect_btn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.create_rect_btn.sizePolicy().hasHeightForWidth()
        )
        self.create_rect_btn.setSizePolicy(sizePolicy)
        self.create_rect_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.create_rect_btn.setStyleSheet(
            "border-image: url(:/icons/src/icons/edit.png);"
        )
        self.create_rect_btn.setText("")
        self.create_rect_btn.setObjectName("create_rect_btn")
        self.horizontalLayout_4.addWidget(self.create_rect_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.create_rect_lbl = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.create_rect_lbl.setFont(font)
        self.create_rect_lbl.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.create_rect_lbl.setObjectName("create_rect_lbl")
        self.verticalLayout_4.addWidget(self.create_rect_lbl)
        self.btn_layout.addLayout(self.verticalLayout_4)
        spacerItem3 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.btn_layout.addItem(spacerItem3)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.go_prev_btn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_prev_btn.sizePolicy().hasHeightForWidth())
        self.go_prev_btn.setSizePolicy(sizePolicy)
        self.go_prev_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.go_prev_btn.setStyleSheet("border-image: url(:/icons/src/icons/prev.png);")
        self.go_prev_btn.setText("")
        self.go_prev_btn.setObjectName("go_prev_btn")
        self.horizontalLayout_5.addWidget(self.go_prev_btn)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.go_prev_lbl = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.go_prev_lbl.setFont(font)
        self.go_prev_lbl.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.go_prev_lbl.setObjectName("go_prev_lbl")
        self.verticalLayout_5.addWidget(self.go_prev_lbl)
        self.btn_layout.addLayout(self.verticalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.btn_layout.addItem(spacerItem4)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.go_next_btn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.go_next_btn.sizePolicy().hasHeightForWidth())
        self.go_next_btn.setSizePolicy(sizePolicy)
        self.go_next_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.go_next_btn.setStyleSheet("border-image: url(:/icons/src/icons/next.png);")
        self.go_next_btn.setText("")
        self.go_next_btn.setObjectName("go_next_btn")
        self.horizontalLayout_6.addWidget(self.go_next_btn)
        self.verticalLayout_6.addLayout(self.horizontalLayout_6)
        self.go_next_lbl = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.go_next_lbl.setFont(font)
        self.go_next_lbl.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.go_next_lbl.setObjectName("go_next_lbl")
        self.verticalLayout_6.addWidget(self.go_next_lbl)
        self.btn_layout.addLayout(self.verticalLayout_6)
        spacerItem5 = QtWidgets.QSpacerItem(
            20,
            30,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        self.btn_layout.addItem(spacerItem5)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.save_btn = QtWidgets.QPushButton(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy)
        self.save_btn.setMinimumSize(QtCore.QSize(64, 64))
        self.save_btn.setStyleSheet("border-image: url(:/icons/src/icons/save.png);")
        self.save_btn.setText("")
        self.save_btn.setObjectName("save_btn")
        self.horizontalLayout_7.addWidget(self.save_btn)
        self.verticalLayout_7.addLayout(self.horizontalLayout_7)
        self.save_lbl = QtWidgets.QLabel(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.save_lbl.setFont(font)
        self.save_lbl.setAlignment(
            QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop
        )
        self.save_lbl.setObjectName("save_lbl")
        self.verticalLayout_7.addWidget(self.save_lbl)
        self.btn_layout.addLayout(self.verticalLayout_7)
        self.gridLayout_2.addLayout(self.btn_layout, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ocr Annotation Tool"))
        self.label.setText(_translate("MainWindow", "Annotations"))
        self.label_2.setText(_translate("MainWindow", "Folder Content"))
        self.label_3.setText(_translate("MainWindow", "Open Image"))
        self.open_folder_lbl.setText(_translate("MainWindow", "Open Folder"))
        self.create_rect_lbl.setText(_translate("MainWindow", "Create Rect"))
        self.go_prev_lbl.setText(_translate("MainWindow", "Go Prev"))
        self.go_next_lbl.setText(_translate("MainWindow", "Go Next"))
        self.save_lbl.setText(_translate("MainWindow", "Save "))
