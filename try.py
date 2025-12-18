class Person:
    def __init__(self,name):
        self.name=name



class Student(Person):
    def __init__(self, name,roll,clas):
        Person.__init__(self,name)
        self.roll=roll
        self.clas=clas
    

class Teacher:
    def __init__(self,name,id):
        self.name=name
        self.id=id
        

st=Student('Awal','639161','eight')

print(st.name)
print('hey')
        








