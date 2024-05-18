from PySide6.QtWidgets import QWidget, QHeaderView, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile, QJsonDocument, QIODevice
from RaceForNuts_ExpCalc.shaman_experience_window.ui_gen.ui_shaman_experience_window import Ui_ShamanExperienceWindow
from RaceForNuts_ExpCalc.resources import data_rc
import json
import math

class ShamanExperienceWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_ShamanExperienceWindow()
        self.ui.setupUi(self)

        self.current_exp = 0
        self.current_total_exp = 0
        self.experience_required = 0
        self.current_level = 0
        self.target_level = 0

        self._data = list()
        self.data_initialization()

        self.ui.exp_info_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.ui.exp_info_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

        self.ui.result_table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.ui.result_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)

        self.ui.result_button.clicked.connect(self.calculation)
        self.ui.experience_spinbox.valueChanged.connect(self.experience_change)

    def data_initialization(self):
        file = QFile(':/data/race_for_nuts_experience.json')
        file.open(QIODevice.OpenModeFlag.ReadOnly)
        byte_array = file.readAll()
        file.close()

        json_dict = json.loads(byte_array.data())

        for el in json_dict.get('shaman_levels'):
            self._data.append(el)

    def experience_change(self):
        if self.ui.experience_spinbox.value() == 0:
            self.current_exp = 0

    def calculation(self):
        if (self.ui.current_level_spinbox.value() > self.ui.target_level_spinbox.value()
                or self.ui.current_level_spinbox.value() == self.ui.target_level_spinbox.value()):
            msg_box = QMessageBox()
            msg_box.setText('Текущий уровень не может быть выше или равен целевому.')
            msg_box.setWindowTitle('Ошибка')
            msg_box.exec()
        else:
            current_data = dict()
            target_data = dict()

            for dat in self._data:
                if dat.get('level') == self.ui.current_level_spinbox.value():
                    current_data = dat
                if dat.get('level') == self.ui.target_level_spinbox.value():
                    target_data = dat

            if not self.ui.experience_spinbox.value() == 0:
                # Опыт, который был получен на текущем уровне (опыт до следующего уровня - остаток опыта до следующего уровня)
                self.current_exp = current_data.get('shaman_experience_to_next_level') - self.ui.experience_spinbox.value()
            else:
                self.current_exp = 0

            # Получение суммарного опыта путем сложения общего опыта и накопленного опыта на текущем уровне
            self.current_total_exp = current_data.get('total_shaman_experience') + self.current_exp

            self.experience_required = target_data.get('total_shaman_experience') - self.current_total_exp

            self.current_level = current_data.get('level')
            self.target_level = target_data.get('level')

            self.result_form(self.current_level, self.current_exp, self.target_level, self.experience_required)

    def result_form(self, cur_lvl, cur_exp, lvl_req, exp_req):

        self.ui.current_level_value_label.setText(f'{cur_lvl}')
        self.ui.current_level_exp_value_label.setText(f'{cur_exp}')

        self.ui.target_level_value_label.setText(f'{lvl_req}')
        self.ui.target_level_exp_value_label.setText(f'{exp_req}')

        # Солнечные долины
        self.ui.result_table.setItem(0, 1, QTableWidgetItem(f'{math.ceil(exp_req / 4)}'))
        self.ui.result_table.setItem(0, 2, QTableWidgetItem(f'{math.ceil(exp_req / 8)}'))

        # Топи
        self.ui.result_table.setItem(1, 1, QTableWidgetItem(f'{math.ceil(exp_req / 7)}'))
        self.ui.result_table.setItem(1, 2, QTableWidgetItem(f'{math.ceil(exp_req / 14)}'))

        # Шторм
        self.ui.result_table.setItem(2, 1, QTableWidgetItem(f'{math.ceil(exp_req / 19)}'))
        self.ui.result_table.setItem(2, 2, QTableWidgetItem(f'{math.ceil(exp_req / 38)}'))

        # Испытания
        self.ui.result_table.setItem(3, 1, QTableWidgetItem(f'{math.ceil(exp_req / 13)}'))
        self.ui.result_table.setItem(3, 2, QTableWidgetItem(f'{math.ceil(exp_req / 26)}'))

        # Пустыня
        self.ui.result_table.setItem(4, 1, QTableWidgetItem(f'{math.ceil(exp_req / 17)}'))
        self.ui.result_table.setItem(4, 2, QTableWidgetItem(f'{math.ceil(exp_req / 34)}'))

        # Аномальная зона
        self.ui.result_table.setItem(5, 1, QTableWidgetItem(f'{math.ceil(exp_req / 21)}'))
        self.ui.result_table.setItem(5, 2, QTableWidgetItem(f'{math.ceil(exp_req / 42)}'))
