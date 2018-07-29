import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QVBoxLayout, QHBoxLayout, QPushButton,
                             QLineEdit, QLabel)
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

        params = ['Px', r'Dx', r'Pfi', r'Dfi']
        self.LE_paramLimits = []
        for i in range(4):
            hBox = QHBoxLayout()
            hBox.addWidget(QLabel(params[i]))
            self.LE_paramLimits.append(QLineEdit())
            self.LE_paramLimits[i].setPlaceholderText('min:max')
            hBox.addWidget(self.LE_paramLimits[i])
            vBoxMain.addLayout(hBox)



        self.B_initPop = QPushButton('Generate 0th population')
        self.B_initPop.clicked.connect(self.S_initPop)
        vBoxMain.addWidget(self.B_initPop)

        self.setLayout(vBoxMain)

    @pyqtSlot()
    def S_initPop(self):
        limits_B =  []
        for b in self.LE_paramLimits:
            try:
                limits_B.append( [float(x) for x in b.text().split(':')] )
            except:
                limits_B.append([None, None])

        print(limits_B)





if __name__ == '__main__':
    app = QApplication(sys.argv)

    mW = populationWidget()
    mW.show()

    sys.exit(app.exec_())