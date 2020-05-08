import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QTextBrowser
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5 import uic
from PyQt5.QtGui import QPixmap
from config import *
from main import *



class Hello_window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('hello.ui', self)

        self.pushButton.clicked.connect(self.open_coords)
        self.pushButton_2.clicked.connect(self.open_sincos)

    def open_coords(self):
        self.first_coords = FirstForm_for_coords(self, '')
        self.first_coords.show()
        Hello_window().hide()
    
    def open_sincos(self):
        self.first_sincos = Sincos_first(self, '')
        self.first_sincos.show()



class Sincos_first(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('sincos.ui', self)

        self.pushButton.clicked.connect(self.open_second)
            
    def open_second(self):
        
        self.alpha = self.line_alpha.text()
        self.beta = self.line_beta.text()
        self.gamma = self.line_gamma.text()
        self.ab = self.line_ab.text()
        self.bc = self.line_bc.text()
        self.ac = self.line_ac.text()
        self.a = self.line_a.text()
        self.b = self.line_b.text()
        self.c = self.line_c.text()

        if self.a == '':
            self.a = 'a'
        if self.b == '':
            self.b = 'b'
        if self.c == '':
            self.c = 'c'
        try:
            if self.alpha == '':
                self.alpha = None
            else:
                self.alpha = float(self.alpha)
            if self.beta == '':
                self.beta = None
            else:
                self.beta = float(self.beta)
            if self.gamma == '':
                self.gamma = None
            else:
                self.gamma = float(self.gamma)
            if self.ab == '':
                self.ab = None
            else:
                self.ab = float(self.ab)
            if self.bc == '':
                self.bc = None
            else:
                self.bc = float(self.bc)
            if self.ac == '':
                self.ac = None
            else:
                self.ac = float(self.ac)
        except ValueError:
            tangle = Triangle_elems(self.a, self.b, self.c, alpha=self.alpha, beta=self.beta, gamma=self.gamma,
                                ab=self.ab, bc=self.bc, ac=self.ac)
            tangle.error3 = True
                
        else:
            tangle = Triangle_elems(self.a, self.b, self.c, alpha=self.alpha, beta=self.beta, gamma=self.gamma,
                                    ab=self.ab, bc=self.bc, ac=self.ac)
        tangle.count()

        self.second_form = Sincos_second(self, self.a, self.b, self.c, self.ab, self.bc, self.ac,
                                         self.alpha, self.beta, self.gamma, tangle.error3)
        self.second_form.show()


class Sincos_second(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)    

    def initUI(self, args):
        self.setGeometry(400, 100, *WIN_SIZE)
        self.setWindowTitle('Secondform')
        print(args)
        tangle = Triangle_elems(*args[1:10])
        tangle.error3 = args[10]
        tangle.count()
        self.output = QTextBrowser(self)
        self.output.move(520, 0)
        self.output.resize(480, 500)
        self.image = QLabel(self)
        self.image.resize(500, 500)
        pixmap = QPixmap('test.jpg')
        if tangle.error:
            self.output.setText('''                               ERROR 
                Похоже вы ввели недопустимую комбинацию
            Доступные комбинации:
                                3 стороны
                                сторона и 2 прилежащих к ней угла
                                2 стороны и угол между ними
                                2 стороны и угол смежный с одной из них
                                сторона угол смежный с ней и противолежащий угол 
                                ''')
        else:
            if tangle.error2:
                self.output.setText('''                               ERROR 
                    Такого треугольника, увы, не сущесвует''')
            else:
                if tangle.error3:
                    self.output.setText('''                               ERROR 
                    Вы ввели некоректные данные''')
                else:
                    self.output.setText(f'''        {tangle.ab_name} = {tangle.ab}
        {tangle.bc_name} = {tangle.bc}
        {tangle.ac_name} = {tangle.ac}
        {tangle.beta_name} = {tangle.beta}
        {tangle.alpha_name} = {tangle.alpha}
        {tangle.gamma_name} = {tangle.gamma}
        Масштаб 1:{tangle.counter}''')

                    self.image.setPixmap(pixmap)
                    self.image.setScaledContents(True)


class FirstForm_for_coords(QWidget):
    def __init__(self, *args):
        super().__init__()
        uic.loadUi('coords.ui', self)
        self.pushButton.clicked.connect(self.open_second)
        self.error = False

    def open_second(self):
        self.ax = self.line_ax.text()
        self.ay = self.line_ay.text()
        self.bx = self.line_bx.text()
        self.by = self.line_by.text()
        self.cx = self.line_cx.text()
        self.cy = self.line_cy.text()

        if '' in [self.ax, self.ay, self.bx, self.by, self.cx, self.cy]:
            return
        else:
            try:
                self.ax = float(self.ax)
                self.ay = float(self.ay)
                self.bx = float(self.bx)
                self.by = float(self.by)
                self.cx = float(self.cx)
                self.cy = float(self.cy)
                self.a = (self.ax, self.ay)
                self.b = (self.bx, self.by)
                self.c = (self.cx, self.cy)
            except Exception:
                self.a = (self.ax, self.ay)
                self.b = (self.bx, self.by)
                self.c = (self.cx, self.cy)
                tangle = Triangle_coords(self.a, self.b, self.c)
                tangle.error2 = True
            else:
                tangle = Triangle_coords(self.a, self.b, self.c)
                tangle.count()
            self.second_form = SecondForm_for_coords(self, self.a, self.b, self.c, tangle.error2)
            self.second_form.show()


class SecondForm_for_coords(QWidget):
    def __init__(self, *args):
        super().__init__()
        self.initUI(args)

    def initUI(self, args):
        self.setGeometry(300, 300, *WIN_SIZE)
        self.setWindowTitle('Secondform')
        tangle = Triangle_coords(*args[1:4])
        tangle.error2 = args[4]
        if not tangle.error2:
            tangle.count()

        self.image = QLabel(self)
        self.image.resize(500, 500)
        pixmap = QPixmap('test.jpg')
        self.image.setScaledContents(True)
        
        self.output = QTextBrowser(self)
        self.output.move(520, 0)
        self.output.resize(480, 500)
        if tangle.error:
                self.output.setText('''                               ERROR 
                    Такого треугольника, увы, не сущесвует''')
        else:
            if tangle.error2:
                    self.output.setText('''                               ERROR 
                    Вы ввели некоректные данные''')
            else:
                self.output.setText(f''' AB = {tangle.ab}
    BC = {tangle.bc}
    AC = {tangle.ac}
    ∠ABC = {tangle.beta}
    ∠BAC = {tangle.alpha}
    ∠BCA = {tangle.gamma}
    Периметр = {tangle.per}
    Площадь = {tangle.ar}
    Масштаб 1:{tangle.counter}''')
                self.image.setPixmap(pixmap)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Hello_window()
    ex.show()
    sys.exit(app.exec())