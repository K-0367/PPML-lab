class Addition:
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
    def add(self):
        print(self.data1+self.data2)

class substraction:
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
    def sub(self):
        print(self.data1-self.data2)

class multiplication:
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
    def mul(self):
        print(self.data1*self.data2)

class substraction:
    def __init__(self,data1,data2):
        self.data1=data1
        self.data2=data2
    def div(self):
        if self.data1 !=0:
            print("division is possible")
        else:
            print("divison is not possible")
class calc(Addition,substraction,multiplication):
    def __init__(self, data1, data2):
        self.data1=data1
        self.data2=data2
calc(1,2).add()
calc(1,7).div()