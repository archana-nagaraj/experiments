class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def domath(self, num1, num2):
        #self.num1 = num1
        #self.num2 = num2
        result = num1 + num2
        print("here is the result :"+str(result))


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys  

    def domath(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        result = num1 - num2 
        print(result) 
     
#billy_cyrus = Parent("Cyrus", "blue")
#print(billy_cyrus.last_name)


miley_Cyrus = Child("Cyrus", "Blue", 4)
print(miley_Cyrus.last_name)
print(miley_Cyrus.number_of_toys)
miley_Cyrus.domath(13,10)