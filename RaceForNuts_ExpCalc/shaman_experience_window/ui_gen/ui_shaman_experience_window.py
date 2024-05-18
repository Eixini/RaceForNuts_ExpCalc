# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shaman_experience_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_ShamanExperienceWindow(object):
    def setupUi(self, ShamanExperienceWindow):
        if not ShamanExperienceWindow.objectName():
            ShamanExperienceWindow.setObjectName(u"ShamanExperienceWindow")
        ShamanExperienceWindow.resize(684, 661)
        self.verticalLayout_3 = QVBoxLayout(ShamanExperienceWindow)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.level_combobox_label = QLabel(ShamanExperienceWindow)
        self.level_combobox_label.setObjectName(u"level_combobox_label")

        self.horizontalLayout_2.addWidget(self.level_combobox_label)

        self.current_level_spinbox = QSpinBox(ShamanExperienceWindow)
        self.current_level_spinbox.setObjectName(u"current_level_spinbox")
        self.current_level_spinbox.setMaximum(200)

        self.horizontalLayout_2.addWidget(self.current_level_spinbox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.level_combobox_label_2 = QLabel(ShamanExperienceWindow)
        self.level_combobox_label_2.setObjectName(u"level_combobox_label_2")

        self.horizontalLayout_3.addWidget(self.level_combobox_label_2)

        self.experience_spinbox = QSpinBox(ShamanExperienceWindow)
        self.experience_spinbox.setObjectName(u"experience_spinbox")
        self.experience_spinbox.setMaximum(999999999)

        self.horizontalLayout_3.addWidget(self.experience_spinbox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.target_level_combobox_label = QLabel(ShamanExperienceWindow)
        self.target_level_combobox_label.setObjectName(u"target_level_combobox_label")

        self.horizontalLayout.addWidget(self.target_level_combobox_label)

        self.target_level_spinbox = QSpinBox(ShamanExperienceWindow)
        self.target_level_spinbox.setObjectName(u"target_level_spinbox")
        self.target_level_spinbox.setMaximum(200)

        self.horizontalLayout.addWidget(self.target_level_spinbox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.label = QLabel(ShamanExperienceWindow)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setBold(True)
        self.label.setFont(font)

        self.verticalLayout_3.addWidget(self.label)

        self.exp_info_table = QTableWidget(ShamanExperienceWindow)
        if (self.exp_info_table.columnCount() < 3):
            self.exp_info_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.exp_info_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.exp_info_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.exp_info_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.exp_info_table.rowCount() < 6):
            self.exp_info_table.setRowCount(6)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.exp_info_table.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.exp_info_table.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.exp_info_table.setItem(0, 2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.exp_info_table.setItem(1, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.exp_info_table.setItem(1, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.exp_info_table.setItem(1, 2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.exp_info_table.setItem(2, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.exp_info_table.setItem(2, 1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.exp_info_table.setItem(2, 2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.exp_info_table.setItem(3, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.exp_info_table.setItem(3, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.exp_info_table.setItem(3, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.exp_info_table.setItem(4, 0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.exp_info_table.setItem(4, 1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.exp_info_table.setItem(4, 2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.exp_info_table.setItem(5, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.exp_info_table.setItem(5, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.exp_info_table.setItem(5, 2, __qtablewidgetitem20)
        self.exp_info_table.setObjectName(u"exp_info_table")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exp_info_table.sizePolicy().hasHeightForWidth())
        self.exp_info_table.setSizePolicy(sizePolicy)
        self.exp_info_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.exp_info_table.setTabKeyNavigation(False)
        self.exp_info_table.setProperty("showDropIndicator", False)
        self.exp_info_table.setDragDropOverwriteMode(False)
        self.exp_info_table.setAlternatingRowColors(False)
        self.exp_info_table.setRowCount(6)
        self.exp_info_table.setColumnCount(3)
        self.exp_info_table.horizontalHeader().setVisible(True)
        self.exp_info_table.horizontalHeader().setCascadingSectionResizes(False)
        self.exp_info_table.horizontalHeader().setHighlightSections(False)
        self.exp_info_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.exp_info_table.horizontalHeader().setStretchLastSection(True)
        self.exp_info_table.verticalHeader().setVisible(False)
        self.exp_info_table.verticalHeader().setCascadingSectionResizes(True)
        self.exp_info_table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.exp_info_table)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.result_button = QPushButton(ShamanExperienceWindow)
        self.result_button.setObjectName(u"result_button")

        self.horizontalLayout_6.addWidget(self.result_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.current_level_label = QLabel(ShamanExperienceWindow)
        self.current_level_label.setObjectName(u"current_level_label")
        font1 = QFont()
        font1.setFamilies([u"Ubuntu"])
        self.current_level_label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.current_level_label)

        self.current_level_value_label = QLabel(ShamanExperienceWindow)
        self.current_level_value_label.setObjectName(u"current_level_value_label")
        self.current_level_value_label.setFont(font1)

        self.horizontalLayout_9.addWidget(self.current_level_value_label)


        self.verticalLayout.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.target_level_label = QLabel(ShamanExperienceWindow)
        self.target_level_label.setObjectName(u"target_level_label")
        self.target_level_label.setFont(font1)

        self.horizontalLayout_10.addWidget(self.target_level_label)

        self.target_level_value_label = QLabel(ShamanExperienceWindow)
        self.target_level_value_label.setObjectName(u"target_level_value_label")
        self.target_level_value_label.setFont(font1)

        self.horizontalLayout_10.addWidget(self.target_level_value_label)


        self.verticalLayout.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.current_level_exp_label = QLabel(ShamanExperienceWindow)
        self.current_level_exp_label.setObjectName(u"current_level_exp_label")
        self.current_level_exp_label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.current_level_exp_label)

        self.current_level_exp_value_label = QLabel(ShamanExperienceWindow)
        self.current_level_exp_value_label.setObjectName(u"current_level_exp_value_label")
        self.current_level_exp_value_label.setFont(font1)

        self.horizontalLayout_8.addWidget(self.current_level_exp_value_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.target_level_exp_label = QLabel(ShamanExperienceWindow)
        self.target_level_exp_label.setObjectName(u"target_level_exp_label")
        self.target_level_exp_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.target_level_exp_label)

        self.target_level_exp_value_label = QLabel(ShamanExperienceWindow)
        self.target_level_exp_value_label.setObjectName(u"target_level_exp_value_label")
        self.target_level_exp_value_label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.target_level_exp_value_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_11.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.result_table = QTableWidget(ShamanExperienceWindow)
        if (self.result_table.columnCount() < 3):
            self.result_table.setColumnCount(3)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        if (self.result_table.rowCount() < 6):
            self.result_table.setRowCount(6)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.result_table.setItem(0, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.result_table.setItem(0, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.result_table.setItem(0, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.result_table.setItem(1, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.result_table.setItem(1, 1, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.result_table.setItem(1, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.result_table.setItem(2, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.result_table.setItem(2, 1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.result_table.setItem(2, 2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.result_table.setItem(3, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.result_table.setItem(3, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.result_table.setItem(3, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.result_table.setItem(4, 0, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.result_table.setItem(4, 1, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.result_table.setItem(4, 2, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.result_table.setItem(5, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.result_table.setItem(5, 1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.result_table.setItem(5, 2, __qtablewidgetitem41)
        self.result_table.setObjectName(u"result_table")
        sizePolicy.setHeightForWidth(self.result_table.sizePolicy().hasHeightForWidth())
        self.result_table.setSizePolicy(sizePolicy)
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_table.setTabKeyNavigation(False)
        self.result_table.setProperty("showDropIndicator", False)
        self.result_table.setDragDropOverwriteMode(False)
        self.result_table.setAlternatingRowColors(False)
        self.result_table.setRowCount(6)
        self.result_table.setColumnCount(3)
        self.result_table.horizontalHeader().setVisible(True)
        self.result_table.horizontalHeader().setCascadingSectionResizes(False)
        self.result_table.horizontalHeader().setHighlightSections(False)
        self.result_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.result_table.verticalHeader().setVisible(False)
        self.result_table.verticalHeader().setCascadingSectionResizes(True)
        self.result_table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.result_table)


        self.retranslateUi(ShamanExperienceWindow)

        QMetaObject.connectSlotsByName(ShamanExperienceWindow)
    # setupUi

    def retranslateUi(self, ShamanExperienceWindow):
        ShamanExperienceWindow.setWindowTitle(QCoreApplication.translate("ShamanExperienceWindow", u"Form", None))
        self.level_combobox_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.level_combobox_label_2.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0414\u043e \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u043e\u043f\u044b\u0442\u0430", None))
        self.target_level_combobox_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041e\u043f\u044b\u0442 \u0437\u0430 1  \u0437\u0430\u0432\u0435\u0434\u0435\u043d\u043d\u0443\u044e \u0431\u0435\u043b\u043a\u0443 \u0432 \u0434\u0443\u043f\u043b\u043e:", None))
        ___qtablewidgetitem = self.exp_info_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041b\u043e\u043a\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem1 = self.exp_info_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041e\u043f\u044b\u0442", None));
        ___qtablewidgetitem2 = self.exp_info_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041e\u043f\u044b\u0442 \u0441 VIP", None));

        __sortingEnabled = self.exp_info_table.isSortingEnabled()
        self.exp_info_table.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.exp_info_table.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0421\u043e\u043b\u043d\u0435\u0447\u043d\u044b\u0435 \u0434\u043e\u043b\u0438\u043d\u044b", None));
        ___qtablewidgetitem4 = self.exp_info_table.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ShamanExperienceWindow", u"4", None));
        ___qtablewidgetitem5 = self.exp_info_table.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ShamanExperienceWindow", u"8", None));
        ___qtablewidgetitem6 = self.exp_info_table.item(1, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0422\u043e\u043f\u0438", None));
        ___qtablewidgetitem7 = self.exp_info_table.item(1, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ShamanExperienceWindow", u"7", None));
        ___qtablewidgetitem8 = self.exp_info_table.item(1, 2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ShamanExperienceWindow", u"14", None));
        ___qtablewidgetitem9 = self.exp_info_table.item(2, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0428\u0442\u043e\u0440\u043c", None));
        ___qtablewidgetitem10 = self.exp_info_table.item(2, 1)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ShamanExperienceWindow", u"19", None));
        ___qtablewidgetitem11 = self.exp_info_table.item(2, 2)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ShamanExperienceWindow", u"38", None));
        ___qtablewidgetitem12 = self.exp_info_table.item(3, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0418\u0441\u043f\u044b\u0442\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem13 = self.exp_info_table.item(3, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ShamanExperienceWindow", u"13", None));
        ___qtablewidgetitem14 = self.exp_info_table.item(3, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ShamanExperienceWindow", u"26", None));
        ___qtablewidgetitem15 = self.exp_info_table.item(4, 0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041f\u0443\u0441\u0442\u044b\u043d\u044f", None));
        ___qtablewidgetitem16 = self.exp_info_table.item(4, 1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ShamanExperienceWindow", u"17", None));
        ___qtablewidgetitem17 = self.exp_info_table.item(4, 2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ShamanExperienceWindow", u"34", None));
        ___qtablewidgetitem18 = self.exp_info_table.item(5, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0410\u043d\u043e\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u043e\u043d\u0430", None));
        ___qtablewidgetitem19 = self.exp_info_table.item(5, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("ShamanExperienceWindow", u"21", None));
        ___qtablewidgetitem20 = self.exp_info_table.item(5, 2)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ShamanExperienceWindow", u"42", None));
        self.exp_info_table.setSortingEnabled(__sortingEnabled)

        self.result_button.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.current_level_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c:", None))
        self.current_level_value_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None))
        self.target_level_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0426\u0435\u043b\u0435\u0432\u043e\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c:", None))
        self.target_level_value_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None))
        self.current_level_exp_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043e\u043f\u044b\u0442 \u0443\u0440\u043e\u0432\u043d\u044f:", None))
        self.current_level_exp_value_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None))
        self.target_level_exp_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u043f\u044b\u0442\u0430:", None))
        self.target_level_exp_value_label.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None))
        ___qtablewidgetitem21 = self.result_table.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041b\u043e\u043a\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem22 = self.result_table.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0431\u0435\u043b\u043e\u043a", None));
        ___qtablewidgetitem23 = self.result_table.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041a\u043e\u043b-\u0432\u043e \u0431\u0435\u043b\u043e\u043a (\u0448\u0430\u043c \u0441 VIP)", None));

        __sortingEnabled1 = self.result_table.isSortingEnabled()
        self.result_table.setSortingEnabled(False)
        ___qtablewidgetitem24 = self.result_table.item(0, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0421\u043e\u043b\u043d\u0435\u0447\u043d\u044b\u0435 \u0434\u043e\u043b\u0438\u043d\u044b", None));
        ___qtablewidgetitem25 = self.result_table.item(0, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem26 = self.result_table.item(0, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem27 = self.result_table.item(1, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0422\u043e\u043f\u0438", None));
        ___qtablewidgetitem28 = self.result_table.item(1, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem29 = self.result_table.item(1, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem30 = self.result_table.item(2, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0428\u0442\u043e\u0440\u043c", None));
        ___qtablewidgetitem31 = self.result_table.item(2, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem32 = self.result_table.item(2, 2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem33 = self.result_table.item(3, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0418\u0441\u043f\u044b\u0442\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem34 = self.result_table.item(3, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem35 = self.result_table.item(3, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem36 = self.result_table.item(4, 0)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u041f\u0443\u0441\u0442\u044b\u043d\u044f", None));
        ___qtablewidgetitem37 = self.result_table.item(4, 1)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem38 = self.result_table.item(4, 2)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem39 = self.result_table.item(5, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("ShamanExperienceWindow", u"\u0410\u043d\u043e\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u043e\u043d\u0430", None));
        ___qtablewidgetitem40 = self.result_table.item(5, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        ___qtablewidgetitem41 = self.result_table.item(5, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("ShamanExperienceWindow", u"0", None));
        self.result_table.setSortingEnabled(__sortingEnabled1)

    # retranslateUi

