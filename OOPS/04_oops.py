########################################################################################
###################### Sttaic method in OOP ######################################
#### 1 method
class day:
    dayname=["Sun","Mon","Tue","Wed","Thu","Fri"]
    def dayinfo(self):
        if self.dayinput in day.dayname:
            print("valid input")
            self.greeting()
        else:
            print("invalid input")
            self.input= False
    @staticmethod       ## this static method is applid to avoid use of self in defining object method
    def greeting():
        print("Good morning!")

day1=day()
day1.dayinput="Sun"     ## varibales, attributes, property are inerchagiably used in OOP
day1.dayinfo()
#day1.greeting()

day2=day()
day2.dayinput="Sunday"
day2.dayinfo()
#day2.greeting()


#### 1 method
class day:
    dayname=["Sun","Mon","Tue","Wed","Thu","Fri"]
    def dayinfo(self):
        if self.dayinput in day.dayname:
            print("valid input")
            #self.greeting()
        else:
            print("invalid input")
            self.input= False
    @staticmethod       ## this static method is applid to avoid use of self in defining object method
    def greeting():
        print("Good morning!")

day1=day()
day1.dayinput="Sun"     ## varibales, attributes, property are inerchagiably used in OOP
day1.dayinfo()
#day1.greeting()

day2=day()
day2.dayinput="Sunday"
day2.dayinfo()
#day2.greeting()