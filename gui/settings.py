# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.resize(624, 391)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/oce.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        SettingsDialog.setWindowIcon(icon)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.settings_layout = QtWidgets.QVBoxLayout()
        self.settings_layout.setObjectName("settings_layout")
        self.api_box = QtWidgets.QGroupBox(SettingsDialog)
        self.api_box.setEnabled(True)
        self.api_box.setCheckable(False)
        self.api_box.setChecked(False)
        self.api_box.setObjectName("api_box")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.api_box)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.api_key_layout = QtWidgets.QHBoxLayout()
        self.api_key_layout.setObjectName("api_key_layout")
        self.api_key_label = QtWidgets.QLabel(self.api_box)
        self.api_key_label.setObjectName("api_key_label")
        self.api_key_layout.addWidget(self.api_key_label)
        self.api_key_line = QtWidgets.QLineEdit(self.api_box)
        self.api_key_line.setObjectName("api_key_line")
        self.api_key_layout.addWidget(self.api_key_line)
        self.verticalLayout_3.addLayout(self.api_key_layout)
        self.download_api_layout = QtWidgets.QHBoxLayout()
        self.download_api_layout.setObjectName("download_api_layout")
        self.download_api_label = QtWidgets.QLabel(self.api_box)
        self.download_api_label.setObjectName("download_api_label")
        self.download_api_layout.addWidget(self.download_api_label)
        self.download_api_combobox = QtWidgets.QComboBox(self.api_box)
        self.download_api_combobox.setObjectName("download_api_combobox")
        self.download_api_combobox.addItem("")
        self.download_api_combobox.addItem("")
        self.download_api_combobox.addItem("")
        self.download_api_layout.addWidget(self.download_api_combobox)
        self.verticalLayout_3.addLayout(self.download_api_layout)
        self.settings_layout.addWidget(self.api_box)
        self.default_folders_box = QtWidgets.QGroupBox(SettingsDialog)
        self.default_folders_box.setObjectName("default_folders_box")
        self.formLayout_2 = QtWidgets.QFormLayout(self.default_folders_box)
        self.formLayout_2.setObjectName("formLayout_2")
        self.default_songs_label = QtWidgets.QLabel(self.default_folders_box)
        self.default_songs_label.setObjectName("default_songs_label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.default_songs_label)
        self.default_collection_label = QtWidgets.QLabel(self.default_folders_box)
        self.default_collection_label.setObjectName("default_collection_label")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.default_collection_label)
        self.default_songs_layout = QtWidgets.QHBoxLayout()
        self.default_songs_layout.setObjectName("default_songs_layout")
        self.default_songs_line = QtWidgets.QLineEdit(self.default_folders_box)
        self.default_songs_line.setObjectName("default_songs_line")
        self.default_songs_layout.addWidget(self.default_songs_line)
        self.default_songs_button = QtWidgets.QPushButton(self.default_folders_box)
        self.default_songs_button.setObjectName("default_songs_button")
        self.default_songs_layout.addWidget(self.default_songs_button)
        self.formLayout_2.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.default_songs_layout)
        self.default_collection_layout = QtWidgets.QHBoxLayout()
        self.default_collection_layout.setObjectName("default_collection_layout")
        self.default_collection_line = QtWidgets.QLineEdit(self.default_folders_box)
        self.default_collection_line.setObjectName("default_collection_line")
        self.default_collection_layout.addWidget(self.default_collection_line)
        self.default_collection_button = QtWidgets.QPushButton(self.default_folders_box)
        self.default_collection_button.setObjectName("default_collection_button")
        self.default_collection_layout.addWidget(self.default_collection_button)
        self.formLayout_2.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.default_collection_layout)
        self.settings_layout.addWidget(self.default_folders_box)
        self.dialog_settings_box = QtWidgets.QGroupBox(SettingsDialog)
        self.dialog_settings_box.setObjectName("dialog_settings_box")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dialog_settings_box)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.shutdown_dialog_checkbox = QtWidgets.QCheckBox(self.dialog_settings_box)
        self.shutdown_dialog_checkbox.setChecked(True)
        self.shutdown_dialog_checkbox.setObjectName("shutdown_dialog_checkbox")
        self.verticalLayout_2.addWidget(self.shutdown_dialog_checkbox)
        self.api_explanation_dialog = QtWidgets.QCheckBox(self.dialog_settings_box)
        self.api_explanation_dialog.setChecked(True)
        self.api_explanation_dialog.setObjectName("api_explanation_dialog")
        self.verticalLayout_2.addWidget(self.api_explanation_dialog)
        self.collection_delete_dialog = QtWidgets.QCheckBox(self.dialog_settings_box)
        self.collection_delete_dialog.setChecked(True)
        self.collection_delete_dialog.setObjectName("collection_delete_dialog")
        self.verticalLayout_2.addWidget(self.collection_delete_dialog)
        self.song_remove_dialog = QtWidgets.QCheckBox(self.dialog_settings_box)
        self.song_remove_dialog.setChecked(True)
        self.song_remove_dialog.setObjectName("song_remove_dialog")
        self.verticalLayout_2.addWidget(self.song_remove_dialog)
        self.mapset_remove_dialog = QtWidgets.QCheckBox(self.dialog_settings_box)
        self.mapset_remove_dialog.setChecked(True)
        self.mapset_remove_dialog.setObjectName("mapset_remove_dialog")
        self.verticalLayout_2.addWidget(self.mapset_remove_dialog)
        self.settings_layout.addWidget(self.dialog_settings_box)
        self.verticalLayout.addLayout(self.settings_layout)
        self.button_box = QtWidgets.QDialogButtonBox(SettingsDialog)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.api_box.setTitle(_translate("SettingsDialog", "Osu! API"))
        self.api_key_label.setText(_translate("SettingsDialog", "Osu! API Key"))
        self.download_api_label.setText(_translate("SettingsDialog", "Download song info from API?"))
        self.download_api_combobox.setItemText(0, _translate("SettingsDialog", "Ask"))
        self.download_api_combobox.setItemText(1, _translate("SettingsDialog", "Always"))
        self.download_api_combobox.setItemText(2, _translate("SettingsDialog", "Never"))
        self.default_folders_box.setTitle(_translate("SettingsDialog", "Default Folders"))
        self.default_songs_label.setText(_translate("SettingsDialog", "Default Songs folder"))
        self.default_collection_label.setText(_translate("SettingsDialog", "Default collection.db"))
        self.default_songs_button.setText(_translate("SettingsDialog", "Browse"))
        self.default_collection_button.setText(_translate("SettingsDialog", "Browse"))
        self.dialog_settings_box.setTitle(_translate("SettingsDialog", "Dialog Settings"))
        self.shutdown_dialog_checkbox.setText(_translate("SettingsDialog", "Show shutdown dialog when I exit the program."))
        self.api_explanation_dialog.setText(_translate("SettingsDialog", "Show API icon explanation dialogs."))
        self.collection_delete_dialog.setText(_translate("SettingsDialog", "Show collection delete confirmation."))
        self.song_remove_dialog.setText(_translate("SettingsDialog", "Show remove song from collection confirmation."))
        self.mapset_remove_dialog.setText(_translate("SettingsDialog", "Show remove mapset from collection confirmation."))
