#Bài tập Định nghĩa lớp điểm (Point) gồm 2 thuộc tính x và y
#Các phương thức thông tin tọa độ của điểm. Tính khoảng cách từ 2 điểm (distance)
#Phương thức tính khoảng cách đến gốc tọa độ (Ox)
#Tính chu vi của hình tam giá từ 3 điểm
#Visulization tam giác
import math
import turtle as t
#Xây dựng lớp điểm
class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def info(self):
        print(f'{self.x}, {self.y}')
    def distance_o(self):
        '''Khoảng cách từ điểm P đến O'''
        return round(math.sqrt(self.x**2 + self.y**2),2)
    def distance_p(self,p):
        '''Khoảng cách từ hai điểm'''
        return round(math.sqrt((self.x-p.x)**2 + (self.y-p.y)**2), 2)
p1 = Point(0,200)
p2 = Point(100,-20)
distance_o = p1.distance_o()
distance_p2 = p1.distance_p(p2)
print(distance_o)
print(distance_p2)
#Tính chu vi của hình tam giác tạo thành từ 3 điểm
class Triangles:
    def __init__(self, p1,p2,p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def length(self):
        length = self.p1.distance_p(self.p2) + self.p2.distance_p(self.p3) + self.p3.distance_p(self.p1)
        return length
    def visulization(self):
        '''Vẽ hình tam giác bằng turtle'''
        t.shape('circle')
        t.color('blue')
        t.penup()
        t.goto(self.p1.x, self.p1.y)
        t.stamp()
        t.pendown()
        t.goto(self.p2.x, self.p2.y)
        t.stamp()
        t.goto(self.p3.x, self.p3.y)
        t.stamp()
        t.goto(self.p1.x, self.p1.y)
        t.done()
p3 = Point(0,0)
triangle = Triangles(p1,p2,p3)
triangle.visulization()
#Nhận xét: Lớp được xây dựng theo tầng và khai báo các biến, Lớp tam giác được tạo thành từ các lớp điểm, và trong lớp điểm lại có các thuộc tính và phương thức
#Mình sẽ access từng lớp một và vận dụng các thuộc tính, phương thức trong class