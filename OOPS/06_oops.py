###############################################################################
############ OOPS program for railway reservations using class ################
## 1#######

class reservation:
    train="Rajdhani Express 2510"
    type="passenger"
    seats=25
    def enquiry(self):
        trainname=self.train
        traintype=self.type
        trainseats=self.seats
        print(f"Train {trainname} and available seats are {trainseats}" )
    def reserve(self):
        print(f"Your ticket #seat no {self.seats} have booked successfully")
        self.seats-=1
    def cancel(self):
        print(f"Your ticket #seat no {self.seats} booking cancelled successfully")
        self.seats+=1
        
# r=reservation()
# r.enquiry()
# r.reserve()
# r.enquiry()
# r.cancel()
# r.enquiry()

############ OOPS program for railway reservations using class ################
## 2#######

class railway:
    info="Indian Railway Reservation System"
    def __init__(self,name,seats,type, fare):
        print("Train initiated successfully...")
        self.name=name
        self.seats=seats
        self.type=type
        self.fare=fare
                
        ### Generate no of seats
        self.myseats=list()
        for i in range(1,self.myseats):
            self.myseats.append(i)
        print(f"Seats generated successfully\n{self.myseats}")

    def info(self):
        print(f"Train Name: {self.name}\nSeats: {self.seats}\nType:{self.type}\nFare:{self.fare}")
        self.availabeseats()
    def bookticket(self,seatNo):
        if self.seats>0:
            if seatNo in self.myseats:
                print(f"Ticket booked seat no. {str(seatNo)} successfully!")
                self.myseats.remove(seatNo)
                self.seats-=1
            else:
                print("Seat is already booked")
        else:
            print("Sorry! Seats not available")
            
    def cancelticket(self,seatNo):
        if seatNo not in self.myseats:
            self.myseats.append(seatNo)
            print(f"Ticket cancelled {seatNo} successfully!")
            self.seats+=1
        else:
            print("seat not booked")
    
    def availabeseats(self):
        print(f"Available seats are: \n {self.myseats}")

r=railway("Train1",10,"passenger",450)
print("-"*25)
for count in range(20):
    print(f"****************Count remaining is: {20-count} *************")
    option1=input("Select following options:\n[T]Train information\n[B] For New Ticket Booking\n[C] cancel existing ticket\n[L] For list of available tickets").upper()
    if option1=='T':
        r.info()
    elif option1=='B':
        r.bookticket(int(input("Enter seat no which you want to book: ")))
    elif option1=='C':
        r.cancelticket(int(input("Enter seat no which you want to cancel: ")))
    elif option1=='L':
       r.availabeseats()
    else:
        print("Oops! Invalid option selected, Try again")
