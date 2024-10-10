print("hello world")

#operators class 4 

# (i) assigning operator 
a = 10
a = a + 100
print(a)

#to write it in simple form use this insted
b = 10
b += 100
print(b)

#or multiply
c = 10
c *= 100

print(c)

#(ii) comparision operator 

c = 10
d = 20
print(a==b)
print(a != b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)

#logical operators 
"""  """
print("This is logoc operators ")
#AND OPE
print(2>1 and 2<1)  #both should be true 

#OR oper
print(not(2<1)) #this is false butstill true cuz of not operator

#OR oper
print(2>1 or 2<1)#any one should be true it will print true

#membership operator 
print("this is membership operator output")

string = ("Dineshtarun g")
print("p" in string) #checks fro p in the string 
print("D" in string) 
print("z" not in string)
string2 = ("yoookloooooooo dinesh is super")
print(("D" in string) and ("d" in string2)) #should print true 
print(("D" in string) or ("d" in string2)) #should again print true cuz one is correct
print(("y"in string))
print(not("y" in string))

print("y" not in string)

#bitwise operator 
print("this is bitwise operator ")
#ill study this i promise :)

# HOMEWORK------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------
print("this is prgrm 1 ")
boi1 = (int(input("Enter the value one : ")))
boi2 = (int(input("Enter the value two : ")))
print(boi1>10 and boi2>10)
print(boi1<5 or boi2<5)
print(not(boi1>10))

#prrm 2 
print("this is prgrm 2 ")
#comparison operator challenge
age = (int(input("Enter the user age : ")))

# since if statement is not working iam gonna use boolean operation and do the sum
print(f"you are adult yoo0! " * int(age>=18) or "you are child")

#prgrm 3 
print("this is 3rd progra : ")
q = input("Namaste")
print("N" in q)

w = input("gowtham is loffar")
print("gowtham" not in w)
print("python"not in w)

#prgrm 4 
print("this is 4th progra :")

#this is bitwise operator that i dono ill read i promise :)