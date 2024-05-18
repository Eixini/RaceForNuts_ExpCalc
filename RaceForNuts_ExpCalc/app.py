import sys
from PySide6.QtWidgets import QApplication
from RaceForNuts_ExpCalc.main_window.main_window import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('RaceForNuts_ExpCalc')
    app.setOrganizationName('Eixini Software')

    window = MainWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
