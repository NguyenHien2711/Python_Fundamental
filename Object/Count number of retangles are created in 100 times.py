import random
class Triangle:
    #Hàm khởi tạo
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    # Hàm check
    def validate(self):
        if self.a + self.b> self.c and self.b + self.c> self.a and self.c + self.a> self.b:
            return True
        else: 
            return False
    def info(self):
        print(f'({self.a}, {self.b}, {self.c})')
tg = Triangle(3,5,6)
print(tg.validate())
edges = [i for i in range(1,100,1)]
triangles = []
for i in range(100):
    a = random.choice(edges)
    b = random.choice(edges)
    c = random.choice(edges)
    tg = Triangle(a, b, c)
    tg.info()
    print(tg.validate())
    triangles.append(tg.validate())
print(triangles)
result_number_retangles = 0
for i in range(len(triangles)):
    if triangles[i]:
        result_number_retangles = result_number_retangles + 1
print(f'The number of retangles are created: {result_number_retangles}')