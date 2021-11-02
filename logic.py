from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtGui import QIcon
from PyQt6 import uic 
from SORTS.tri_a_bulles import tri_a_bulles
import random
class SortingUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI/gui.ui',self)
        self.setWindowTitle("Sorting Teacher")
        self.setFixedHeight(600)
        self.setFixedWidth(830)
        self.savedTest=False
        self.insertion_found=False
        self.savedArray=[]
        self.counter=0
        self.j=0
        self.pushButton_CLEAR.clicked.connect(self.sort_clear)
        self.pushButton_RESET.clicked.connect(self.reset)
        self.pushButton_SORT.clicked.connect(self.sort_tri_insertion)
    
    def clear_color(self):
        array=self.get_array()
        for i,j  in enumerate(array):
           array[i].setStyleSheet('background-color:white;')

    def permute(self,first,scnd):
        aux=first.text()
        first.setText(scnd.text())
        scnd.setText(aux)
    
    def change(self,x,y,name):
        array=self.get_array()
        
        if name=="bulles":
            first=array[x]
            scnd=array[x+1]
            first.setStyleSheet('background-color:yellow;')
            scnd.setStyleSheet('background-color:green;')
            self.permute(first,scnd)

        if name == "insertion" :
            first=array[x]
            scnd=array[y]
            first.setStyleSheet('background-color:yellow;')
            scnd.setStyleSheet('background-color:green;')
            self.permute(first,scnd)
        
        if name == "valid":
            array[x].setStyleSheet('background-color:red;')
            
    def get_array(self):
        if self.savedTest == False:
            self.savedArray=[self.arr1.text(),self.arr2.text(),self.arr3.text(),self.arr4.text(),self.arr5.text(),self.arr6.text(),self.arr7.text(),self.arr8.text(),self.arr9.text(),self.arr10.text()]
            self.savedTest = True

        array=[self.arr1,self.arr2,self.arr3,self.arr4,self.arr5,self.arr6,self.arr7,self.arr8,self.arr9,self.arr10]
        return array        
            
    def sort_tri_a_bulles(self):   
        self.clear_color()
        array=self.get_array()
        for i,j  in enumerate(array):
            array[i]=int(j.text())
            
        print(self.counter)
        if self.counter < len(array)-1:
            if array[self.counter] > array[self.counter+1] and array[self.counter] != array[self.counter+1]:
                array[self.counter] , array[self.counter+1] = array[self.counter+1] , array[self.counter]
                self.change(self.counter,0,"bulles")
            else:
                self.change(self.counter,0,"valid")
            
            print(array)
            
            self.counter += 1
        else:
            self.counter = 0
    
    def sort_tri_insertion(self):
        self.clear_color()
        array=self.get_array()
        for i,j  in enumerate(array):
            array[i]=int(j.text())
        
        if self.insertion_found == False:
            print("j = counter")
            self.counter += 1
            self.j=self.counter            

        if self.counter < len(array):
            
            print(f"{array[self.j-1]} > {array[self.j]} = {array[self.j-1]>array[self.j]}")
            
            if (array[self.j-1] > array[self.j]) and (self.j>0):
                aux=array[self.j]
                array[self.j]=array[self.j-1]
                array[self.j-1]=aux
                self.change(self.j-1,self.j,"insertion")
                if self.j > 1 :
                    self.j -= 1
                    self.insertion_found = True
            else:
                self.change(self.j,0,"valid")
                self.insertion_found = False
                
            print(array)
        else:
            self.counter = 0
        
    def reset(self):
        self.clear_color()
        self.counter = 0
        savedArray=self.savedArray
        print(savedArray)
        array=self.get_array()
        for i,j in enumerate(array):
            j.setText(savedArray[i])    
    
    def sort_clear(self):
        self.clear_color()
        array=self.get_array()
        for i,j in enumerate(array):
            j.setText("0")
        self.savedTest=False