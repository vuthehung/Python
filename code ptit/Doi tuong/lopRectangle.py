class Rectangle:
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.colors=color.title()
    def invalid(self):
        return self.x>0 and self.y>0
    def perimeter(self):
        return (self.x+self.y)*2
    def area(self):
        return self.x*self.y
    def color(self):
        return self.colors
arr = input().split()
r = Rectangle(int(arr[0]), int(arr[1]), (arr[2]))
if(r.invalid()):
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
else:
    print("INVALID")
