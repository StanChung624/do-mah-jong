# Form implementation generated from reading ui file 'dmj-draft.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class BaseStructure(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1116, 510)
        Dialog.setMinimumSize(QtCore.QSize(1080, 386))
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 60, 861, 294))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.message = QtWidgets.QLabel(parent=self.widget)
        self.message.setMinimumSize(QtCore.QSize(280, 240))
        self.message.setMaximumSize(QtCore.QSize(16777214, 16777215))
        self.message.setAutoFillBackground(False)
        self.message.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.message.setObjectName("message")
        self.horizontalLayout_4.addWidget(self.message)
        self.sea = QtWidgets.QLabel(parent=self.widget)
        self.sea.setMinimumSize(QtCore.QSize(540, 240))
        self.sea.setMaximumSize(QtCore.QSize(660, 240))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 247, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 120, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 160, 133))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 225))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 247, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 247, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 120, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 160, 133))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(220, 255, 225))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 247, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 120, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(233, 247, 227))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 120, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(141, 160, 133))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 120, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 120, 100))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(212, 240, 199))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(106, 120, 100, 127))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.PlaceholderText, brush)
        self.sea.setPalette(palette)
        self.sea.setAutoFillBackground(True)
        self.sea.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignTop)
        self.sea.setObjectName("sea")
        self.horizontalLayout_4.addWidget(self.sea)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.flw_0 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_0.setEnabled(False)
        self.flw_0.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_0.setObjectName("flw_0")
        self.horizontalLayout_2.addWidget(self.flw_0)
        self.flw_1 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_1.setEnabled(False)
        self.flw_1.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_1.setObjectName("flw_1")
        self.horizontalLayout_2.addWidget(self.flw_1)
        self.flw_2 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_2.setEnabled(False)
        self.flw_2.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_2.setObjectName("flw_2")
        self.horizontalLayout_2.addWidget(self.flw_2)
        self.flw_3 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_3.setEnabled(False)
        self.flw_3.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_3.setObjectName("flw_3")
        self.horizontalLayout_2.addWidget(self.flw_3)
        self.flw_4 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_4.setEnabled(False)
        self.flw_4.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_4.setObjectName("flw_4")
        self.horizontalLayout_2.addWidget(self.flw_4)
        self.flw_5 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_5.setEnabled(False)
        self.flw_5.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_5.setObjectName("flw_5")
        self.horizontalLayout_2.addWidget(self.flw_5)
        self.flw_6 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_6.setEnabled(False)
        self.flw_6.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_6.setObjectName("flw_6")
        self.horizontalLayout_2.addWidget(self.flw_6)
        self.flw_7 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_7.setEnabled(False)
        self.flw_7.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_7.setObjectName("flw_7")
        self.horizontalLayout_2.addWidget(self.flw_7)
        self.flw_8 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_8.setEnabled(False)
        self.flw_8.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_8.setObjectName("flw_8")
        self.horizontalLayout_2.addWidget(self.flw_8)
        self.flw_9 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_9.setEnabled(False)
        self.flw_9.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_9.setObjectName("flw_9")
        self.horizontalLayout_2.addWidget(self.flw_9)
        self.flw_10 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_10.setEnabled(False)
        self.flw_10.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_10.setObjectName("flw_10")
        self.horizontalLayout_2.addWidget(self.flw_10)
        self.flw_11 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_11.setEnabled(False)
        self.flw_11.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_11.setObjectName("flw_11")
        self.horizontalLayout_2.addWidget(self.flw_11)
        self.flw_12 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_12.setEnabled(False)
        self.flw_12.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_12.setObjectName("flw_12")
        self.horizontalLayout_2.addWidget(self.flw_12)
        self.flw_13 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_13.setEnabled(False)
        self.flw_13.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_13.setObjectName("flw_13")
        self.horizontalLayout_2.addWidget(self.flw_13)
        self.flw_14 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_14.setEnabled(False)
        self.flw_14.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_14.setObjectName("flw_14")
        self.horizontalLayout_2.addWidget(self.flw_14)
        self.flw_15 = QtWidgets.QPushButton(parent=self.widget)
        self.flw_15.setEnabled(False)
        self.flw_15.setMinimumSize(QtCore.QSize(40, 40))
        self.flw_15.setObjectName("flw_15")
        self.horizontalLayout_2.addWidget(self.flw_15)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(parent=Dialog)
        self.widget1.setGeometry(QtCore.QRect(62, 364, 1001, 84))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tile_0 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_0.setEnabled(True)
        self.tile_0.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_0.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_0.setBaseSize(QtCore.QSize(0, 0))
        self.tile_0.setObjectName("tile_0")
        self.horizontalLayout.addWidget(self.tile_0)
        self.tile_1 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_1.setEnabled(True)
        self.tile_1.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_1.setMaximumSize(QtCore.QSize(20, 40))
        self.tile_1.setBaseSize(QtCore.QSize(0, 0))
        self.tile_1.setObjectName("tile_1")
        self.horizontalLayout.addWidget(self.tile_1)
        self.tile_2 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_2.setEnabled(True)
        self.tile_2.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_2.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_2.setBaseSize(QtCore.QSize(0, 0))
        self.tile_2.setObjectName("tile_2")
        self.horizontalLayout.addWidget(self.tile_2)
        self.tile_3 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_3.setEnabled(True)
        self.tile_3.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_3.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_3.setBaseSize(QtCore.QSize(0, 0))
        self.tile_3.setObjectName("tile_3")
        self.horizontalLayout.addWidget(self.tile_3)
        self.tile_4 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_4.setEnabled(True)
        self.tile_4.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_4.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_4.setBaseSize(QtCore.QSize(0, 0))
        self.tile_4.setObjectName("tile_4")
        self.horizontalLayout.addWidget(self.tile_4)
        self.tile_5 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_5.setEnabled(True)
        self.tile_5.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_5.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_5.setBaseSize(QtCore.QSize(0, 0))
        self.tile_5.setObjectName("tile_5")
        self.horizontalLayout.addWidget(self.tile_5)
        self.tile_6 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_6.setEnabled(True)
        self.tile_6.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_6.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_6.setBaseSize(QtCore.QSize(0, 0))
        self.tile_6.setObjectName("tile_6")
        self.horizontalLayout.addWidget(self.tile_6)
        self.tile_7 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_7.setEnabled(True)
        self.tile_7.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_7.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_7.setBaseSize(QtCore.QSize(0, 0))
        self.tile_7.setObjectName("tile_7")
        self.horizontalLayout.addWidget(self.tile_7)
        self.tile_8 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_8.setEnabled(True)
        self.tile_8.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_8.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_8.setBaseSize(QtCore.QSize(0, 0))
        self.tile_8.setObjectName("tile_8")
        self.horizontalLayout.addWidget(self.tile_8)
        self.tile_9 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_9.setEnabled(True)
        self.tile_9.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_9.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_9.setBaseSize(QtCore.QSize(0, 0))
        self.tile_9.setObjectName("tile_9")
        self.horizontalLayout.addWidget(self.tile_9)
        self.tile_10 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_10.setEnabled(True)
        self.tile_10.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_10.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_10.setBaseSize(QtCore.QSize(0, 0))
        self.tile_10.setObjectName("tile_10")
        self.horizontalLayout.addWidget(self.tile_10)
        self.tile_11 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_11.setEnabled(True)
        self.tile_11.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_11.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_11.setBaseSize(QtCore.QSize(0, 0))
        self.tile_11.setObjectName("tile_11")
        self.horizontalLayout.addWidget(self.tile_11)
        self.tile_12 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_12.setEnabled(True)
        self.tile_12.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_12.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_12.setBaseSize(QtCore.QSize(0, 0))
        self.tile_12.setObjectName("tile_12")
        self.horizontalLayout.addWidget(self.tile_12)
        self.tile_13 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_13.setEnabled(True)
        self.tile_13.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_13.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_13.setBaseSize(QtCore.QSize(0, 0))
        self.tile_13.setObjectName("tile_13")
        self.horizontalLayout.addWidget(self.tile_13)
        self.tile_14 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_14.setEnabled(True)
        self.tile_14.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_14.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_14.setBaseSize(QtCore.QSize(0, 0))
        self.tile_14.setObjectName("tile_14")
        self.horizontalLayout.addWidget(self.tile_14)
        self.tile_15 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_15.setEnabled(True)
        self.tile_15.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_15.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_15.setBaseSize(QtCore.QSize(0, 0))
        self.tile_15.setObjectName("tile_15")
        self.horizontalLayout.addWidget(self.tile_15)
        self.tile_16 = QtWidgets.QPushButton(parent=self.widget1)
        self.tile_16.setEnabled(True)
        self.tile_16.setMinimumSize(QtCore.QSize(40, 40))
        self.tile_16.setMaximumSize(QtCore.QSize(40, 40))
        self.tile_16.setBaseSize(QtCore.QSize(0, 0))
        self.tile_16.setObjectName("tile_16")
        self.horizontalLayout.addWidget(self.tile_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.button_eat = QtWidgets.QPushButton(parent=self.widget1)
        self.button_eat.setObjectName("button_eat")
        self.horizontalLayout_3.addWidget(self.button_eat)
        self.button_pon = QtWidgets.QPushButton(parent=self.widget1)
        self.button_pon.setObjectName("button_pon")
        self.horizontalLayout_3.addWidget(self.button_pon)
        self.button_gan = QtWidgets.QPushButton(parent=self.widget1)
        self.button_gan.setObjectName("button_gan")
        self.horizontalLayout_3.addWidget(self.button_gan)
        self.button_win = QtWidgets.QPushButton(parent=self.widget1)
        self.button_win.setObjectName("button_win")
        self.horizontalLayout_3.addWidget(self.button_win)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.copilot_msg = QtWidgets.QLabel(parent=Dialog)
        self.copilot_msg.setGeometry(QtCore.QRect(930, 79, 130, 201))
        self.copilot_msg.setMinimumSize(QtCore.QSize(130, 50))
        self.copilot_msg.setObjectName("copilot_msg")
        self.text_env = QtWidgets.QLabel(parent=Dialog)
        self.text_env.setGeometry(QtCore.QRect(930, 300, 130, 45))
        self.text_env.setMinimumSize(QtCore.QSize(130, 45))
        self.text_env.setObjectName("text_env")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.message.setText(_translate("Dialog", "TextLabel"))
        self.sea.setText(_translate("Dialog", "sea"))
        self.flw_0.setText(_translate("Dialog", "flw_0"))
        self.flw_1.setText(_translate("Dialog", "flw_1"))
        self.flw_2.setText(_translate("Dialog", "flw_2"))
        self.flw_3.setText(_translate("Dialog", "flw_3"))
        self.flw_4.setText(_translate("Dialog", "flw_0"))
        self.flw_5.setText(_translate("Dialog", "flw_1"))
        self.flw_6.setText(_translate("Dialog", "flw_2"))
        self.flw_7.setText(_translate("Dialog", "flw_3"))
        self.flw_8.setText(_translate("Dialog", "flw_0"))
        self.flw_9.setText(_translate("Dialog", "flw_1"))
        self.flw_10.setText(_translate("Dialog", "flw_2"))
        self.flw_11.setText(_translate("Dialog", "flw_3"))
        self.flw_12.setText(_translate("Dialog", "flw_0"))
        self.flw_13.setText(_translate("Dialog", "flw_1"))
        self.flw_14.setText(_translate("Dialog", "flw_2"))
        self.flw_15.setText(_translate("Dialog", "flw_3"))
        self.tile_0.setText(_translate("Dialog", "tile_0"))
        self.tile_1.setText(_translate("Dialog", "tile_1"))
        self.tile_2.setText(_translate("Dialog", "tile_2"))
        self.tile_3.setText(_translate("Dialog", "tile_3"))
        self.tile_4.setText(_translate("Dialog", "tile_0"))
        self.tile_5.setText(_translate("Dialog", "tile_1"))
        self.tile_6.setText(_translate("Dialog", "tile_2"))
        self.tile_7.setText(_translate("Dialog", "tile_3"))
        self.tile_8.setText(_translate("Dialog", "tile_0"))
        self.tile_9.setText(_translate("Dialog", "tile_1"))
        self.tile_10.setText(_translate("Dialog", "tile_2"))
        self.tile_11.setText(_translate("Dialog", "tile_3"))
        self.tile_12.setText(_translate("Dialog", "tile_0"))
        self.tile_13.setText(_translate("Dialog", "tile_1"))
        self.tile_14.setText(_translate("Dialog", "tile_2"))
        self.tile_15.setText(_translate("Dialog", "tile_3"))
        self.tile_16.setText(_translate("Dialog", "tile_3"))
        self.button_eat.setText(_translate("Dialog", "吃"))
        self.button_pon.setText(_translate("Dialog", "碰"))
        self.button_gan.setText(_translate("Dialog", "槓"))
        self.button_win.setText(_translate("Dialog", "胡"))
        self.copilot_msg.setText(_translate("Dialog", "TextLabel"))
        self.text_env.setText(_translate("Dialog", "TextLabel"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = BaseStructure()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
