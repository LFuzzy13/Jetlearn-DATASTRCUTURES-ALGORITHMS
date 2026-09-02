#class practice and testing

#creating the class
class student:

    #creating a constructor (the information)
    def __init__(self,name,age,course,marks): #needs 'self' because its in a class 

        #information
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    #creating methods (actions)
    #display method creation
    def display(self):
        print("\n student details")
        print("name :", self.name)
        print("age :", self.age)
        print("course :", self.course)
        print("marks :", self.marks)

    #method to calculate average marks
    def average(self):
        avg = sum (self.marks)/len(self.marks)#adding all the marks together
        print("Average Mark :", avg)

#creating objects
student1 = student("john johnson", 1250, ["english","maths","science","coding","history"], [94, 23, 40, 87, 12])
student2 = student("brian brianson", 4170, ["english","maths","science","coding","history"], [12, 71, 25, 59,93])
student3 = student("james jameson", 508, ["english","maths","science","coding","history"], [100, 82, 61, 88, 99.9])
student4 = student("pete peterson", 2934, ["english","maths","science","coding","history"], [20, 31, 24, 19,31])

#connecting objects and methods together
student1.display()
student1.average()

student2.display()
student2.average()

student3.display()
student3.average()

student4.display()
student4.average()
