from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6 import uic 
from SORTS.tri_a_bulles import tri_a_bulles
class SortingUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/gui.ui',self)
        self.setWindowTitle("Sorting Teacher")
        self.setFixedHeight(600)
        self.setFixedWidth(830)
        self.pushButton_SORT.clicked.connect(self.sort_tri_a_bulles)

    def clear(self):
        array=self.get()
        for i,j  in enumerate(array):
           j.setStyleSheet('background-color:white;')

    def permute(self,first,scnd):
        aux=first.text()
        first.setText(scnd.text())
        scnd.setText(aux)
    
    def change(self,x):
        if x == 0:
            first=self.arr1
            scnd=self.arr2
        elif x == 1:
            first=self.arr2
            scnd=self.arr3
        elif x == 2:
            first=self.arr3
            scnd=self.arr4
        elif x == 3:
            first=self.arr4
            scnd=self.arr5
        elif x == 4:
            first=self.arr5
            scnd=self.arr6
        elif x == 5:
            first=self.arr6
            scnd=self.arr7
        elif x == 6:
            first=self.arr7
            scnd=self.arr8
        elif x == 7:
            first=self.arr8
            scnd=self.arr9
        elif x == 8:
            first=self.arr9
            scnd=self.arr10
        self.permute(first,scnd)
        first.setStyleSheet('background-color:#03DAC5;')
        scnd.setStyleSheet('background-color:#03DAC5;')
 
    def sort_tri_a_bulles(self):   
        self.clear()
        array=self.get()
        for i,j  in enumerate(array):
            array[i]=int(j.text())
            
        for i in range(len(array)-1):
            if array[i] > array[i+1] and array[i] != array[i+1]:
                array[i] , array[i+1] = array[i+1] , array[i]
                self.change(i)
                break
                    
        print(array)
        
    def get(self):
        array=[self.arr1,self.arr2,self.arr3,self.arr4,self.arr5,self.arr6,self.arr7,self.arr8,self.arr9,self.arr10]
        return array