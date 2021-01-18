# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:13:50 2020

@author: artur
"""


import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPixmap, QPainter, QColor, QFont
from PIL import Image
import numpy as np
from collections import Counter


class ImageLabel(QLabel):
    def __init__(self):
        super().__init__()
 
        self.setAlignment(Qt.AlignCenter)
        self.setText('\n\n Drop Image Here \n\n')
        self.setStyleSheet('''
            QLabel{
                border: 4px dashed #aaa
            }
        ''')
 
    def setPixmap(self, image):
        super().setPixmap(image)
 
class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Vajalik data")
        mainLayout = QVBoxLayout()
        
        self.input1=QLineEdit()
        self.input2=QLineEdit()
        mainLayout.addWidget(self.input1)
        mainLayout.addWidget(self.input2)

        
        self.closeButton = QPushButton("Close")
        self.closeButton.clicked.connect(self.close)
        
        mainLayout.addWidget(self.closeButton)
        
        self.setLayout(mainLayout)
        
    def displayInfo(self):
        self.show()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Image")
        self.resize(400, 400)
        self.setAcceptDrops(True)
        
        self.secondWindow=SecondWindow()
        
        mainLayout = QVBoxLayout()
 
        self.photoViewer = ImageLabel()
        mainLayout.addWidget(self.photoViewer)
        
        self.Confirm= QPushButton("Confirm")
        self.Confirm.setStyleSheet('font-size: 15px')
        self.Confirm.clicked.connect(self.passingInformation)
        mainLayout.addWidget(self.Confirm)
        self.setLayout(mainLayout)
        
    def dragEnterEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
 
    def dragMoveEvent(self, event):
        if event.mimeData().hasImage:
            event.accept()
        else:
            event.ignore()
 
    def dropEvent(self, event):
        
        if event.mimeData().hasImage:
            event.setDropAction(Qt.CopyAction)
            file_path = event.mimeData().urls()[0].toLocalFile()
            self.set_image(file_path)
            event.accept()            
            #for i in nimekiri:
               # print(str(i[0])+" protsent on: " + str (round(100*(int(i[1]))/(suurus1)))+"%")
        
        else:
            event.ignore()   

    def passingInformation(self):
        pilt=Image.open(file_path)
        data = list(pilt.getdata()) #saan numpy array data. Ehk list mis koosneb pikslite tupletest.
        #pikkus= len(data)
        suurus=width,height=pilt.size
        suurus1=width*height
        loendus=dict(Counter(data))
        nimekiri = [[k, v] for k, v in loendus.items()]
        
        self.secondWindow.input1.setText(self.str((nimekiri[0])).text())
        self.secondWindow.input2.setText(self.str((nimekiri[1])).text())
        self.secondWindow.displayInfo()
    def set_image(self, file_path):
        self.photoViewer.setPixmap(QPixmap(file_path))
app = QApplication(sys.argv)
demo = MainWindow()
demo.show()
sys.exit(app.exec_())



