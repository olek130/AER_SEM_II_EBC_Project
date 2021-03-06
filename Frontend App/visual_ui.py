# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'visual.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QGridLayout, QFileDialog)
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtGui import QScreen
from PyQt5.QtCore import Qt, QTimer
import json
from collections import deque
StateList = {
1:"B",
2:"SH1",
3:"SH2",
4:"SH3",
5:"ST1",
6:"ST2",
7:"ST3",
8:"C1",
9:"C2",
10:"C3",
11:"C4",
12:"C5",
13:"C6",
14:"C7",
15:"C8",
16:"C9",
17:"C2C1",
18:"C1C2",
19:"C3C2",
20:"C2C3",
21:"C1C4",
22:"C4C1",
23:"C2C5",
24:"C5C2",
25:"C3C6",
26:"C6C3",
27:"C5C4",
28:"C4C5",
29:"C6C5",
30:"C5C6",
31:"BC6",
32:"C6B",
33:"C4C7",
34:"C7C4",
35:"C5C8",
36:"C8C5",
37:"C6C9",
38:"C9C6",
39:"C8C7",
40:"C7C8",
41:"C9C8",
42:"C8C9"
}

colors = ["rgb(0, 0, 204)",
"rgb(0, 102, 0)",
"rgb(102, 0, 0)",
"rgb(0, 255, 255)",
"magenta",
"yellow",
"black",
"white"]

head_colors = [
    "rgb(0, 0, 102)",
    "rgb(0, 204, 0)",
    "rgb(205, 0, 0)",
    "rgb(0, 204, 255)",
    "",
    "",
    "",


]

time = 0


