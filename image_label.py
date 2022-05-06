import math

from PyQt6 import QtWidgets, QtGui, QtCore


class ImageLabel(QtWidgets.QLabel):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.parentCls = parent
        self.prevLocX = 0
        self.prevLocY = 0
        self.curLocX = 0
        self.curLocY = 0
        self.isClickOnImg = False
        self.isCreateRectBtnClicked = False

    def mousePressEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mousePressEvent(ev)

        if self.isCreateRectBtnClicked:
            self.prevLocX = ev.position().x()
            self.prevLocY = ev.position().y()
            self.isClickOnImg = True
            self.setMouseTracking(False)
            self.update()

    def mouseReleaseEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mouseReleaseEvent(ev)

        if self.isCreateRectBtnClicked:
            dist = math.sqrt(
                math.pow(self.curLocX - self.prevLocX, 2)
                + math.pow(self.curLocY - self.prevLocY, 2)
            )

            if dist > 50:
                label, ret = QtWidgets.QInputDialog.getText(
                    self, "Label Box", "Please enter the label"
                )

                if label and ret:
                    paintRectX1 = int(
                        self.prevLocX
                        * self.pixmap().size().width()
                        / self.size().width()
                    )
                    paintRectY1 = int(
                        self.prevLocY
                        * self.pixmap().size().height()
                        / self.size().height()
                    )
                    paintRectX2 = int(
                        self.curLocX
                        * self.pixmap().size().width()
                        / self.size().width()
                    )
                    paintRectY2 = int(
                        self.curLocY
                        * self.pixmap().size().height()
                        / self.size().height()
                    )

                    self.parentCls.to_staging_area(
                        label=label,
                        pt1=(paintRectX1, paintRectY1),
                        pt2=(paintRectX2, paintRectY2),
                    )

            self.isClickOnImg = False
            self.setMouseTracking(True)
            self.update()

    def mouseMoveEvent(self, ev: QtGui.QMouseEvent) -> None:
        super().mouseMoveEvent(ev)

        if self.isCreateRectBtnClicked:
            self.curLocX = int(ev.position().x())
            self.curLocY = int(ev.position().y())
            self.update()

    def paintEvent(self, a0: QtGui.QPaintEvent) -> None:
        super().paintEvent(a0)

        if self.isCreateRectBtnClicked:

            if not self.isClickOnImg:
                painter = QtGui.QPainter(self)

                painter.setPen(
                    QtGui.QPen(
                        QtCore.Qt.GlobalColor.red, 2, QtCore.Qt.PenStyle.DashLine
                    )
                )

                lineX = QtCore.QLine(
                    self.curLocX, 0, self.curLocX, self.size().height()
                )
                painter.drawLine(lineX)

                lineY = QtCore.QLine(
                    0, self.curLocY, self.size().width(), self.curLocY,
                )
                painter.drawLine(lineY)

            else:
                painter = QtGui.QPainter(self)

                painter.setPen(
                    QtGui.QPen(
                        QtCore.Qt.GlobalColor.black, 5, QtCore.Qt.PenStyle.SolidLine
                    )
                )
                painter.setBrush(
                    QtGui.QBrush(
                        QtCore.Qt.GlobalColor.green,
                        QtCore.Qt.BrushStyle.DiagCrossPattern,
                    )
                )
                rect = QtCore.QRect(
                    self.prevLocX,
                    self.prevLocY,
                    self.curLocX - self.prevLocX,
                    self.curLocY - self.prevLocY,
                )
                painter.drawRect(rect)

                painter.setPen(
                    QtGui.QPen(
                        QtCore.Qt.GlobalColor.blue, 3, QtCore.Qt.PenStyle.SolidLine
                    )
                )
                line = QtCore.QLine(
                    int(self.prevLocX),
                    int(self.prevLocY),
                    int(self.curLocX),
                    int(self.curLocY),
                )
                painter.drawLine(line)

            self.update()
