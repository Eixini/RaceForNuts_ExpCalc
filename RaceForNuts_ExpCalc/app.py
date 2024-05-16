import sys
from PySide6.QtWidgets import QApplication
from RaceForNuts_ExpCalc.window.race_for_nuts_experience import Window


def main():
    app = QApplication(sys.argv)
    app.setApplicationName('RaceForNuts_ExpCalc')
    app.setOrganizationName('Eixini Software')

    window = Window()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()
