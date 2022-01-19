from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5 import uic
import sqlite3


class Widget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.initUI()

    def initUI(self):
        self.tableWidget.setColumnWidth(0, 120)  # pеализация таблицы
        self.tableWidget.setColumnWidth(1, 130)
        self.tableWidget.setColumnWidth(2, 130)
        self.tableWidget.setColumnWidth(3, 130)
        self.tableWidget.setColumnWidth(4, 130)
        self.tableWidget.setColumnWidth(5, 130)
        self.tableWidget.setColumnWidth(6, 130)
        self.tableWidget.setColumnWidth(7, 130)
        self.tableWidget.setHorizontalHeaderLabels(["title", "degree", "sort", 'description', 'price', 'volume'])
        self.loaddata()  # выводит значение таблицы
        self.count = 0
        self.change_menu()
        self.label.setText(' ')
        self.btn_menu.clicked.connect(self.change_menu)
        self.pushButton_2.clicked.connect(self.update_menu)

    def loaddata(self):  # обновляет значения таблицы
        connection = sqlite3.connect('coffee.sqlite')
        cur = connection.cursor()
        sqlstr = 'SELECT * FROM rrr LIMIT 15'

        tablerow = 0
        results = cur.execute(sqlstr)
        self.tableWidget.setRowCount(15)
        for row in results:
            print(row)
            self.tableWidget.setItem(tablerow, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[4])))
            self.tableWidget.setItem(tablerow, 4, QtWidgets.QTableWidgetItem(str(row[5])))
            self.tableWidget.setItem(tablerow, 5, QtWidgets.QTableWidgetItem(str(row[6])))
            tablerow += 1

    def change_menu(self):
        if self.count == 0:
            self.label_3.hide()
            self.k_nazv.hide()
            self.label_4.hide()
            self.label_6.hide()
            self.label_5.hide()
            self.label_7.hide()
            self.label_8.hide()
            self.k_cena.hide()
            self.k_cena_2.hide()
            self.k_cena_3.hide()
            self.k_cena_4.hide()
            self.k_cena_5.hide()
            self.pushButton_2.hide()
            self.tableWidget.show()
            self.count = 1
        else:
            self.label_3.show()
            self.k_nazv.show()
            self.label_4.show()
            self.label_6.show()
            self.label_5.show()
            self.label_7.show()
            self.label_8.show()
            self.k_cena.show()
            self.k_cena_2.show()
            self.k_cena_3.show()
            self.k_cena_4.show()
            self.k_cena_5.show()
            self.pushButton_2.show()
            self.tableWidget.hide()
            self.count = 0

    def update_menu(self):
        try:
            n = str((self.k_nazv.text()).strip())
            t = '"{}"'.format(n)
            s = int((self.k_cena.text()).strip())
            m_ = str((self.k_cena_2.text()).strip())
            m = '"{}"'.format(m_)
            o_ = str((self.k_cena_3.text()).strip())
            o = '"{}"'.format(o_)
            c = int((self.k_cena_4.text()).strip())
            v = int((self.k_cena_5.text()).strip())
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()
            ult = ("""SELECT * FROM rrr
                        WHERE title = {}""").format(str(t))
            result = cur.execute(ult).fetchall()
            if result == []:
                req = ("""INSERT INTO rrr (title, degree, sort, description, price, volume)
                          VALUES ({}, {}, {}, {}, {}, {})""").format(str(t), s, str(m), str(o), c, v)
                print(str(t))
                print(req)
                cur.execute(req)
                con.commit()
                self.loaddata()
            else:
                con = sqlite3.connect("coffee.sqlite")
                cur = con.cursor()
                ryr = ("""
                                    UPDATE rrr
                                SET degree = {}, sort = {}, description = {}, price = {}, volume = {}
                                WHERE title = {}
                                    """).format(s, str(m), str(o), c, v, str(t))
                cur.execute(ryr)
                con.commit()
                con.close()
                self.loaddata()
        except ValueError:
            self.label.setText('ошибка')
            return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Widget()
    ex.show()
    sys.exit(app.exec_())
