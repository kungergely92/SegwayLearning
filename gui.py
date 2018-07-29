import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QPushButton,
                             QLineEdit)
from PyQt5.QtCore import (pyqtSlot)


class populationWidget(QWidget):
    def __init__(self):
        """ This is the main window and enter point of the program.
            It will show us diagrams of the results and provide an interface
            to handle the populations.
        """
        QWidget.__init__(self)

        self.buildGUI()

    def buildGUI(self):
        vBoxMain = QVBoxLayout()

        self.LE_paramLimits = []
        for i in range(4):
            self.LE_paramLimits.append(QLineEdit())
            self.LE_paramLimits[i].setPlaceholderText('min-max')
            vBoxMain.addWidget(self.LE_paramLimits[i])



        self.B_initPop = QPushButton('Generate 0th population')
        self.B_initPop.clicked.connect(self.S_initPop)
        vBoxMain.addWidget(self.B_initPop)

        self.setLayout(vBoxMain)

    @pyqtSlot()
    def S_initPop(self):
        limits_B =  []
        for b in self.LE_paramLimits:
            try:
                limits_B.append( [float(x) for x in b.text().split('-')] )
            except:
                pass

        print(limits_B)





if __name__ == '__main__':
    app = QApplication(sys.argv)

    mW = populationWidget()
    mW.show()

    sys.exit(app.exec_())