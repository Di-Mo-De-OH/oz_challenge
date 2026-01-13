class Eagle:
    
    def __init__(self,name,kind,age):
        self.name = name
        self.kind = kind
        self.age = age
    
    def introduce(self):
        print(f"hi my name is {self.name} and i'm {self.kind}, my age is {self.age}")