# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'race_for_nuts_experience.ui'
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

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.setEnabled(True)
        Window.resize(775, 677)
        self.verticalLayout_3 = QVBoxLayout(Window)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.level_combobox_label = QLabel(Window)
        self.level_combobox_label.setObjectName(u"level_combobox_label")

        self.horizontalLayout.addWidget(self.level_combobox_label)

        self.current_level_spinbox = QSpinBox(Window)
        self.current_level_spinbox.setObjectName(u"current_level_spinbox")
        self.current_level_spinbox.setMaximum(200)

        self.horizontalLayout.addWidget(self.current_level_spinbox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.level_combobox_label_2 = QLabel(Window)
        self.level_combobox_label_2.setObjectName(u"level_combobox_label_2")

        self.horizontalLayout_2.addWidget(self.level_combobox_label_2)

        self.experience_spinbox = QSpinBox(Window)
        self.experience_spinbox.setObjectName(u"experience_spinbox")
        self.experience_spinbox.setMaximum(999999999)

        self.horizontalLayout_2.addWidget(self.experience_spinbox)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.target_level_combobox_label = QLabel(Window)
        self.target_level_combobox_label.setObjectName(u"target_level_combobox_label")

        self.horizontalLayout_3.addWidget(self.target_level_combobox_label)

        self.target_level_spinbox = QSpinBox(Window)
        self.target_level_spinbox.setObjectName(u"target_level_spinbox")
        self.target_level_spinbox.setMaximum(200)

        self.horizontalLayout_3.addWidget(self.target_level_spinbox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.exp_info_table = QTableWidget(Window)
        if (self.exp_info_table.columnCount() < 4):
            self.exp_info_table.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.exp_info_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.exp_info_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.exp_info_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.exp_info_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.exp_info_table.rowCount() < 6):
            self.exp_info_table.setRowCount(6)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.exp_info_table.setItem(0, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.exp_info_table.setItem(0, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.exp_info_table.setItem(0, 2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.exp_info_table.setItem(0, 3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.exp_info_table.setItem(1, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.exp_info_table.setItem(1, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.exp_info_table.setItem(1, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.exp_info_table.setItem(1, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.exp_info_table.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.exp_info_table.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.exp_info_table.setItem(2, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.exp_info_table.setItem(2, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.exp_info_table.setItem(3, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.exp_info_table.setItem(3, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.exp_info_table.setItem(3, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.exp_info_table.setItem(3, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.exp_info_table.setItem(4, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.exp_info_table.setItem(4, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.exp_info_table.setItem(4, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.exp_info_table.setItem(4, 3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.exp_info_table.setItem(5, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.exp_info_table.setItem(5, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.exp_info_table.setItem(5, 2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.exp_info_table.setItem(5, 3, __qtablewidgetitem27)
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
        self.exp_info_table.setColumnCount(4)
        self.exp_info_table.horizontalHeader().setVisible(True)
        self.exp_info_table.horizontalHeader().setCascadingSectionResizes(False)
        self.exp_info_table.horizontalHeader().setHighlightSections(False)
        self.exp_info_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.exp_info_table.horizontalHeader().setStretchLastSection(True)
        self.exp_info_table.verticalHeader().setVisible(False)
        self.exp_info_table.verticalHeader().setCascadingSectionResizes(True)
        self.exp_info_table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.exp_info_table)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.result_button = QPushButton(Window)
        self.result_button.setObjectName(u"result_button")

        self.horizontalLayout_4.addWidget(self.result_button)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.current_level_label = QLabel(Window)
        self.current_level_label.setObjectName(u"current_level_label")
        font = QFont()
        font.setFamilies([u"Ubuntu"])
        self.current_level_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.current_level_label)

        self.current_level_value_label = QLabel(Window)
        self.current_level_value_label.setObjectName(u"current_level_value_label")
        self.current_level_value_label.setFont(font)

        self.horizontalLayout_6.addWidget(self.current_level_value_label)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.target_level_label = QLabel(Window)
        self.target_level_label.setObjectName(u"target_level_label")
        self.target_level_label.setFont(font)

        self.horizontalLayout_7.addWidget(self.target_level_label)

        self.target_level_value_label = QLabel(Window)
        self.target_level_value_label.setObjectName(u"target_level_value_label")
        self.target_level_value_label.setFont(font)

        self.horizontalLayout_7.addWidget(self.target_level_value_label)


        self.verticalLayout.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_10.addLayout(self.verticalLayout)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.current_level_exp_label = QLabel(Window)
        self.current_level_exp_label.setObjectName(u"current_level_exp_label")
        self.current_level_exp_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.current_level_exp_label)

        self.current_level_exp_value_label = QLabel(Window)
        self.current_level_exp_value_label.setObjectName(u"current_level_exp_value_label")
        self.current_level_exp_value_label.setFont(font)

        self.horizontalLayout_8.addWidget(self.current_level_exp_value_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.target_level_exp_label = QLabel(Window)
        self.target_level_exp_label.setObjectName(u"target_level_exp_label")
        self.target_level_exp_label.setFont(font)

        self.horizontalLayout_9.addWidget(self.target_level_exp_label)

        self.target_level_exp_value_label = QLabel(Window)
        self.target_level_exp_value_label.setObjectName(u"target_level_exp_value_label")
        self.target_level_exp_value_label.setFont(font)

        self.horizontalLayout_9.addWidget(self.target_level_exp_value_label)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)


        self.horizontalLayout_10.addLayout(self.verticalLayout_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.result_table = QTableWidget(Window)
        if (self.result_table.columnCount() < 5):
            self.result_table.setColumnCount(5)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.result_table.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        if (self.result_table.rowCount() < 6):
            self.result_table.setRowCount(6)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.result_table.setItem(0, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.result_table.setItem(0, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.result_table.setItem(0, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.result_table.setItem(0, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.result_table.setItem(0, 4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.result_table.setItem(1, 0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.result_table.setItem(1, 1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.result_table.setItem(1, 2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.result_table.setItem(1, 3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.result_table.setItem(1, 4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.result_table.setItem(2, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.result_table.setItem(2, 1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.result_table.setItem(2, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.result_table.setItem(2, 3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.result_table.setItem(2, 4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.result_table.setItem(3, 0, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.result_table.setItem(3, 1, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.result_table.setItem(3, 2, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.result_table.setItem(3, 3, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.result_table.setItem(3, 4, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.result_table.setItem(4, 0, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.result_table.setItem(4, 1, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.result_table.setItem(4, 2, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.result_table.setItem(4, 3, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.result_table.setItem(4, 4, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.result_table.setItem(5, 0, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.result_table.setItem(5, 1, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.result_table.setItem(5, 2, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.result_table.setItem(5, 3, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.result_table.setItem(5, 4, __qtablewidgetitem62)
        self.result_table.setObjectName(u"result_table")
        sizePolicy.setHeightForWidth(self.result_table.sizePolicy().hasHeightForWidth())
        self.result_table.setSizePolicy(sizePolicy)
        self.result_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.result_table.setTabKeyNavigation(False)
        self.result_table.setProperty("showDropIndicator", False)
        self.result_table.setDragDropOverwriteMode(False)
        self.result_table.setAlternatingRowColors(False)
        self.result_table.setRowCount(6)
        self.result_table.setColumnCount(5)
        self.result_table.horizontalHeader().setVisible(True)
        self.result_table.horizontalHeader().setCascadingSectionResizes(False)
        self.result_table.horizontalHeader().setHighlightSections(False)
        self.result_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.result_table.horizontalHeader().setStretchLastSection(True)
        self.result_table.verticalHeader().setVisible(False)
        self.result_table.verticalHeader().setCascadingSectionResizes(True)
        self.result_table.verticalHeader().setStretchLastSection(True)

        self.verticalLayout_3.addWidget(self.result_table)

        self.label = QLabel(Window)
        self.label.setObjectName(u"label")

        self.verticalLayout_3.addWidget(self.label)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"\u0422\u0440\u0430\u0433\u0435\u0434\u0438\u044f \u0431\u0435\u043b\u043e\u043a - \u043a\u0430\u043b\u044c\u043a\u0443\u043b\u044f\u0442\u043e\u0440 \u043e\u043f\u044b\u0442\u0430", None))
        self.level_combobox_label.setText(QCoreApplication.translate("Window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0442\u0435\u043a\u0443\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        self.level_combobox_label_2.setText(QCoreApplication.translate("Window", u"\u0414\u043e \u0441\u043b\u0435\u0434\u0443\u044e\u0449\u0435\u0433\u043e \u0443\u0440\u043e\u0432\u043d\u044f \u043e\u0441\u0442\u0430\u043b\u043e\u0441\u044c \u043e\u043f\u044b\u0442\u0430", None))
        self.target_level_combobox_label.setText(QCoreApplication.translate("Window", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0436\u0435\u043b\u0430\u0435\u043c\u044b\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c", None))
        ___qtablewidgetitem = self.exp_info_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Window", u"\u041b\u043e\u043a\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem1 = self.exp_info_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Window", u"\u041e\u043f\u044b\u0442", None));
        ___qtablewidgetitem2 = self.exp_info_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Window", u"\u041e\u043f\u044b\u0442 \u0441 VIP", None));
        ___qtablewidgetitem3 = self.exp_info_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Window", u"\u041e\u0440\u0435\u0445\u0438", None));

        __sortingEnabled = self.exp_info_table.isSortingEnabled()
        self.exp_info_table.setSortingEnabled(False)
        ___qtablewidgetitem4 = self.exp_info_table.item(0, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Window", u"\u0421\u043e\u043b\u043d\u0435\u0447\u043d\u044b\u0435 \u0434\u043e\u043b\u0438\u043d\u044b", None));
        ___qtablewidgetitem5 = self.exp_info_table.item(0, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Window", u"25", None));
        ___qtablewidgetitem6 = self.exp_info_table.item(0, 2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Window", u"50", None));
        ___qtablewidgetitem7 = self.exp_info_table.item(0, 3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Window", u"5", None));
        ___qtablewidgetitem8 = self.exp_info_table.item(1, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Window", u"\u0422\u043e\u043f\u0438", None));
        ___qtablewidgetitem9 = self.exp_info_table.item(1, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Window", u"40", None));
        ___qtablewidgetitem10 = self.exp_info_table.item(1, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Window", u"80", None));
        ___qtablewidgetitem11 = self.exp_info_table.item(1, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Window", u"6", None));
        ___qtablewidgetitem12 = self.exp_info_table.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Window", u"\u0428\u0442\u043e\u0440\u043c", None));
        ___qtablewidgetitem13 = self.exp_info_table.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Window", u"40", None));
        ___qtablewidgetitem14 = self.exp_info_table.item(2, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Window", u"80", None));
        ___qtablewidgetitem15 = self.exp_info_table.item(2, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Window", u"7", None));
        ___qtablewidgetitem16 = self.exp_info_table.item(3, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Window", u"\u0418\u0441\u043f\u044b\u0442\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem17 = self.exp_info_table.item(3, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Window", u"70", None));
        ___qtablewidgetitem18 = self.exp_info_table.item(3, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Window", u"140", None));
        ___qtablewidgetitem19 = self.exp_info_table.item(3, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Window", u"8", None));
        ___qtablewidgetitem20 = self.exp_info_table.item(4, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Window", u"\u041f\u0443\u0441\u0442\u044b\u043d\u044f", None));
        ___qtablewidgetitem21 = self.exp_info_table.item(4, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Window", u"60", None));
        ___qtablewidgetitem22 = self.exp_info_table.item(4, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Window", u"120", None));
        ___qtablewidgetitem23 = self.exp_info_table.item(4, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Window", u"8", None));
        ___qtablewidgetitem24 = self.exp_info_table.item(5, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Window", u"\u0410\u043d\u043e\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u043e\u043d\u0430", None));
        ___qtablewidgetitem25 = self.exp_info_table.item(5, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Window", u"80", None));
        ___qtablewidgetitem26 = self.exp_info_table.item(5, 2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("Window", u"160", None));
        ___qtablewidgetitem27 = self.exp_info_table.item(5, 3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("Window", u"10", None));
        self.exp_info_table.setSortingEnabled(__sortingEnabled)

        self.result_button.setText(QCoreApplication.translate("Window", u"\u0420\u0430\u0441\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.current_level_label.setText(QCoreApplication.translate("Window", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c:", None))
        self.current_level_value_label.setText(QCoreApplication.translate("Window", u"0", None))
        self.target_level_label.setText(QCoreApplication.translate("Window", u"\u0426\u0435\u043b\u0435\u0432\u043e\u0439 \u0443\u0440\u043e\u0432\u0435\u043d\u044c:", None))
        self.target_level_value_label.setText(QCoreApplication.translate("Window", u"0", None))
        self.current_level_exp_label.setText(QCoreApplication.translate("Window", u"\u0422\u0435\u043a\u0443\u0449\u0438\u0439 \u043e\u043f\u044b\u0442 \u0443\u0440\u043e\u0432\u043d\u044f:", None))
        self.current_level_exp_value_label.setText(QCoreApplication.translate("Window", u"0", None))
        self.target_level_exp_label.setText(QCoreApplication.translate("Window", u"\u041d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u043e \u043e\u043f\u044b\u0442\u0430:", None))
        self.target_level_exp_value_label.setText(QCoreApplication.translate("Window", u"0", None))
        ___qtablewidgetitem28 = self.result_table.horizontalHeaderItem(0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("Window", u"\u041b\u043e\u043a\u0430\u0446\u0438\u044f", None));
        ___qtablewidgetitem29 = self.result_table.horizontalHeaderItem(1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("Window", u"\u0418\u0433\u0440", None));
        ___qtablewidgetitem30 = self.result_table.horizontalHeaderItem(2)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("Window", u"\u0418\u0433\u0440 \u0441 VIP", None));
        ___qtablewidgetitem31 = self.result_table.horizontalHeaderItem(3)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("Window", u"\u041e\u0440\u0435\u0445\u0438", None));
        ___qtablewidgetitem32 = self.result_table.horizontalHeaderItem(4)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("Window", u"\u041e\u0440\u0435\u0445\u0438 \u0441 VIP", None));

        __sortingEnabled1 = self.result_table.isSortingEnabled()
        self.result_table.setSortingEnabled(False)
        ___qtablewidgetitem33 = self.result_table.item(0, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("Window", u"\u0421\u043e\u043b\u043d\u0435\u0447\u043d\u044b\u0435 \u0434\u043e\u043b\u0438\u043d\u044b", None));
        ___qtablewidgetitem34 = self.result_table.item(0, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem35 = self.result_table.item(0, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem36 = self.result_table.item(0, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem37 = self.result_table.item(0, 4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem38 = self.result_table.item(1, 0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("Window", u"\u0422\u043e\u043f\u0438", None));
        ___qtablewidgetitem39 = self.result_table.item(1, 1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem40 = self.result_table.item(1, 2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem41 = self.result_table.item(1, 3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem42 = self.result_table.item(1, 4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem43 = self.result_table.item(2, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("Window", u"\u0428\u0442\u043e\u0440\u043c", None));
        ___qtablewidgetitem44 = self.result_table.item(2, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem45 = self.result_table.item(2, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem46 = self.result_table.item(2, 3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem47 = self.result_table.item(2, 4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem48 = self.result_table.item(3, 0)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("Window", u"\u0418\u0441\u043f\u044b\u0442\u0430\u043d\u0438\u044f", None));
        ___qtablewidgetitem49 = self.result_table.item(3, 1)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem50 = self.result_table.item(3, 2)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem51 = self.result_table.item(3, 3)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem52 = self.result_table.item(3, 4)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem53 = self.result_table.item(4, 0)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("Window", u"\u041f\u0443\u0441\u0442\u044b\u043d\u044f", None));
        ___qtablewidgetitem54 = self.result_table.item(4, 1)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem55 = self.result_table.item(4, 2)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem56 = self.result_table.item(4, 3)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem57 = self.result_table.item(4, 4)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem58 = self.result_table.item(5, 0)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("Window", u"\u0410\u043d\u043e\u043c\u0430\u043b\u044c\u043d\u0430\u044f \u0437\u043e\u043d\u0430", None));
        ___qtablewidgetitem59 = self.result_table.item(5, 1)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem60 = self.result_table.item(5, 2)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem61 = self.result_table.item(5, 3)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("Window", u"0", None));
        ___qtablewidgetitem62 = self.result_table.item(5, 4)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("Window", u"0", None));
        self.result_table.setSortingEnabled(__sortingEnabled1)

        self.label.setText(QCoreApplication.translate("Window", u"Eixini (Roman R\u00e4ximov)   --- ID: 3349442 --- ver. 1.0.0 (16.05.2024)", None))
    # retranslateUi

