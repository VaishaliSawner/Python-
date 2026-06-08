class Time:
    def __init__(self,h,m,s):
        self.__h=h
        self.__m=m
        self.__s=s
    
    def display(self):
        print(f"{self.__h},{self.__m},{self.__s}")
        
    def __mul__ (self,other):
        temp=Time(0,0,0)
        temp.__h=self.__h * other.__h 
        temp.__m=self.__m * other.__m 
        temp.__s=self.__s * other.__s 
        
        if temp.__s>=60:
            temp.__m=temp.__m+temp.__s//60
            temp.__s=temp.__s%60
        if temp.__m>=60:
             temp.__h=temp.__h+temp.__m//60
             temp.__m=temp.__m%60
        return temp
            
d1=Time(2,12,12)
d2=Time(3,15,15)
d1.display()
d2.display()
d3=d1*d2
d3.display()