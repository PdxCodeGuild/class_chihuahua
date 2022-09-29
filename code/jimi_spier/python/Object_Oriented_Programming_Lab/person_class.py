# Jimi Spier
# person_class.py
# 20220923

# ----------------------Class------------------------------------------- #
class Person:
    # ----------------------Constructor------------------------------------- #
    def __init__(self, name, age):      #Constructor sets prototype for Person class
        self.name = name
        self.age = age
    
    # ----------------------Method------------------------------------------ #
    def school_section(self, section):  #Polymorphs class to add school section
        self.section = section 
         
    # ----------------------Method------------------------------------------ #
    def display(self): #Outputs data to console when invoked
        return f"\n {self.name} is {self.age}. {self.name} is currently a {self.section} "
              
# ----------------------Data-Collect/Calls-------------------------------#
prs1 = Person("Jill", 20)               # Instantiation and details for prs1
prs2 = Person("Mitch", 21)              # Instantiation and details for prs2
prs3 = Person("Jimi", 45)               # Instantiation and details for prs3

# ----------------------Data-Collect/Calls-------------------------------#
prs1.school_section("Freshman")         # Adding school section to prs1
prs2.school_section("Sophomore")        # Adding school section to prs2
prs3.school_section("Knowledge Junkie") # Adding school section to prs3

# ----------------------Output-to-Console--------------------------------#
print(Person.display(prs1))             #Sending data about to the console about prs1
print(Person.display(prs2))             #Sending data about to the console about prs2
print(Person.display(prs3))             #Sending data about to the console about prs3
