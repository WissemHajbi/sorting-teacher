from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic
from SORTS.tri_a_bulles import tri_a_bulles
import random


class SortingUI(QMainWindow):
    def __init__(self, sorting_method):
        super().__init__()
        uic.loadUi('UI/gui.ui', self)
        self.setWindowTitle("Sorting Teacher")
        self.setFixedHeight(600)
        self.setFixedWidth(830)
        self.savedTest = False
        self.insertion_found = False
        self.savedArray = []
        self.counter = 0
        self.action = False
        self.j = 0
        self.pushButton_CLEAR.clicked.connect(self.sort_clear)
        self.pushButton_RESET.clicked.connect(self.reset)
        self.pushButton_RANDOM.clicked.connect(self.random)
        self.sorting_method = sorting_method
        if sorting_method == "insertion":
            self.pushButton_SORT.clicked.connect(self.sort_tri_insertion)
            self.counter = 1
        elif sorting_method == "bulles":
            self.pushButton_SORT.clicked.connect(self.sort_tri_a_bulles)
        elif sorting_method == "selection":
            self.pushButton_SORT.clicked.connect(self.sort_tri_selection)

    def random(self):
        self.sort_clear()
        random_array = [
            random.randint(0, 100) for i in range(10)
        ]
        array = self.get_array()
        for i in range(len(random_array)):
            array[i].setText(str(random_array[i]))
        self.savedArray = [
            str(i) for i in random_array
        ]

    def clear_color(self):
        array = self.get_array()
        for i, j in enumerate(array):
            array[i].setStyleSheet('background-color:white;')

    def permute(self, first, scnd):
        aux = first.text()
        first.setText(scnd.text())
        scnd.setText(aux)

    def change(self, x, y, name, action=""):
        array = self.get_array()

        if name == "bulles":
            array[x].setStyleSheet('background-color:yellow;')
            array[x+1].setStyleSheet('background-color:green;')
            self.permute(array[x], array[x+1])

        if name == "insertion":
            array[x].setStyleSheet('background-color:yellow;')
            array[y].setStyleSheet('background-color:green;')
            if action == "move":
                self.permute(array[x], array[y])

        if name == "selection":
            array[x].setStyleSheet('background-color:yellow;')
            array[y].setStyleSheet('background-color:green;')
            if action == "move":
                self.permute(array[x], array[y])

        if name == "valid":
            array[x].setStyleSheet('background-color:red;')

    def get_array(self):
        if self.savedTest == False:
            self.savedArray = [self.arr1.text(), self.arr2.text(), self.arr3.text(), self.arr4.text(), self.arr5.text(
            ), self.arr6.text(), self.arr7.text(), self.arr8.text(), self.arr9.text(), self.arr10.text()]
            self.savedTest = True

        array = [self.arr1, self.arr2, self.arr3, self.arr4, self.arr5,
                 self.arr6, self.arr7, self.arr8, self.arr9, self.arr10]
        return array

    # tri a bulles
    def sort_tri_a_bulles(self):
        self.clear_color()
        array = self.get_array()
        self.casting_array_to_int(array)

        if self.counter < len(array)-1:
            if array[self.counter] > array[self.counter+1] and array[self.counter] != array[self.counter+1]:
                if self.action:
                    self.change(self.counter, 0, "bulles", "move")
                    self.action = False
                else:
                    self.change(self.counter, 0, "bulles")
                    self.action = True
                    return
            else:
                self.change(self.counter, 0, "valid")
            self.counter += 1
        else:
            self.counter = 0

    # tri par insertion
    def sort_tri_insertion(self):
        self.clear_color()
        array = self.get_array()
        self.casting_array_to_int(array)

        if self.insertion_found == False and self.action == False:
            self.j = self.counter

        if self.counter < len(array):
            if (array[self.j-1] > array[self.j]) and (self.j > 0):
                if self.action:
                    self.change(self.j, self.j-1, "insertion", "move")
                    self.action = False
                else:
                    self.change(self.j, self.j-1, "insertion")
                    self.action = True
                    return
                if self.j > 1:
                    self.j -= 1
                    self.insertion_found = True
            else:
                self.change(self.j, 0, "valid")
                self.insertion_found = False
                self.counter += 1
        else:
            self.counter = 0

    # tri par selection
    def sort_tri_selection(self):
        self.clear_color()
        array = self.get_array()

        self.casting_array_to_int(array)

        if self.counter < len(array)-1:
            min_number = array.index(
                min(array[self.counter+1:])) + self.counter+1
            if (array[self.counter] > array[min_number]):
                if self.action:
                    self.change(self.counter, min_number, "selection", "move")
                    self.action = False
                else:
                    self.change(self.counter, min_number, "selection")
                    self.action = True
                    return
            else:
                self.change(self.counter, 0, "valid")
            self.counter += 1
        else:
            self.counter = 0

    def reset(self):
        self.clear_color()
        if self.sorting_method == "insertion":
            self.counter = 1
        else:
            self.counter = 0
        self.action = False
        savedArray = self.savedArray
        array = self.get_array()
        for i, j in enumerate(array):
            j.setText(savedArray[i])

    def sort_clear(self):
        self.clear_color()
        array = self.get_array()
        for i, j in enumerate(array):
            j.setText("0")
        self.savedTest = False

    def casting_array_to_int(self, array):
        for i, j in enumerate(array):
            array[i] = int(j.text())
