
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
import os
import time
from PIL import Image
from SingleController import data_predict,time_series

def users_database():
    files = os.listdir()
    if 'shurlz_database.csv' in files:
        pass
    else:
        users_database = pd.DataFrame(columns=['Name', 'Price', 'Date'])
        users_database.to_csv('shurlz_database.csv', index=False)

data = pd.read_csv('shurlz_database.csv')

data['Date'] = pd.to_datetime(data.Date)
data['Year'] = pd.to_datetime(data.Date).dt.year
data['Month'] = pd.to_datetime(data.Date).dt.month
data['Day'] = pd.to_datetime(data.Date).dt.day
default_end = str(data['Date'].max()).split(" ")[0].split("-")
default_start = str(data['Date'].min()).split(" ")[0].split("-")
default_max_price = data['Price'].sum()
default_min_price = 0

def Return(default,user):
    string = 'string'
    integer = 1011
    try:
        if type(user) == type(string) or type(integer):
            user = int(user)
            return user
        else:
            return default
    except:
        return default

class allplots:
    def __init__(self,count):
        self.count = 0
        self.plots = [image for image in os.listdir() if image.split('.')[-1] == 'png']
    def change_plot(self):
        if self.count < len(self.plots):
            self.count+=1
        return self.plots[self.count]
    def reset(self):
        self.count=-1

base = allplots('counts')

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.resize(850, 429)
        Form.setStyleSheet("background-color:black;")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 591, 361))
        self.label.setStyleSheet('background-image:url(D_most_spent_on_item.png)')
        self.label.setText("")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(610, 80, 71, 31))
        self.lineEdit.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:white;\n"
"font: 14pt \"Times New Roman\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(690, 80, 71, 31))
        self.lineEdit_2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(770, 80, 71, 31))
        self.lineEdit_3.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(690, 160, 71, 31))
        self.lineEdit_4.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(610, 160, 71, 31))
        self.lineEdit_5.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(770, 160, 71, 31))
        self.lineEdit_6.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(720, 290, 121, 31))
        self.lineEdit_7.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(720, 230, 121, 31))
        self.lineEdit_8.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(770, 390, 71, 31))
        self.pushButton.setStyleSheet("color:black;\n"
"background-color:white;\n"
"font: 11pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 390, 71, 31))
        self.pushButton_2.setStyleSheet("color:black;\n"
"background-color:white;\n"
"font: 11pt \"Times New Roman\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(610, 390, 41, 31))
        self.pushButton_3.setStyleSheet("font: 75 24pt \"Times New Roman\";\n"
"border-radius:14px;\n"
"background-color:white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(610, 11, 91, 31))
        self.comboBox.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color:white;\n"
"font: 14pt \"Times New Roman\";")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        #self.comboBox.addItem("")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(330, 390, 131, 31))
        self.lineEdit_9.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(170, 390, 131, 31))
        self.lineEdit_10.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(10, 390, 131, 31))
        self.lineEdit_11.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"color:rgb(0, 0, 0);\n"
