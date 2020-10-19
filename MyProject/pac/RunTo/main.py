# Python 3.7
# Designed by BillowJ

from PyQt5.Qt import *
from qt.untitled import Ui_Form
from  qt.untitled1 import Ui_subForm_1
from  qt.untitled2 import  Ui_subForm_2
import sys


class Min(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.qsl = QStackedLayout(self.frame_2)

        one = Ui_subForm_1()
        two = Ui_subForm_2()

        self.qsl.addWidget(one)
        self.qsl.addWidget(two)

    def show_panel(self):
        print(self.qsl)
        print("...")
        dic = {
            "pushButton" : 0,
            "pushButton_2" : 1,
        }
        index = dic[self.sender().objectName()]
        self.qsl.setCurrentIndex(index)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    min = Min()
    min.show()
    sys.exit(app.exec_())