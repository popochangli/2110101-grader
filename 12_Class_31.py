class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

class Rect:
    def __init__(self, p1, p2):
        self.lowerleft = p1
        self.upperright  = p2
    def area(self):
        return (self.upperright.x-self.lowerleft.x)*(self.upperright.y-self.lowerleft.y)
    def contains(self, p):
        return self.upperright.x>=p.x>=self.lowerleft.x and self.upperright.y>=p.y>=self.lowerleft.y

x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p))

'''
2 2 10 10
4
0 0
2 4
3 5
10 1
'''