"background-color:white;")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 340, 71, 31))
        self.pushButton_4.setStyleSheet("color:black;\n"
"background-color:white;\n"
"font: 11pt \"Times New Roman\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(660, 50, 131, 21))
        self.label_2.setStyleSheet("color:white;\n"
"font: 12pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(660, 130, 131, 21))
        self.label_3.setStyleSheet("color:white;\n"
"font: 12pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(610, 230, 91, 31))
        self.label_4.setStyleSheet("color:white;\n"
"font: 11pt \"Times New Roman\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(610, 290, 81, 31))
        self.label_5.setStyleSheet("color:white;\n"
"font: 11pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.lineEdit.setPlaceholderText(_translate("Form", "   year"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "  month"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "   day"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "  month"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "   year"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "    day"))
        self.lineEdit_7.setPlaceholderText(_translate("Form", " 0.00"))
        self.lineEdit_8.setPlaceholderText(_translate("Form", " 0.00"))
        self.pushButton.setText(_translate("Form", "Predict"))
        self.pushButton_2.setText(_translate("Form", "Add"))
        self.pushButton_3.setText(_translate("Form", "^"))
        self.comboBox.setItemText(0, _translate("Form", "barh"))
        #self.comboBox.setItemText(1, _translate("Form", "pie"))
        self.comboBox.setItemText(1, _translate("Form", "bar"))
        self.lineEdit_9.setPlaceholderText(_translate("Form", "      Date"))
        self.lineEdit_10.setPlaceholderText(_translate("Form", "      Amount"))
        self.lineEdit_11.setPlaceholderText(_translate("Form", "      Expense"))
        self.pushButton_4.setText(_translate("Form", "Plot"))
        self.label_2.setText(_translate("Form", "        Start Date"))
        self.label_3.setText(_translate("Form", "         End Date"))
        self.label_4.setText(_translate("Form", "Max Amount :"))
        self.label_5.setText(_translate("Form", "Min Amount :"))
        self.pushButton_2.clicked.connect(self.add_new_spending)
        self.pushButton_4.clicked.connect(self.plot_by_year_month_day)
        self.pushButton_3.clicked.connect(self.change_plot)
        self.pushButton.clicked.connect(self.Prediction_by_month)

    def add_new_spending(self):
        try:
            Name = self.lineEdit_11.text()
            Price = int(self.lineEdit_10.text())
            Date = self.lineEdit_9.text()
            data = pd.read_csv('shurlz_database.csv')
            new_data = {'Name': Name, 'Price': Price, 'Date': Date}
            shurlz = data.append(new_data, ignore_index=True)
            os.remove('shurlz_database.csv')
            shurlz.to_csv('shurlz_database.csv', index=False)
        except:
            pass

    def plot_by_year_month_day(self):
        try:
            s_user_yr = self.lineEdit.text()
            s_user_mt = self.lineEdit_2.text()
            s_user_day = self.lineEdit_3.text()
            e_user_yr = self.lineEdit_5.text()
            e_user_mt = self.lineEdit_4.text()
            e_user_day = self.lineEdit_6.text()
            u_min_price = self.lineEdit_7.text()
            u_max_price = self.lineEdit_8.text()
            plot_type = self.comboBox.currentText()
            new_data_frame = pd.DataFrame(data.groupby(['Year', 'Month', 'Day']).sum()['Price'])
            new_data_frame_without_day = pd.DataFrame(data.groupby(['Year', 'Month']).sum()['Price'])
            start_year = Return(int(default_start[0]), s_user_yr)
            start_month = Return(int(default_start[1]), s_user_mt)
            start_day = Return(int(default_start[2]), s_user_day)
            end_year = Return(int(default_end[0]), e_user_yr)
            end_month = Return(int(default_end[1]), e_user_mt)
            end_day = Return(int(default_end[2]), e_user_day)
            max_price = Return(default_max_price, u_max_price)
            min_price = Return(default_min_price, u_min_price)
            stage_1_data = new_data_frame.loc[(start_year, start_month, start_day):(end_year, end_month, end_day)]
            price_recorgnized_1 = stage_1_data[(stage_1_data['Price'] >= min_price) & (stage_1_data['Price'] <= max_price)]
            price_recorgnized_1.plot(kind=plot_type,color='gray')
            plt.title('Daily spendings')
            plt.savefig('A_year_month_day.png', bbox_inches='tight', dpi=100)

            # without the day.............................................................................................
            stage_2_data_without_day = new_data_frame_without_day.loc[(start_year, start_month):(end_year, end_month)]
            price_recorgnized_2_without_day = stage_2_data_without_day[
                 (stage_2_data_without_day['Price'] >= min_price) & (stage_2_data_without_day['Price'] <= max_price)]
            price_recorgnized_2_without_day.plot(kind=plot_type,color='gray')
            plt.title('Monthly spendings')
            plt.savefig('B_year_month.png', bbox_inches='tight', dpi=100)

            # # plotting others
            plot_products = data.copy()
            plt.title('Most spent on items by cost')
            plot_products.groupby('Name').sum()['Price'].plot(kind=plot_type,color='gray')
            plt.savefig('C_products_by_price.png', bbox_inches='tight', dpi=100)

            plot_most_spent_on_item = data.copy()
            plot_most_spent_on_item.Name.value_counts().plot(kind=plot_type,color='gray')
            plt.title('most occuring item')
            plt.savefig('D_most_spent_on_item.png', bbox_inches='tight', dpi=100)

            for files in os.listdir():
                if files.split('.')[-1] == 'png':
                    name = files.split('.')[0]
                    image = Image.open(files)
                    if int(image.width) != 591 and int(image.height) != 361:
                        image = image.resize((591, 361), resample=Image.LANCZOS)
                        image.save(f'{name}.png')
            plots = []
            for files in os.listdir():
                if files.split('.')[-1] == 'png':
                    plots.append(files)
            print(plots)
            time.sleep(1)
            self.label.setStyleSheet(f"background-image:url({plots[0]})")
        except:
            pass

    def change_plot(self):
        if self.pushButton_3.isChecked()==False:
            if base.count < len(base.plots):
                base.change_plot()
                self.label.setStyleSheet(f"background-image:url({base.plots[base.count]})")
                print(base.count)
                if base.count == len(base.plots)-1:
                    base.reset()

    def Prediction_by_month(self):
        data = data_predict()
        plt.plot(data.index[:-2], data['Price'][:-2], 'b*-')
        plt.plot(data.index[-3:], data['Price'][-3:], '*--',color='gray')
        plt.title('Linear Regression Prediction - (gray)')
        plt.savefig('F_prediction.png', bbox_inches='tight', dpi=100)
        for files in os.listdir():
            if files.split('.')[-1] == 'png':
                name = files.split('.')[0]
                image = Image.open(files)
                if int(image.width) != 591 and int(image.height) != 361:
                    image = image.resize((591, 361), resample=Image.LANCZOS)
                    image.save(f'{name}.png')
        time.sleep(1)
        self.label.setStyleSheet(f"background-image:url('F_prediction.png')")

print(users_database())
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    users_database()
    ui = Ui_Form()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())