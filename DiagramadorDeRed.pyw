from sys import argv

from PySide2.QtCore import Qt
from PySide2.QtGui import QIcon, QGuiApplication
from PySide2.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QWidget, QTabWidget, QAction, QStyle

from modules.InformacionIP import InformacionIP
from modules.CalcularSubred import CalcularSubred
from modules.ConversionNumeros import ConversionNumeros
from modules.CalcularVLSM import CalcularVLSM
from utilities.Style import style


class NetworkAssistant(QMainWindow):
    def __init__(self):
        super(NetworkAssistant, self).__init__()

        # The size of the starting window
        self.resize(965, 600)

        # Set window center of screen
        self.setGeometry(
            QStyle.alignedRect(
                Qt.LeftToRight,
                Qt.AlignCenter,
                self.size(),
                QGuiApplication.primaryScreen().availableGeometry(),
            ),
        )

        # The version of the program
        self.version = "v1.0"

        # The title of the program
        self.setWindowTitle(f"{'Diagramador de Red'} {self.version}")

        # The icon of the program
        self.setWindowIcon(QIcon("static/images/main_icon.png"))

        # Before using the main layout, need to create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.ip_information = InformacionIP()
        self.number_conversion = ConversionNumeros()
        self.ip_subnet_calculation = CalcularSubred()
        self.vlsm_calculation = CalcularVLSM()

        self.tabwidget = QTabWidget()
        self.tabwidget.addTab(self.ip_information, "Información de la IP")
        self.tabwidget.addTab(self.number_conversion, "Conversión de número")
        self.tabwidget.addTab(self.ip_subnet_calculation, "Calcular subred")
        self.tabwidget.addTab(self.vlsm_calculation, "Calcular VLSM")
        main_layout.addWidget(self.tabwidget)

        # Set stylesheet
        self.setStyleSheet(style())

        self.setWindowTitle(f"{'Diagramador de Red'} {self.version}")
        self.tabwidget.setTabText(0, "Información de la IP")
        self.tabwidget.setTabText(1, "Conversión de número")
        self.tabwidget.setTabText(2, "Calcular subred")
        self.tabwidget.setTabText(3, "Calcular VLSM")


if __name__ == '__main__':
    app = QApplication(argv)
    win = NetworkAssistant()
    win.show()
    app.exec_()
