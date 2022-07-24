# -*- coding: utf-8 -*-
"""
Created on Sun May  1 16:44:09 2022

@author: Ritwiz
"""

usertext = 'a'

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
import sys
from nltk.corpus import stopwords

with open('output/segmented_docs.txt') as f:
    all_docs = f.readlines()

all_docs[0] = all_docs[0].replace("]","")
all_docs[0] = all_docs[0].replace("[","")
all_docs[0] = all_docs[0].replace("(","")
all_docs[0] = all_docs[0].replace(")","")
all_docs[0] = all_docs[0].replace(".","")
all_docs[0] = all_docs[0].replace("/","")
all_docs[0] = all_docs[0].replace(",","")
all_docs[0] = all_docs[0].replace("-"," ")
all_docs[0] = all_docs[0].replace("?","")
all_docs[0] = all_docs[0].replace("=","")
all_docs[0] = all_docs[0].replace("<","")
all_docs[0] = all_docs[0].replace(">","")
all_docs[0] = all_docs[0].replace('"',"")
all_docs[0] = all_docs[0].replace("'","")

all_docs[0]=' '.join(dict.fromkeys(all_docs[0].split()))

from nltk import ngrams
u,b,t=1,2,3
uni = ngrams(all_docs[0].split(), u)
unigrams = []
for grams in uni:
  unigrams.append(grams)
gram1 = [' '.join(i) for i in unigrams]
bi = ngrams(all_docs[0].split(), b)
bigrams = []
for grams in bi:
  bigrams.append(grams)
gram2 = [' '.join(i) for i in bigrams]
tri = ngrams(all_docs[0].split(), t)
trigrams = []
for grams in tri:
  trigrams.append(grams)
gram3 = [' '.join(i) for i in trigrams]

all_grams = gram1 + gram2 + gram3

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)
        self.setMinimumSize(QSize(480, 480))
        self.setWindowTitle("Welcome to AutoComplete!")

        # auto complete options                                                 
        names = all_grams
        completer = QCompleter(names)

        # create line edit and add auto complete                                
        self.lineedit = QLineEdit()
        self.lineedit.setCompleter(completer)
        layout.addWidget(self.lineedit, 0, 0)


def myfunc(a):
    global usertext
    usertext = a
    with open('userquery.txt','w') as f:
        f.write(usertext)    

app = QApplication(sys.argv)
screen = Window()
val = screen.lineedit.textChanged.connect(myfunc)
main_text = QtWidgets.QLabel(screen)
main_text.setText("Welcome to AutoComplete Helper for Cranfield dataset \nEnter query below:")
main_text.move(100,100)
main_text.adjustSize()
screen.show()
sys.exit(app.exec_())