class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.tick)
        self.timer.start()

    def setTimerInterval(self,newInterval):
        self.timer.setInterval(newInterval)


    def readJsonAndDrawRobotPaths(self):
        global time
        with open('symulacja.json') as plik_z_symulacja:
            symulacja = json.load(plik_z_symulacja)

        for step in symulacja['steps']:
            try:
                if step['number'] == time:
                    for robot in step['robots']:
                        print(robot['id'],robot['path'])
                        try: 
                            print(len(robot['path']))
                            if (len(robot['path']) > 0):
                                if(len(robot['path']) > 1):
                                    for path in robot['path']:
                                        # ui.line_PathC3C2.setStyleSheet("background-color: green;")
                                        if( path <= 16 ):
                                            command="self.label_"+StateList[path]+".setStyleSheet(\"background-color: "+colors[robot['id']-1]+";\")"
                                        else:
                                            command="self.line_Path"+StateList[path]+".setStyleSheet(\"background-color: "+colors[robot['id']-1]+";\")"
                                        print("[INFO] Evaluating command " + command)
                                        eval(command)
                                        print("[INFO] Evaluated command " + command + "sucessfully")
                                elif (len(robot['path']) == 1):
                                    path = robot['path']
                                    if( path <= 16 ):
                                        command="self.label_"+StateList[path]+".setStyleSheet(\"background-color: "+colors[robot['id']-1]+";\")"
                                    else:
                                        command="self.line_Path"+StateList[path]+".setStyleSheet(\"background-color: "+colors[robot['id']-1]+";\")"
                                    print("[INFO] Evaluating command " + command)
                                    eval(command)
                                    print("[INFO] Evaluated command " + command + "sucessfully")
                            else:
                                pass
                            command = "self.label_"+robot['location']+".setStyleSheet(\"background-color: "+head_colors[robot['id']-1]+";\")"
                            print("[INFO] Evaluating command " + command)
                            eval(command)
                            print("[INFO] Evaluated command " + command + "sucessfully")
                        except: 
                            print("[ERR] ERR in evaluating robot paths")   
                            input("Press Enter to continue...")
            except:
                print("Skipped step: " + step['number'])
                pass

    def tick(self):
        global time
        print("[INFO] Step: " + str(time))
        self.setupUi(MainWindow)
        try:
            self.readJsonAndDrawRobotPaths()
            print("[INFO] Displayed window for step: " + str(time))
        except:
            pass
        img =  QApplication.primaryScreen().grabWindow(0)
        img.save(str(time)+".png")
        time += 1   



    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line_PathC5C4 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC5C4.setGeometry(QtCore.QRect(240, 360, 161, 20))
        self.line_PathC5C4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC5C4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC5C4.setObjectName("line_PathC5C4")
        self.line_PathC4C5 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC4C5.setGeometry(QtCore.QRect(240, 380, 161, 20))
        self.line_PathC4C5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC4C5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC4C5.setObjectName("line_PathC4C5")
        self.line_PathC6C5 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC6C5.setGeometry(QtCore.QRect(480, 360, 161, 16))
        self.line_PathC6C5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC6C5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC6C5.setObjectName("line_PathC6C5")
        self.line_PathC5C6 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC5C6.setGeometry(QtCore.QRect(480, 380, 161, 16))
        self.line_PathC5C6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC5C6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC5C6.setObjectName("line_PathC5C6")
        self.line_PathC2C5 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC2C5.setGeometry(QtCore.QRect(420, 180, 21, 161))
        self.line_PathC2C5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC2C5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC2C5.setObjectName("line_PathC2C5")
        self.line_PathC5C2 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC5C2.setEnabled(True)
        self.line_PathC5C2.setGeometry(QtCore.QRect(440, 180, 21, 161))
        self.line_PathC5C2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC5C2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC5C2.setObjectName("line_PathC5C2")
        self.line_PathC8C5 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC8C5.setEnabled(True)
        self.line_PathC8C5.setGeometry(QtCore.QRect(440, 420, 21, 161))
        self.line_PathC8C5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC8C5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC8C5.setObjectName("line_PathC8C5")
        self.line_PathC5C8 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC5C8.setGeometry(QtCore.QRect(420, 420, 21, 161))
        self.line_PathC5C8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC5C8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC5C8.setObjectName("line_PathC5C8")
        self.line_PathC3C6 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC3C6.setGeometry(QtCore.QRect(650, 180, 21, 161))
        self.line_PathC3C6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC3C6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC3C6.setObjectName("line_PathC3C6")
        self.line_PathC6C3 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC6C3.setEnabled(True)
        self.line_PathC6C3.setGeometry(QtCore.QRect(670, 180, 21, 161))
        self.line_PathC6C3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC6C3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC6C3.setObjectName("line_PathC6C3")

        self.line_PathC1C4 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC1C4.setGeometry(QtCore.QRect(180, 180, 21, 161))
        self.line_PathC1C4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC1C4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC1C4.setObjectName("line_PathC1C4")
        self.line_PathC4C1 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC4C1.setEnabled(True)
        self.line_PathC4C1.setGeometry(QtCore.QRect(200, 180, 21, 161))
        self.line_PathC4C1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC4C1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC4C1.setObjectName("line_PathC4C1")
        self.line_PathC4C7 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC4C7.setGeometry(QtCore.QRect(180, 420, 21, 161))
        self.line_PathC4C7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC4C7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC4C7.setObjectName("line_PathC4C7")
        self.line_PathC7C4 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC7C4.setEnabled(True)
        self.line_PathC7C4.setGeometry(QtCore.QRect(200, 420, 21, 161))
        self.line_PathC7C4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC7C4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC7C4.setObjectName("line_PathC7C4")
        self.line_PathC6C9 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC6C9.setGeometry(QtCore.QRect(650, 420, 21, 161))
        self.line_PathC6C9.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC6C9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC6C9.setObjectName("line_PathC6C9")
        self.line_PathC9C6 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC9C6.setEnabled(True)
        self.line_PathC9C6.setGeometry(QtCore.QRect(670, 420, 21, 161))
        self.line_PathC9C6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_PathC9C6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC9C6.setObjectName("line_PathC9C6")
        self.line_PathC6B = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC6B.setGeometry(QtCore.QRect(710, 380, 161, 16))
        self.line_PathC6B.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC6B.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC6B.setObjectName("line_PathC6B")
        self.line_PathBC6 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathBC6.setGeometry(QtCore.QRect(710, 360, 161, 16))
        self.line_PathBC6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathBC6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathBC6.setObjectName("line_PathBC6")
        self.label_SH1 = QtWidgets.QLabel(self.centralwidget)
        self.label_SH1.setGeometry(QtCore.QRect(170, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SH1.setFont(font)
        self.label_SH1.setObjectName("label_SH1")
        self.label_SH2 = QtWidgets.QLabel(self.centralwidget)
        self.label_SH2.setGeometry(QtCore.QRect(410, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SH2.setFont(font)
        self.label_SH2.setObjectName("label_SH2")
        self.label_SH3 = QtWidgets.QLabel(self.centralwidget)
        self.label_SH3.setGeometry(QtCore.QRect(640, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_SH3.setFont(font)
        self.label_SH3.setObjectName("label_SH3")
        self.label_ST1 = QtWidgets.QLabel(self.centralwidget)
        self.label_ST1.setGeometry(QtCore.QRect(160, 630, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ST1.setFont(font)
        self.label_ST1.setObjectName("label_ST1")
        self.label_ST2 = QtWidgets.QLabel(self.centralwidget)
        self.label_ST2.setGeometry(QtCore.QRect(400, 630, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ST2.setFont(font)
        self.label_ST2.setObjectName("label_ST2")
        self.label_ST3 = QtWidgets.QLabel(self.centralwidget)
        self.label_ST3.setGeometry(QtCore.QRect(630, 630, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_ST3.setFont(font)
        self.label_ST3.setObjectName("label_ST3")
        self.label_C1 = QtWidgets.QLabel(self.centralwidget)
        self.label_C1.setGeometry(QtCore.QRect(190, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C1.setFont(font)
        self.label_C1.setObjectName("label_C1")
        self.label_C2 = QtWidgets.QLabel(self.centralwidget)
        self.label_C2.setGeometry(QtCore.QRect(430, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C2.setFont(font)
        self.label_C2.setObjectName("label_C2")
        self.label_C3 = QtWidgets.QLabel(self.centralwidget)
        self.label_C3.setGeometry(QtCore.QRect(660, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C3.setFont(font)
        self.label_C3.setObjectName("label_C3")
        self.label_C4 = QtWidgets.QLabel(self.centralwidget)
        self.label_C4.setGeometry(QtCore.QRect(190, 360, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C4.setFont(font)
        self.label_C4.setObjectName("label_C4")
        self.label_C5 = QtWidgets.QLabel(self.centralwidget)
        self.label_C5.setGeometry(QtCore.QRect(430, 360, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C5.setFont(font)
        self.label_C5.setObjectName("label_C5")
        self.label_C6 = QtWidgets.QLabel(self.centralwidget)
        self.label_C6.setGeometry(QtCore.QRect(660, 360, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C6.setFont(font)
        self.label_C6.setObjectName("label_C6")
        self.label_C7 = QtWidgets.QLabel(self.centralwidget)
        self.label_C7.setGeometry(QtCore.QRect(190, 590, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C7.setFont(font)
        self.label_C7.setObjectName("label_C7")
        self.label_C8 = QtWidgets.QLabel(self.centralwidget)
        self.label_C8.setGeometry(QtCore.QRect(430, 590, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C8.setFont(font)
        self.label_C8.setObjectName("label_C8")
        self.label_C9 = QtWidgets.QLabel(self.centralwidget)
        self.label_C9.setGeometry(QtCore.QRect(660, 590, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_C9.setFont(font)
        self.label_C9.setObjectName("label_C9")
        self.label_B = QtWidgets.QLabel(self.centralwidget)
        self.label_B.setGeometry(QtCore.QRect(920, 360, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_B.setFont(font)
        self.label_B.setObjectName("label_B")


        self.line_PathC2C1 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC2C1.setGeometry(QtCore.QRect(240, 140, 161, 20))
        self.line_PathC2C1.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC2C1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC2C1.setObjectName("line_PathC2C1")

        self.line_PathC1C2 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC1C2.setGeometry(QtCore.QRect(240, 160, 161, 20))
        self.line_PathC1C2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC1C2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC1C2.setObjectName("line_PathC1C2")

        self.line_PathC2C3 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC2C3.setGeometry(QtCore.QRect(480, 160, 161, 16))
        self.line_PathC2C3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC2C3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC2C3.setObjectName("line_PathC2C3")


        self.line_PathC3C2 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC3C2.setGeometry(QtCore.QRect(480, 140, 161, 16))
        self.line_PathC3C2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC3C2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC3C2.setObjectName("line_PathC3C2")

        self.line_PathC8C9 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC8C9.setGeometry(QtCore.QRect(480, 610, 161, 16))
        self.line_PathC8C9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC8C9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC8C9.setObjectName("line_PathC8C9")
        self.line_PathC9C8 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC9C8.setGeometry(QtCore.QRect(480, 590, 161, 16))
        self.line_PathC9C8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC9C8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC9C8.setObjectName("line_PathC9C8")
        self.line_PathC7C8 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC7C8.setGeometry(QtCore.QRect(240, 610, 161, 16))
        self.line_PathC7C8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC7C8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC7C8.setObjectName("line_PathC7C8")
        self.line_PathC8C7 = QtWidgets.QFrame(self.centralwidget)
        self.line_PathC8C7.setGeometry(QtCore.QRect(240, 590, 161, 16))
        self.line_PathC8C7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_PathC8C7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_PathC8C7.setObjectName("line_PathC8C7")
        self.label_PathC1C2 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC1C2.setGeometry(QtCore.QRect(290, 180, 61, 16))
        self.label_PathC1C2.setObjectName("label_PathC1C2")
        self.label_PathC2C1 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC2C1.setGeometry(QtCore.QRect(290, 120, 61, 16))
        self.label_PathC2C1.setObjectName("label_PathC2C1")
        self.label_PathC3C2 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC3C2.setGeometry(QtCore.QRect(530, 120, 61, 16))
        self.label_PathC3C2.setObjectName("label_PathC3C2")
        self.label_PathC2C3 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC2C3.setGeometry(QtCore.QRect(530, 180, 61, 16))
        self.label_PathC2C3.setObjectName("label_PathC2C3")
        self.label_PathC6C5 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC6C5.setGeometry(QtCore.QRect(530, 340, 61, 16))
        self.label_PathC6C5.setObjectName("label_PathC6C5")
        self.label_PathC5C6 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC5C6.setGeometry(QtCore.QRect(530, 400, 61, 16))
        self.label_PathC5C6.setObjectName("label_PathC5C6")
        self.label_PathC5C4 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC5C4.setGeometry(QtCore.QRect(290, 340, 61, 16))
        self.label_PathC5C4.setObjectName("label_PathC5C4")
        self.label_PathC4C5 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC4C5.setGeometry(QtCore.QRect(290, 400, 61, 16))
        self.label_PathC4C5.setObjectName("label_PathC4C5")
        self.label_PathC8C7 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC8C7.setGeometry(QtCore.QRect(290, 570, 61, 16))
        self.label_PathC8C7.setObjectName("label_PathC8C7")
        self.label_PathC7C8 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC7C8.setGeometry(QtCore.QRect(290, 630, 61, 16))
        self.label_PathC7C8.setObjectName("label_PathC7C8")
        self.label_PathC9C2 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC9C2.setGeometry(QtCore.QRect(530, 570, 61, 16))
        self.label_PathC9C2.setObjectName("label_PathC9C2")
        self.label_PathC8C9 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC8C9.setGeometry(QtCore.QRect(530, 630, 61, 16))
        self.label_PathC8C9.setObjectName("label_PathC8C9")
        self.label_PathBC6 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathBC6.setGeometry(QtCore.QRect(760, 340, 61, 16))
        self.label_PathBC6.setObjectName("label_PathBC6")
        self.label_PathC6B = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC6B.setGeometry(QtCore.QRect(760, 400, 61, 16))
        self.label_PathC6B.setObjectName("label_PathC6B")
        self.label_PathC6C3 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC6C3.setGeometry(QtCore.QRect(690, 250, 61, 16))
        self.label_PathC6C3.setObjectName("label_PathC6C3")
        self.label_PathC3C6 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC3C6.setGeometry(QtCore.QRect(590, 250, 61, 16))
        self.label_PathC3C6.setObjectName("label_PathC3C6")
        self.label_PathC9C6 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC9C6.setGeometry(QtCore.QRect(690, 490, 61, 16))
        self.label_PathC9C6.setObjectName("label_PathC9C6")
        self.label_PathC6C9 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC6C9.setGeometry(QtCore.QRect(590, 490, 61, 16))
        self.label_PathC6C9.setObjectName("label_PathC6C9")
        self.label_PathC8C5 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC8C5.setGeometry(QtCore.QRect(460, 490, 61, 16))
        self.label_PathC8C5.setObjectName("label_PathC8C5")
        self.label_PathC5C8 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC5C8.setGeometry(QtCore.QRect(360, 490, 61, 16))
        self.label_PathC5C8.setObjectName("label_PathC5C8")
        self.label_PathC7C4 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC7C4.setGeometry(QtCore.QRect(220, 490, 61, 16))
        self.label_PathC7C4.setObjectName("label_PathC7C4")
        self.label_PathC4C7 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC4C7.setGeometry(QtCore.QRect(120, 490, 61, 16))
        self.label_PathC4C7.setObjectName("label_PathC4C7")
        self.label_PathC4C1 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC4C1.setGeometry(QtCore.QRect(220, 250, 61, 16))
        self.label_PathC4C1.setObjectName("label_PathC4C1")
        self.label_PathC1C4 = QtWidgets.QLabel(self.centralwidget)
        self.label_PathC1C4.setGeometry(QtCore.QRect(120, 250, 61, 16))
        self.label_PathC1C4.setObjectName("label_PathC1C4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1040, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_SH1.setText(_translate("MainWindow", "SH 1 "))
        self.label_SH2.setText(_translate("MainWindow", "SH 2"))
        self.label_SH3.setText(_translate("MainWindow", "SH 3 "))
        self.label_ST1.setText(_translate("MainWindow", "ST 1 "))
        self.label_ST2.setText(_translate("MainWindow", "ST 2"))
        self.label_ST3.setText(_translate("MainWindow", "ST 3"))
        self.label_C1.setText(_translate("MainWindow", "C1"))
        self.label_C2.setText(_translate("MainWindow", "C2"))
        self.label_C3.setText(_translate("MainWindow", "C3"))
        self.label_C4.setText(_translate("MainWindow", "C4"))
        self.label_C5.setText(_translate("MainWindow", "C5"))
        self.label_C6.setText(_translate("MainWindow", "C6"))
        self.label_C7.setText(_translate("MainWindow", "C7"))
        self.label_C8.setText(_translate("MainWindow", "C8"))
        self.label_C9.setText(_translate("MainWindow", "C9"))
        self.label_B.setText(_translate("MainWindow", "B"))
        self.label_PathC1C2.setText(_translate("MainWindow", "Path C1C2"))
        self.label_PathC2C1.setText(_translate("MainWindow", "Path C2C1"))
        self.label_PathC3C2.setText(_translate("MainWindow", "Path C3C2"))
        self.label_PathC2C3.setText(_translate("MainWindow", "Path C2C3"))
        self.label_PathC6C5.setText(_translate("MainWindow", "Path C6C5"))
        self.label_PathC5C6.setText(_translate("MainWindow", "Path C5C6"))
        self.label_PathC5C4.setText(_translate("MainWindow", "Path C5C4"))
        self.label_PathC4C5.setText(_translate("MainWindow", "Path C4C5"))
        self.label_PathC8C7.setText(_translate("MainWindow", "Path C8C7"))
        self.label_PathC7C8.setText(_translate("MainWindow", "Path C7C8"))
        self.label_PathC9C2.setText(_translate("MainWindow", "Path C9C8"))
        self.label_PathC8C9.setText(_translate("MainWindow", "Path C8C9"))
        self.label_PathBC6.setText(_translate("MainWindow", "Path BC6"))
        self.label_PathC6B.setText(_translate("MainWindow", "Path C6B"))
        self.label_PathC6C3.setText(_translate("MainWindow", "Path C6C3"))
        self.label_PathC3C6.setText(_translate("MainWindow", "Path C3C6"))
        self.label_PathC9C6.setText(_translate("MainWindow", "Path C9C6"))
        self.label_PathC6C9.setText(_translate("MainWindow", "Path C6C9"))
        self.label_PathC8C5.setText(_translate("MainWindow", "Path C8C5"))
        self.label_PathC5C8.setText(_translate("MainWindow", "Path C5C8"))
        self.label_PathC7C4.setText(_translate("MainWindow", "Path C7C4"))
        self.label_PathC4C7.setText(_translate("MainWindow", "Path C4C7"))
        self.label_PathC4C1.setText(_translate("MainWindow", "Path C4C1"))
        self.label_PathC1C4.setText(_translate("MainWindow", "Path C1C4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.line_PathC3C2.setStyleSheet("background-color: green;")
    MainWindow.showMaximized()
    sys.exit(app.exec_())
