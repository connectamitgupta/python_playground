class Library:
    def __init__(self,listOfBooks):
        self.books=listOfBooks
    def displayAvailableBooks(self):
        print("Books available in this library are: ")
        for book in self.books:
            print("\t  *"+book)
    def borrowBoks(self,bookName):
        if bookNmae in self.books:
            print(f"You have been issues{bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
        else:
            print("Sorry, this books has alredy been issues to someone")

class Student:
    pass


if __name__=="__main__":
   centralLibrary=Library(["Django","Algorithms","Py notes by Amit"]) 
   centralLibrary.displayAvailableBooks()



        