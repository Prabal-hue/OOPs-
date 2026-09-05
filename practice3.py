# Creat class students that takes 3 marks and has a method average().

class Student:
    def __init__(self, name, listOfmarks):
        self.name=name
        self.listOfmarks= listOfmarks
        
    def average(self):
        sum=0
        for eachValue in self.listOfmarks:
            sum= sum+eachValue
        average=  sum/3  
        
        print("Average of each value:", average)
        
Student1= Student("Prabal",[90, 98, 99])        
Student1.average()