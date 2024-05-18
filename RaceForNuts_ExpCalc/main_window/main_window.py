from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap
from RaceForNuts_ExpCalc.main_window.ui_gen.ui_main_window import Ui_MainWindow
from RaceForNuts_ExpCalc.experience_window.experience_window import ExperienceWindow
from RaceForNuts_ExpCalc.shaman_experience_window.shaman_experience_window import ShamanExperienceWindow
from RaceForNuts_ExpCalc.resources import icons_rc


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowIcon(QPixmap(':/icons/race_for_nuts_experience.png'))

        self.ui.tab_widget.addTab(ExperienceWindow(), "Расчет опыта")
        self.ui.tab_widget.addTab(ShamanExperienceWindow(), "Расчет опыта шамана")
