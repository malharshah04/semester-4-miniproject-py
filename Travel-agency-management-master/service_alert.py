# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'service_alert.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_service_alert(object):
    def setupUi(self, service_alert):
        service_alert.setObjectName("service_alert")
        service_alert.resize(755, 792)
        service_alert.setMinimumSize(QtCore.QSize(755, 792))
        service_alert.setMaximumSize(QtCore.QSize(755, 792))
        self.label = QtWidgets.QLabel(service_alert)
        self.label.setGeometry(QtCore.QRect(0, -10, 761, 811))
        self.label.setMinimumSize(QtCore.QSize(761, 811))
        self.label.setMaximumSize(QtCore.QSize(761, 811))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Resources/service_alert.png"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(service_alert)
        self.label_2.setGeometry(QtCore.QRect(210, 40, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Rockwell Condensed")
        font.setPointSize(36)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:1 rgba(255, 0, 0, 255));")
        self.label_2.setObjectName("label_2")
        self.car1 = QtWidgets.QLineEdit(service_alert)
        self.car1.setGeometry(QtCore.QRect(80, 340, 191, 22))
        self.car1.setReadOnly(True)
        self.car1.setObjectName("car1")
        self.car2 = QtWidgets.QLineEdit(service_alert)
        self.car2.setGeometry(QtCore.QRect(430, 340, 191, 22))
        self.car2.setReadOnly(True)
        self.car2.setObjectName("car2")
        self.car3 = QtWidgets.QLineEdit(service_alert)
        self.car3.setGeometry(QtCore.QRect(70, 510, 191, 22))
        self.car3.setReadOnly(True)
        self.car3.setObjectName("car3")
        self.car4 = QtWidgets.QLineEdit(service_alert)
        self.car4.setGeometry(QtCore.QRect(430, 510, 191, 22))
        self.car4.setReadOnly(True)
        self.car4.setObjectName("car4")
        self.car5 = QtWidgets.QLineEdit(service_alert)
        self.car5.setGeometry(QtCore.QRect(70, 680, 201, 22))
        self.car5.setReadOnly(True)
        self.car5.setObjectName("car5")
        self.car6 = QtWidgets.QLineEdit(service_alert)
        self.car6.setGeometry(QtCore.QRect(430, 670, 201, 22))
        self.car6.setReadOnly(True)
        self.car6.setObjectName("car6")

        self.retranslateUi(service_alert)
        QtCore.QMetaObject.connectSlotsByName(service_alert)


        from datetime import date
        import json

        filename = 'Resources/DataFiles/service.json'
        with open(filename,'r') as f:
            data=json.load(f)
            today=str(date.today())
            if data["1"]==today:
                self.car1.setText("Need Service")
                self.car1.setStyleSheet("color: rgb(255, 0, 0);")
            if data["2"]==today:
                self.car2.setText("Need Service")
                self.car2.setStyleSheet("color: rgb(255, 0, 0);")
            if data["3"]==today:
                self.car3.setText("Need Service")
                self.car3.setStyleSheet("color: rgb(255, 0, 0);")
            if data["4"]==today:
                self.car4.setText("Need Service")
                self.car4.setStyleSheet("color: rgb(255, 0, 0);")
            if data["5"]==today:
                self.car5.setText("Need Service")
                self.car5.setStyleSheet("color: rgb(255, 0, 0);")
            if data["6"]==today:
                self.car6.setText("Need Service")
                self.car6.setStyleSheet("color: rgb(255, 0, 0);")
                
            if data["1"]!=today:
                self.car1.setText("Serviced")
                self.car1.setStyleSheet("color: rgb(0, 255, 0);")
            if data["2"]!=today:
                self.car2.setText("Serviced")
                self.car2.setStyleSheet("color: rgb(0, 255, 0);")
            if data["3"]!=today:
                self.car3.setText("Serviced")
                self.car3.setStyleSheet("color: rgb(0, 255, 0);")
            if data["4"]!=today:
                self.car4.setText("Serviced")
                self.car4.setStyleSheet("color: rgb(0, 255, 0);")
            if data["5"]!=today:
                self.car5.setText("Serviced")
                self.car5.setStyleSheet("color: rgb(0, 255, 0);")
            if data["6"]!=today:
                self.car6.setText("Serviced")
                self.car6.setStyleSheet("color: rgb(0, 255, 0);")

                   
        f.close()


    def retranslateUi(self, service_alert):
        _translate = QtCore.QCoreApplication.translate
        service_alert.setWindowTitle(_translate("service_alert", "Dialog"))
        self.label_2.setText(_translate("service_alert", "Service Alert"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    service_alert = QtWidgets.QDialog()
    ui = Ui_service_alert()
    ui.setupUi(service_alert)
    service_alert.show()
    sys.exit(app.exec_())
