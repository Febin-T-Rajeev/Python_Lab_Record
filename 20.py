class publisher:
    def __init__(self):
        self.name="Prentice Hall"
    def display(self):
        print("publisher:",self.name)

class book(publisher):
    def __init__(self):
        self.title="Core Python Application Programming"
        self.author="Wesley J Chun"
    def display(self):
        super().__init__()
        super().display()
        print("Title:",self.title)
        print("Auther:",self.author)

class python(book):
    def __init__(self):
        self.price="650"
        self.pages="1136"
    def display(self):
        super().__init__()
        super().display()
        print("Price:",self.price)
        print("No.of pages:",self.pages)


obj2=python()
print("Book Details are:\n")
obj2.display()
