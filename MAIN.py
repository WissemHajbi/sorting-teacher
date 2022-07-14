import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6 import uic 
from SORTS.tri_a_bulles import tri_a_bulles
from logic import SortingUI
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sorting_method = input("what sorting method you like to use ? : ")
    while sorting_method != "insertion" and sorting_method != "bulles" and sorting_method != "selection":
        print("insertion / bulles / selection")
        sorting_method = input("what sorting method you like to use ? : ")
    SortingTeacher = SortingUI(sorting_method) 
    SortingTeacher.show()
    try:
        sys.exit(app.exec())
    except SystemExit:
        print('closing sorting teacher')