from population import populationHandler
import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class mainWindow(QMainWindow):
    def __init__(self):
        """ This is the main window and enterpoint of the program.
            It will show us diagrams of the results and provide an interface
            to handle the populations.
        """
        QMainWindow.__init__(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    mW = mainWindow()
    mW.show()

    sys.exit(app.exec_())