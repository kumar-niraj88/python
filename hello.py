# !print("hello world!")
"""
name = "niraj"
age = 24
# print(name)  niraj 
# print(age)  24

name  = "kumar"
age = 24.0  #re iniliaze
is_adult = True
print(age)


#exercise 

#add a person with name tony Stark 
# tony's age is 51 yrear old 
# tony is a genius

"""
"""
first_name = "tony "
last_name = "Stark"

age = 51 

is_genius = True

print(first_name + last_name)
print(age)
print(is_genius)
"""

# ******************************************

# !for taking the input 
"""
name = input("what is ypur name? : ")
print("Hello " + name)


# Exercise



#tony is secretly a superhero . ask him for this super
#hero name & show it on the terminal


superHeroName = input(" hey tony , what is your Super Hero Name? : ")
print("wow this is your SuperHero Name :" + superHeroName)


# !Types Conversion in py

old_age = input("enter your old age : ")

new_age = int(old_age) + 2 # types converson

"""

# !adding the two number
"""
fNumber = input("Enter the first number :")
lNumber = input("Enter the second number :")

sum = int(fNumber)+ int(lNumber)

print("the sum of the both number : " + str(sum))

"""
# !to upper case & lower --> will not change the original string

name = "Niraj"

print(name.upper()) # "NIRAJ"
print(name.lower()) #  "niraj"
print(name)     # Niraj


# to find the the character ot substring
# !find(character or substring)  --> if not return -1
my_name = "Niraj Kumar"
# zero based index
print(my_name.find('n')) # -1
print (my_name.find('N')) # gives the partiular index like N --> 0
print(my_name.find("Kumar"))  # 6 --> start from 6
print(my_name.find("Kumarr"))  # -1 --> all are not matching

# !replace 

print(my_name.replace("Kumar" , "yadav")) # --> not effect the orignal String --> substring
#Niraj yadav  <-- o/p
print(my_name.replace('N' , 'Y')) # --> for character
#Yiraj Kumar  <-- o/p

# for finding the particular character or substring
# ! in keywords

city = "Chennai"
print('C' in city)  # True
print('c' in city)  # False
print("nn" in city)  # True

# ! operator

print(5*2)   # 10
print(5/2)   # 2.5
print(5//2)  # 2  <-- gives only integer for use double //
print(5+2)   # 7
print(5-2)   # 3
print(5%2)   # 1
print(5**2)   # 25 <-- 5 * 5  <-- power

result = 2 + 3 * 5
print(result)  # 17

#!or --> in py written as word 
#! and --> in py written as word
#!not  --> in py written as word but we also used !=

print(not 3>2) # False buz of not
print(not 2==2) # False buz of not
print(2!=2) # False 


# ! if block 
"""
age = 5
if age>=18:
    print("you are an adult")
    print("you can vote")
elif age < 18 and age > 3:
    print("you are in school")
else:
    print("you are kids")
"""
# !calcuter
"""
frist = input("enter frist number : ")
operator = input("enter operator(+ , - , * , / , %) : ")
second = input("enter the second number : ")

frist = int(frist)
second = int(second)

if operator == "+":
    print(frist + second)
elif operator == "-":
    print(frist - second)
elif operator == "*":
    print(frist * second)
elif operator == "/":
    print(frist / second)
elif operator == "%":
    print(frist % second)
else:
    print("Invlid input")

"""
# ! range()

number = range(5) # 0 ,1,2,3,4
print(number)  #range(0,5) sequnce of number

# ! loop

# ! while
"""
i = 1
while i <= 5 :
    print(i)
    i = i+1  #update

"""
i = 1
while i <= 5 :
    print(i * "*") # i will mutipli the string with i --> print that much of time
    i = i+1  #update

i = 5
while i >=0 :
    print(i * "*")
    i = i-1  #update

#! for

for i in range(5):
    print(i)

# ! list[]

marks = [ 78,90,45 , "niraj"]
print(marks)  # [ 78,90,45 , "niraj"]
print(marks[0]) # 78
print(marks[-1]) # niraj
print(marks[0:2]) #[78, 90]


for score in marks:
    print(score) # one by one printing
score = [88 , 44, 89, 39]

# !append -->  add in the last

score.append(100)
print(score)  # [88, 44, 89, 39, 100]

#! if we want to add in between so used 
#! insert(idx , value)

print(score.insert(0,200))  # None
print(score) #[200, 88, 44, 89, 39, 100]

print(len(score)) #len of the score --> 6

score.clear() #--> used to clear the data of the score --> []
print(score)

# ! break and countinue
"""
students = ["niraj" , "manav" , "suraj" , "nasim", "anish"]

for student in students:
    if student == "suraj":
        break;  # if find the then break
    print(student)

for student in students:
    if student == "suraj":
        continue  #skip  the suraj name
    print(student)
"""
    #!tuple ()--> immutable --> not reinilize
    #! not need to write it is optional 
    # like person = "ram" , "mohan" , "ramesh"
"""
marks = (95,68,98,56,56,56,56)

print(marks.count(56)) # 4
print(marks.index(56)) # 3 buz it takes the frist time

"""
#! set{}

"""
unorder --> to store 
not duplicate element are allows
here not a idx concept thats we call as unOrder

"""

marks ={95, 98 , 97,97, 97}

print(marks)


#! Dictionaries
"""
to store in key and value pairs
possible to access to the help of idx 
"""
"""
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# to printing the value
print(thisdict["brand"])  # ford

# to adding the value
thisdict["price"] = "5cr"
print(thisdict)

# for changing the value
thisdict["price"] = 3456787654
print(thisdict)

"""

#!function 
