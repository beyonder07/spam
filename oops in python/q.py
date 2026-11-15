class Student:
    def __init__(self,name,m1,m2,m3):
        self.name = name
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3
    def avg(self):
        avg=(self.m1 + self.m2 + self.m3) / 3
        print(avg)
s1=Student("Ravi",45,45,45)
print(s1.name,s1.m1,s1.m2,s1.m3)
s1.avg()
