'''demonstrate Single Inheritance. Create class Total 
with methods that will calculate the sum and 
percentage of the user-defined six subjects'''

class Total:

    def __init__(self,s1,s2,s3,s4,s5,s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6

    def Sum(self):
        return (self.s1+self.s2+self.s3+self.s4+self.s5+self.s6)

class Perc(Total):
    def Perc(self):
        return ((self.s1+self.s2+self.s3+self.s4+self.s5+self.s6)/600)*100
sub1 = int(input("Please enter the marks for subjest 1: "))
sub2 = int(input("Please enter the marks for subjest 2: "))
sub3 = int(input("Please enter the marks for subjest 3: "))
sub4 = int(input("Please enter the marks for subjest 4: "))
sub5 = int(input("Please enter the marks for subjest 5: "))
sub6 = int(input("Please enter the marks for subjest 6: "))
marks = Perc(sub1,sub2,sub3,sub4,sub5,sub6)
ADD = marks.Sum()
PERC = marks.Perc()

print("Total marks are: ", ADD)
print("Total percents: ", PERC,"%")