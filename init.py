class student:
    school="ABC School"
    
    def __init__(self,name,course):
       # print("Created a new object is ")
        #print(self)
        self.name= name
        self.course= course
        print(self.name)
        print(self.course)
        
student1= student("Jubi","BBALLB")# init metho is always operating while making an object in a class 
print(student1.name)
print(student1.course)

student2= student("Prabal","Btech")
print(student2.name)
print(student2.course)
