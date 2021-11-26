'''class Student:
  def __init__(self,a,b):
    self.roll_no=a
    self.name=b

  def display(self):
    print(self.roll_no,self.name)

s0=Student(0,'Nik')
s0.display()

s1=Student(1,'Sri')
s1.display()
'''
class Shape:
    def __init__(self, name):
        self.name = name
        self.area = None
        self.perimeter = None

    def display(self):
        print(f'{self.name} has an area of {self.area} and perimeter of {self.perimeter}')
class Square(Shape):
    def __init__(self,name,side):
        super().__init__(name)
        self.side=side
        self.compute_area()
        self.compute_perimeter()
    def compute_area(self):
        self.area= self.side*self.side
    def compute_perimeter(self):
        self.perimeter= 4*self.side
a=Square('sml',4)
print(a.side)
a.display()    