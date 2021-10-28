import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6 import uic 
from SORTS.tri_a_bulles import tri_a_bulles
from logic import SortingUI
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    SortingTeacher = SortingUI()
    SortingTeacher.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing sorting teacher')
        