import sys
from PyQt5 import QtWidgets,QtCore,QtGui

from Ui_Ccr_main import *

class Ccr_MainWin(QtWidgets.QWidget):
    
    def __init__(self,parent=None):
        super().__init__(parent)
        self.ui = Ui_Ccr()
        self.a = self.ui.setupUi(self)
        self.ini_set()    # 加载窗口初始设置

    def ini_set(self):
        self.center()     # 设置窗口居中
        self.input_valid() # 设置数据输入格式限制
        self.ui.pushButton.clicked.connect(self.check_data_miss)   #按键链接槽函数进行计算

    # 设定函数使窗口位置居中
    def center(self):                     
        screen = QtWidgets.QApplication.desktop()
        size = self.geometry()
        self.move((screen.width() - size.width())/2,(screen.height() - size.height())/2) 

    # 设置函数限制输入数据格式
    def input_valid(self):
        self.ui.lineEdit.setValidator(QtGui.QIntValidator(1,100))
        self.ui.lineEdit_2.setValidator(QtGui.QDoubleValidator(15.0,500.0,2))
        self.ui.lineEdit_3.setValidator(QtGui.QDoubleValidator(1.0,200.0,2))
    
    # 检查数据空项
    def check_data_miss(self):
        data_miss =[]   #创建确实数据容器
        data_miss_str=''    #空项字符串

        if self.ui.lineEdit.text()=='':
            data_miss.append('年龄，')
        if self.ui.lineEdit_2.text()=='':
            data_miss.append('体重，')
        if self.ui.lineEdit_3.text()=='':
            data_miss.append('血肌酐值，')

        if len(data_miss) != 0: #审查是否有空项
            data_miss[-1]=data_miss[-1][0:-1]+'．'   #删除最后的逗号改为句号
            for i in range (len(data_miss)):
                data_miss_str=data_miss_str+data_miss[i]               
            QtWidgets.QMessageBox.warning(self,'缺少必要数据','缺少的数据：'+data_miss_str) #如果空项，提醒
        else:   #如果无空项，调用计算
            self.caculate()

    
    # 设置函数进行数据最终计算
    def caculate(self):
        
        gender = 1.0       # 设置性别因子
        if self.ui.radioButton.isChecked()==True:
            gender=1.0
        else:
            gender=0.85
        age = int(self.ui.lineEdit.text())  #获取年龄
        weight = float(self.ui.lineEdit_2.text())   #获取体重
        cr = float(self.ui.lineEdit_3.text())   #获取血肌酐值

        ccr = 140*weight/(0.818*cr)*gender  #计算ｃｃｒ结果
        self.ui.label_7.setText(str(ccr))   #输出结果


def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Ccr_MainWin()
    main.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()