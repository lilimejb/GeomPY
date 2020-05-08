import math
from PIL import Image, ImageDraw
# from interface import *


class Triangle_coords():
    def __init__(self, a, b, c):
        self.alpha = None
        self.beta = None
        self.gamma = None
        self.a = a
        self.b = b
        self.c = c
        self.ab = None
        self.bc = None
        self.ac = None
        self.per = None
        self.ar = None
        self.error = False
        self.error2 = False
        
    
    
    def perimetr(self):
        self.per = self.ab + self.bc + self.ac
    

    def ab_counter(self):
        ax, ay = self.a
        bx, by = self.b
        self.ab = round(math.sqrt((ax - bx) ** 2 + (ay - by) ** 2), 1)


    def bc_counter(self):
        bx, by = self.b
        cx, cy = self.c
        self.bc = round(math.sqrt((cx - bx) ** 2 + (cy - by) ** 2), 1)
    

    def ac_counter(self):
        ax, ay = self.a
        cx, cy = self.c
        self.ac = round(math.sqrt((ax - cx) ** 2 + (ay - cy) ** 2), 1)
    

    def alpha_counter(self):
        self.alpha = round(math.degrees(math.acos((self.ab ** 2 + self.ac ** 2 - self.bc ** 2) / (2 * self.ab * self.ac))), 1)


    def beta_counter(self):
        self.beta = round(math.degrees(math.acos((self.ab ** 2 + self.bc ** 2 - self.ac ** 2) / (2 * self.ab * self.bc))), 1)

    def gamma_counter(self):
        self.gamma = round(math.degrees(math.acos((self.ac ** 2 + self.bc ** 2 - self.ab ** 2) / (2 * self.ac * self.bc))), 1)


    def area(self):
        self.ar = round(self.ab * self.ac * math.sin(math.radians(self.alpha)) / 2, 1)


    def count(self):
        if self.error2:
            return
        else:
            self.ab_counter()
            self.bc_counter()
            self.ac_counter()
            if self.ab <= 0 or self.bc <= 0 or self.ac <= 0:
                self.error = True
            else:
                if self.ab <= self.bc + self.ac and self.bc <= self.ab + self.ac and self.ac <= self.ab + self.bc:
                    self.alpha_counter()
                    self.beta_counter()
                    self.gamma_counter()
                    if self.alpha + self.beta + self.gamma != 180:
                        self.error = True
                    else:
                        self.perimetr()
                        self.area()
                        self.picture('test.jpg', 500, 500)
                else:
                    self.error = True
        

    def picture(self, file_name, width, height, background_color='#ffffff', triangle_color='#bF311A',):
        im = Image.new("RGB", (width, height))
        drawer = ImageDraw.Draw(im)

        drawer.rectangle(((0, 0), (width, height)), background_color)
        
        
        ax, ay = self.a
        bx, by = self.b
        cx, cy = self.c
        ax = ax % 8 + 1
        ay = ay % 8 + 1
        bx = bx % 8 + 1
        by = by % 8 + 1
        cx = cx % 8 + 1
        cy = cy % 8 + 1
        self.counter = ax // 8 + 1
        drawer.polygon([(width // 4 + ax * width // 10, height // 2 + int(-1 * (ay * width // 10))),
                        (width // 4 + bx * width // 10, height // 2 + int(-1 * (by * width // 10))),
                        (width // 4 + cx * width // 10, height // 2 + int(-1 * (cy * width // 10)))], triangle_color)

        drawer.line((width // 2, 0, width // 2, height), fill=(0, 0, 0), width=5)
        drawer.line((0, height // 2, width, height // 2), fill=(0, 0, 0), width=5)
        drawer.line((width // 2 + 2, 0, width // 2 + 5, 5), fill=(0, 0, 0), width=10)
        im.save(file_name)

    
class Triangle_elems():
    def __init__(self, a='a', b='b', c='c', 
                       ab = None, bc = None, ac = None,
                       alpha = None, beta = None, gamma = None):
        self.ab_name = a.upper() + b.upper()
        self.ac_name = a.upper() + c.upper()
        self.bc_name = b.upper() + c.upper()
        self.alpha_name = '∠' + b.upper() + a.upper() + c.upper()
        self.beta_name = '∠' + a.upper() + b.upper() + c.upper()
        self.gamma_name = '∠' + b.upper() + c.upper() + a.upper()
        self.between = False
        self.near = False
        self.side_between = False
        self.side_away = False
        self.ab_bool = False
        self.bc_bool = False
        self.ac_bool = False
        self.alpha_bool = False
        self.beta_bool = False
        self.gamma_bool = False
        self.side3 = False
        self.error = False 
        self.error2 = False
        self.error3 = False

        if ab != None and bc != None and ac != None:
            self.ab = ab
            self.ac = ac
            self.bc = bc
            self.side3 = True


        if ab != None and ac != None:
            if alpha != None:
                self.ab = ab
                self.ac = ac
                self.alpha = alpha
                self.between = True
                self.gamma_bool = True
                self.beta_bool = True
            elif beta != None:
                self.ab = ab
                self.ac = ac
                self.beta = beta
                self.near = True
                self.alpha_bool = True
                self.gamma_bool = True
            elif gamma != None:
                self.ab = ab
                self.ac = ac
                self.gamma = gamma
                self.near = True
                self.alpha_bool = True
                self.beta_bool = True
            self.bc_bool = True


        if ab != None and bc != None:
            if beta != None:
                self.ab = ab 
                self.bc = bc
                self.beta = beta
                self.between = True
                self.alpha_bool = True
                self.gamma_bool = True
            elif gamma != None:
                self.ab = ab
                self.bc = bc
                self.gamma = gamma
                self.near = True
                self.alpha_bool = True
                self.beta_bool = True
            elif alpha != None:
                self.ab = ab
                self.bc = bc
                self.alpha = alpha
                self.near = True
                self.gamma_bool = True
                self.beta_bool = True
            self.ac_bool = True

        if bc != None and ac != None:
            if gamma != None:
                self.bc = bc
                self.ac = ac
                self.gamma = gamma
                self.between = True
                self.alpha_bool = True
                self.beta_bool = True
            elif beta != None:
                self.bc = bc
                self.ac = ac
                self.beta = beta
                self.near = True
                self.alpha_bool = True
                self.gamma_bool = True
            elif alpha != None:
                self.bc = bc
                self.ac = ac
                self.alpha = alpha
                self.near = True
                self.gamma_bool = True
                self.beta_bool = True
            self.ab_bool = True
        

        if alpha != None and beta != None:
            if ab != None:
                self.alpha = alpha
                self.beta = beta
                self.ab = ab
                self.side_between = True
                self.ac_bool = True
                self.bc_bool = True
            elif ac != None:
                self.alpha = alpha
                self.beta = beta
                self.ac = ac
                self.side_away = True
                self.ab_bool = True
                self.bc_bool = True
            elif bc != None:
                self.alpha = alpha
                self.beta = beta
                self.bc = bc
                self.side_away = True
                self.ab_bool = True
                self.ac_bool = True
            self.gamma_bool = True

        if beta != None and gamma != None:
            if ab != None:
                self.gamma = gamma
                self.beta = beta
                self.ab = ab
                self.side_away = True
                self.ac_bool = True
                self.bc_bool = True
            elif ac != None:
                self.gamma = gamma
                self.beta = beta
                self.ac = ac
                self.side_away = True
                self.ab_bool = True
                self.bc_bool = True
            elif bc != None:
                self.gamma = gamma
                self.beta = beta
                self.bc = bc
                self.side_between = True
                self.ab_bool = True
                self.ac_bool = True
            self.alpha_bool = True

        if alpha != None and gamma != None:
            if ab != None:
                self.gamma = gamma
                self.alpha = alpha
                self.ab = ab
                self.side_away = True
                self.ac_bool = True
                self.bc_bool = True
            elif ac != None:
                self.gamma = gamma
                self.alpha = alpha
                self.ac = ac
                self.side_between = True
                self.ab_bool = True
                self.bc_bool = True
            elif bc != None:
                self.gamma = gamma
                self.alpha = alpha
                self.bc = bc
                self.side_away = True
                self.ac_bool = True
                self.ab_bool = True
            self.beta_bool = True
    
    def sides3(self, ab, bc, ac):
        if ab <= bc + ac and bc <= ab + ac and ac <= ab + bc:
            self.alpha = round(math.degrees(math.acos((ab ** 2 + ac ** 2 - bc ** 2) / (2 * ab * ac))), 1)
            self.beta = round(math.degrees(math.acos((ab ** 2 + bc ** 2 - ac ** 2) / (2 * ab * bc))), 1)
            self.gamma = round(math.degrees(math.acos((ac ** 2 + bc ** 2 - ab ** 2) / (2 * ac * bc))), 1)
            if (self.alpha + self.beta + self.gamma != 180) or self.alpha <= 0 or self.beta <= 0 or self.gamma <= 0:
                self.error2 = True
        else:
            self.error2 = True
        

    def between_func(self, ab, ac, alpha):
        if alpha == 0:
            self.error2 = True
        else:
            bc = round(math.sqrt(ab ** 2 + ac ** 2 - (2 * ab * ac * math.cos(math.radians(alpha)))), 1)
            beta = round(math.degrees(math.acos((ab ** 2 + bc ** 2 - ac ** 2) / (2 * ab * bc))), 1)
            gamma = round((180 - beta - alpha), 1)

            if self.bc_bool:
                self.bc = bc
                self.beta = beta
                self.gamma = gamma

            elif self.ab_bool:
                self.ab = bc
                self.beta = gamma
                self.alpha = beta

            elif self.ac_bool:
                self.ac = bc
                self.alpha = gamma
                self.gamma = beta
            if (self.alpha + self.beta + self.gamma != 180) or self.alpha <= 0 or self.beta <= 0 or self.gamma <= 0:
                self.error2 = True

    
    def near_func(self, ab, ac, alpha):
        if alpha == 0:
            self.error2 = True
        else:
            gamma = round(math.asin((ab * math.sin(math.radians(alpha)) / ac)), 1)
            beta = round((180 - gamma - alpha), 1)
            bc = round(math.sqrt(ab ** 2 + ac ** 2 - (2 * ab * ac * math.cos(math.radians(beta)))), 1)

            if self.bc_bool:
                self.bc = bc
                if self.gamma_bool:
                    self.alpha = beta
                    self.gamma = gamma
                    self.beta = alpha
                if self.beta_bool:
                    self.alpha = gamma
                    self.gamma = alpha
                    self.beta = beta
            elif self.ac_bool:
                self.ac = bc
                if self.alpha_bool:
                    self.alpha = beta
                    self.gamma = alpha
                    self.beta = gamma 
                if self.gamma_bool:
                    self.gamma = beta
                    self.alpha = alpha
                    self.beta = gamma
            elif self.ab_bool:
                self.ab = bc
                if self.alpha_bool:
                    self.beta = alpha
                    self.gamma = beta
                    self.alpha = gamma
                if self.beta_bool:
                    self.alpha = alpha
                    self.beta = gamma
                    self.gamma = beta
            if (self.alpha + self.beta + self.gamma != 180) or self.alpha <= 0 or self.beta <= 0 or self.gamma <= 0:
                self.error2 = True
        
    def side_between_func(self, alpha, beta, ab):
        if alpha == 0 or beta == 0:
            self.error2 = True
        else:
            gamma = round((180 - alpha - beta), 1)
            bc = round((ab * math.sin(math.radians(alpha))) / math.sin(math.radians(gamma)), 1)
            ac = round(math.sqrt(ab ** 2 + bc ** 2 - (2 * ab * bc * math.cos(math.radians(beta)))), 1)

            if self.gamma_bool and self.bc_bool and self.ac_bool:
                self.bc = bc
                self.ac = ac
                self.gamma = gamma
            elif self.beta_bool and self.ab_bool and self.bc_bool:
                self.beta = gamma
                self.ab = bc
                self.bc = ac
            elif self.alpha_bool and self.ab_bool and self.ac_bool:
                self.alpha = gamma
                self.ab = ac
                self.ac = bc
            if (self.alpha + self.beta + self.gamma != 180) or self.alpha <= 0 or self.beta <= 0 or self.gamma <= 0:
                self.error2 = True

    def side_away_func(self, alpha, beta, ac):
        if alpha == 0 or beta == 0:
            self.error2 = True
        else:
            gamma = round(180 - alpha - beta, 1)
            bc = round((ac * math.sin(math.radians(alpha))) / math.sin(math.radians(beta)), 1)
            ab = round(math.sqrt(ac ** 2 + bc ** 2 - (2 * ac * bc * math.cos(math.radians(gamma)))), 1)

            if self.gamma_bool: 
                if self.ab_bool and self.bc_bool:
                    self.gamma = gamma
                    self.ab = ab
                    self.bc = bc
                if self.ab_bool and self.ac_bool:
                    self.ab = ab
                    self.gamma = gamma
                    self.ac = bc
            elif self.beta_bool:
                if self.ab_bool and self.ac_bool:
                    self.beta = gamma
                    self.ab = bc
                    self.ac = ab
                if self.bc_bool and self.ac_bool:
                    self.beta = gamma
                    self.bc = bc
                    self.ac = ab
            elif self.alpha_bool:
                if self.bc_bool and self.ac_bool:
                    self.alpha = gamma
                    self.bc = ab
                    self.ac = bc
                if self.bc_bool and self.ab_bool:
                    self.alpha = gamma
                    self.bc = ab
                    self.ab = bc
            
        if (self.alpha + self.beta + self.gamma != 180) or self.alpha <= 0 or self.beta <= 0 or self.gamma <= 0:
            self.error2 = True
    
    def median_couter(self):
        pass
    
    def vertical_counter(self):
        pass

    def bisector(self):
        pass

    def picture(self, file_name, width, height, background_color='#ffffff', triangle_color='#bF311A',):
        im = Image.new("RGB", (width, height))
        drawer = ImageDraw.Draw(im)

        drawer.rectangle(((0, 0), (width, height)), background_color)

        rightangle_alpha = self.gamma
        bx = self.bc * math.cos(math.radians(rightangle_alpha))
        ox = bx 
        rightangle_beta = math.degrees(math.asin(ox / self.bc))
        bc = self.bc % 8 + 1
        ac = self.ac % 8 + 1
        self.counter = int((self.bc // 8) + 1)
        # print(self.bc * math.cos(math.radians(self.gamma)))
        # print(rightangle_beta)
        # print(self.bc * math.cos(math.radians(rightangle_beta)))

        drawer.polygon([((width // 16), (height - 100)),
                        ((width // 16 + ac * (width // 10)), (height - 100)),
                        ((width // 16 + bc * math.cos(math.radians(rightangle_alpha)) * (width // 10)), 
                        (height - 100 - bc * math.cos(math.radians(rightangle_beta)) * (width // 10)))], 
                        triangle_color)
        im.save(file_name)
        
    def count(self):
        if not self.between and not self.near and not self.side_between and not self.side3 and not self.side_away:
            print('Всё плохо')
            self.error = True
        else:
            if not self.error3:
                if self.between:
                    if not self.ab_bool and not self.ac_bool and not self.alpha_bool:
                        self.between_func(self.ab, self.ac, self.alpha)
                    if not self.ab_bool and not self.bc_bool and not self.beta_bool:
                        self.between_func(self.bc, self.ab, self.beta)
                    if not self.ac_bool and not self.bc_bool and not self.gamma_bool:
                        self.between_func(self.ac, self.bc, self.gamma)

                if self.near:
                    if self.ab_bool and self.gamma_bool:
                        if self.alpha_bool:
                            self.near_func(self.ac, self.bc, self.beta)
                        elif self.beta_bool:
                            self.near_func(self.bc, self.ac, self.alpha)
                    if self.bc_bool and self.alpha_bool:
                        if self.gamma_bool:
                            self.near_func(self.ab, self.ac, self.beta)
                        if self.beta_bool:
                            self.near_func(self.ac, self.ab, self.gamma)
                    if self.ac_bool and self.beta_bool:
                        if self.alpha_bool:
                            self.near_func(self.bc, self.ab, self.gamma)
                        if self.gamma_bool:
                            self.near_func(self.ab, self.bc, self.alpha)

                if self.side_between:
                    if self.gamma_bool and self.bc_bool and self.ac_bool:
                        self.side_between_func(self.alpha, self.beta, self.ab)
                    elif self.beta_bool and self.ab_bool and self.bc_bool:
                        self.side_between_func(self.gamma, self.alpha, self.ac)
                    elif self.alpha_bool and self.ab_bool and self.ac_bool:
                        self.side_between_func(self.beta, self.gamma, self.bc)
                
                if self.side3:
                    self.sides3(self.ab, self.bc, self.ac)
                
                if self.side_away:
                    if self.gamma_bool and self.ab_bool:
                        if self.bc_bool:
                            self.side_away_func(self.alpha, self.beta, self.ac)
                        elif self.ac_bool:
                            self.side_away_func(self.beta, self.alpha, self.bc)
                    if self.alpha_bool and self.bc_bool:
                        if self.ac_bool:
                            self.side_away_func(self.beta, self.gamma, self.ab)
                        elif self.ab_bool:
                            self.side_away_func(self.gamma, self.beta, self.ac)
                    if self.beta_bool and self.ac_bool:
                        if self.ab_bool:
                            self.side_away_func(self.gamma, self.alpha, self.bc)
                        elif self.bc_bool:
                            self.side_away_func(self.alpha, self.beta, self.ab)
                    
                

            if not self.error2 and not self.error3:
                print(self.ab_name, '=', self.ab)
                print(self.ac_name, '=', self.ac)
                print(self.bc_name, '=', self.bc)
                print(self.alpha_name, '=', self.alpha)
                print(self.beta_name, '=', self.beta)
                print(self.gamma_name, '=', self.gamma)
                self.picture('test.jpg', 1024, 840)
            
                

      
        
