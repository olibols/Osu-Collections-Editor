# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 376)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/oce.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.collections_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.collections_groupbox.setObjectName("collections_groupbox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.collections_groupbox)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.collection_label = QtWidgets.QLabel(self.collections_groupbox)
        self.collection_label.setObjectName("collection_label")
        self.verticalLayout.addWidget(self.collection_label)
        self.collection_scrollarea = QtWidgets.QScrollArea(self.collections_groupbox)
        self.collection_scrollarea.setWidgetResizable(True)
        self.collection_scrollarea.setObjectName("collection_scrollarea")
        self.collection_scrollarea_contents = QtWidgets.QWidget()
        self.collection_scrollarea_contents.setGeometry(QtCore.QRect(0, 0, 360, 236))
        self.collection_scrollarea_contents.setObjectName("collection_scrollarea_contents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.collection_scrollarea_contents)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.collection_list = QtWidgets.QListWidget(self.collection_scrollarea_contents)
        self.collection_list.setObjectName("collection_list")
        self.verticalLayout_3.addWidget(self.collection_list)
        self.collection_scrollarea.setWidget(self.collection_scrollarea_contents)
        self.verticalLayout.addWidget(self.collection_scrollarea)
        self.collection_button_frame = QtWidgets.QFrame(self.collections_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collection_button_frame.sizePolicy().hasHeightForWidth())
        self.collection_button_frame.setSizePolicy(sizePolicy)
        self.collection_button_frame.setLineWidth(0)
        self.collection_button_frame.setObjectName("collection_button_frame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.collection_button_frame)
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.collection_left_button_frame = QtWidgets.QFrame(self.collection_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collection_left_button_frame.sizePolicy().hasHeightForWidth())
        self.collection_left_button_frame.setSizePolicy(sizePolicy)
        self.collection_left_button_frame.setObjectName("collection_left_button_frame")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.collection_left_button_frame)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.add_collection_button = QtWidgets.QToolButton(self.collection_left_button_frame)
        self.add_collection_button.setMinimumSize(QtCore.QSize(24, 24))
        self.add_collection_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_collection_button.setIcon(icon1)
        self.add_collection_button.setIconSize(QtCore.QSize(16, 16))
        self.add_collection_button.setObjectName("add_collection_button")
        self.horizontalLayout_10.addWidget(self.add_collection_button)
        self.remove_collection_button = QtWidgets.QToolButton(self.collection_left_button_frame)
        self.remove_collection_button.setMinimumSize(QtCore.QSize(24, 24))
        self.remove_collection_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.remove_collection_button.setIcon(icon2)
        self.remove_collection_button.setIconSize(QtCore.QSize(16, 16))
        self.remove_collection_button.setObjectName("remove_collection_button")
        self.horizontalLayout_10.addWidget(self.remove_collection_button)
        self.options_collection_button = QtWidgets.QToolButton(self.collection_left_button_frame)
        self.options_collection_button.setMinimumSize(QtCore.QSize(24, 24))
        self.options_collection_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icons/options.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.options_collection_button.setIcon(icon3)
        self.options_collection_button.setIconSize(QtCore.QSize(16, 16))
        self.options_collection_button.setObjectName("options_collection_button")
        self.horizontalLayout_10.addWidget(self.options_collection_button)
        self.horizontalLayout_4.addWidget(self.collection_left_button_frame, 0, QtCore.Qt.AlignLeft)
        self.collection_right_button_frame = QtWidgets.QFrame(self.collection_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.collection_right_button_frame.sizePolicy().hasHeightForWidth())
        self.collection_right_button_frame.setSizePolicy(sizePolicy)
        self.collection_right_button_frame.setObjectName("collection_right_button_frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.collection_right_button_frame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.up_collection_button = QtWidgets.QToolButton(self.collection_right_button_frame)
        self.up_collection_button.setMinimumSize(QtCore.QSize(24, 24))
        self.up_collection_button.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icons/up.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.up_collection_button.setIcon(icon4)
        self.up_collection_button.setIconSize(QtCore.QSize(16, 16))
        self.up_collection_button.setObjectName("up_collection_button")
        self.horizontalLayout_11.addWidget(self.up_collection_button)
        self.down_collection_button = QtWidgets.QToolButton(self.collection_right_button_frame)
        self.down_collection_button.setMinimumSize(QtCore.QSize(24, 24))
        self.down_collection_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icons/down.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.down_collection_button.setIcon(icon5)
        self.down_collection_button.setIconSize(QtCore.QSize(16, 16))
        self.down_collection_button.setObjectName("down_collection_button")
        self.horizontalLayout_11.addWidget(self.down_collection_button)
        self.horizontalLayout_4.addWidget(self.collection_right_button_frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.collection_button_frame)
        self.horizontalLayout.addWidget(self.collections_groupbox)
        self.songs_groupbox = QtWidgets.QGroupBox(self.centralwidget)
        self.songs_groupbox.setObjectName("songs_groupbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.songs_groupbox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.songs_label = QtWidgets.QLabel(self.songs_groupbox)
        self.songs_label.setObjectName("songs_label")
        self.verticalLayout_2.addWidget(self.songs_label)
        self.songs_scrollarea = QtWidgets.QScrollArea(self.songs_groupbox)
        self.songs_scrollarea.setWidgetResizable(True)
        self.songs_scrollarea.setObjectName("songs_scrollarea")
        self.songs_scrollarea_contents = QtWidgets.QWidget()
        self.songs_scrollarea_contents.setGeometry(QtCore.QRect(0, 0, 360, 236))
        self.songs_scrollarea_contents.setObjectName("songs_scrollarea_contents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.songs_scrollarea_contents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.songs_list = QtWidgets.QListWidget(self.songs_scrollarea_contents)
        self.songs_list.setObjectName("songs_list")
        self.verticalLayout_4.addWidget(self.songs_list)
        self.songs_scrollarea.setWidget(self.songs_scrollarea_contents)
        self.verticalLayout_2.addWidget(self.songs_scrollarea)
        self.songs_button_frame = QtWidgets.QFrame(self.songs_groupbox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songs_button_frame.sizePolicy().hasHeightForWidth())
        self.songs_button_frame.setSizePolicy(sizePolicy)
        self.songs_button_frame.setObjectName("songs_button_frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.songs_button_frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.songs_left_button_frame = QtWidgets.QFrame(self.songs_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songs_left_button_frame.sizePolicy().hasHeightForWidth())
        self.songs_left_button_frame.setSizePolicy(sizePolicy)
        self.songs_left_button_frame.setObjectName("songs_left_button_frame")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.songs_left_button_frame)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.songs_add_button = QtWidgets.QToolButton(self.songs_left_button_frame)
        self.songs_add_button.setMinimumSize(QtCore.QSize(24, 24))
        self.songs_add_button.setText("")
        self.songs_add_button.setIcon(icon1)
        self.songs_add_button.setIconSize(QtCore.QSize(16, 16))
        self.songs_add_button.setObjectName("songs_add_button")
        self.horizontalLayout_9.addWidget(self.songs_add_button)
        self.songs_remove_button = QtWidgets.QToolButton(self.songs_left_button_frame)
        self.songs_remove_button.setMinimumSize(QtCore.QSize(24, 24))
        self.songs_remove_button.setText("")
        self.songs_remove_button.setIcon(icon2)
        self.songs_remove_button.setIconSize(QtCore.QSize(16, 16))
        self.songs_remove_button.setObjectName("songs_remove_button")
        self.horizontalLayout_9.addWidget(self.songs_remove_button)
        self.songs_options_button = QtWidgets.QToolButton(self.songs_left_button_frame)
        self.songs_options_button.setMinimumSize(QtCore.QSize(24, 24))
        self.songs_options_button.setText("")
        self.songs_options_button.setIcon(icon3)
        self.songs_options_button.setIconSize(QtCore.QSize(16, 16))
        self.songs_options_button.setObjectName("songs_options_button")
        self.horizontalLayout_9.addWidget(self.songs_options_button)
        self.horizontalLayout_6.addWidget(self.songs_left_button_frame)
        self.songs_right_button_frame = QtWidgets.QFrame(self.songs_button_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.songs_right_button_frame.sizePolicy().hasHeightForWidth())
        self.songs_right_button_frame.setSizePolicy(sizePolicy)
        self.songs_right_button_frame.setObjectName("songs_right_button_frame")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.songs_right_button_frame)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.songs_up_button = QtWidgets.QToolButton(self.songs_right_button_frame)
        self.songs_up_button.setMinimumSize(QtCore.QSize(24, 24))
        self.songs_up_button.setText("")
        self.songs_up_button.setIcon(icon4)
        self.songs_up_button.setIconSize(QtCore.QSize(16, 16))
        self.songs_up_button.setObjectName("songs_up_button")
        self.horizontalLayout_8.addWidget(self.songs_up_button)
        self.songs_down_button = QtWidgets.QToolButton(self.songs_right_button_frame)
        self.songs_down_button.setMinimumSize(QtCore.QSize(24, 24))
        self.songs_down_button.setText("")
        self.songs_down_button.setIcon(icon5)
        self.songs_down_button.setIconSize(QtCore.QSize(16, 16))
        self.songs_down_button.setObjectName("songs_down_button")
        self.horizontalLayout_8.addWidget(self.songs_down_button)
        self.horizontalLayout_6.addWidget(self.songs_right_button_frame, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_2.addWidget(self.songs_button_frame)
        self.horizontalLayout.addWidget(self.songs_groupbox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName("action_open")
        self.action_about = QtWidgets.QAction(MainWindow)
        self.action_about.setObjectName("action_about")
        self.action_exit = QtWidgets.QAction(MainWindow)
        self.action_exit.setObjectName("action_exit")
        self.menu_file.addAction(self.action_open)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        self.menu_help.addAction(self.action_about)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "osu! Collection Editor"))
        self.collections_groupbox.setTitle(_translate("MainWindow", "Collections"))
        self.collection_label.setText(_translate("MainWindow", "No collection.db loaded."))
        self.add_collection_button.setStatusTip(_translate("MainWindow", "Add collection"))
        self.remove_collection_button.setStatusTip(_translate("MainWindow", "Remove selected collection"))
        self.options_collection_button.setStatusTip(_translate("MainWindow", "Collection options"))
        self.up_collection_button.setStatusTip(_translate("MainWindow", "Move selected collection up"))
        self.down_collection_button.setStatusTip(_translate("MainWindow", "Move selected collection down"))
        self.songs_groupbox.setTitle(_translate("MainWindow", "Songs"))
        self.songs_label.setText(_translate("MainWindow", "No collection selected."))
        self.songs_add_button.setStatusTip(_translate("MainWindow", "Add song to this collection"))
        self.songs_remove_button.setStatusTip(_translate("MainWindow", "Remove selected song from this collection"))
        self.songs_options_button.setStatusTip(_translate("MainWindow", "Song options"))
        self.songs_up_button.setStatusTip(_translate("MainWindow", "Move selected song up"))
        self.songs_down_button.setStatusTip(_translate("MainWindow", "Move selected song down"))
        self.menu_file.setStatusTip(_translate("MainWindow", "File"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_help.setStatusTip(_translate("MainWindow", "Help"))
        self.menu_help.setTitle(_translate("MainWindow", "Help"))
        self.action_open.setText(_translate("MainWindow", "Open"))
        self.action_open.setStatusTip(_translate("MainWindow", "Open collection"))
        self.action_open.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.action_about.setText(_translate("MainWindow", "About"))
        self.action_about.setStatusTip(_translate("MainWindow", "Information about this program"))
        self.action_exit.setText(_translate("MainWindow", "Exit"))
        self.action_exit.setToolTip(_translate("MainWindow", "Exit program"))
        self.action_exit.setStatusTip(_translate("MainWindow", "Exit program"))
        self.action_exit.setShortcut(_translate("MainWindow", "Ctrl+Q"))

