
#string concatenation
first_name = "Dinesh"
second_name = "tarun"
sir_name = "G"
lol = "he is a boy"
full_name = (first_name + second_name + sir_name)
print (full_name)
#now to give space between dineshtarun and g u have to give space in prgm
full_name2 = (first_name + second_name + " " + sir_name)
print (full_name2)
#sring repetation to print string multiple times 
print (first_name*8)

#next string methods or operations
#lol = he is a boy
print(lol.upper())
print(lol.lower())
print(lol.strip()) #used to remove spaces from string like at the end of front
print(lol.replace("boy","girl")) #replace words 
#to print the length of string 
print(len(lol))
#to print particular letter or string usig index
print(first_name[3])
#to print more 
print(first_name[2:4]) #called slicing 
print(first_name[3:]) #to print the overall
print(first_name[:5])
#can do reverse index alos by using neagative 
print(first_name[:-2])
#to jump and print the sring lettere use this 
print(first_name[::2])
#now this will print one leaving other and vise versa

#escape sequence 
s=("diensh is \n a good boy")
print(s)
#to give tabspace 
d=("tarun is \t a bad boy")
print(d)

#HOME WORK--------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------
#1 simple greeting prgm
print("THIS IS FIRST PRGM")
name = input("Enter your sweet name : ")
age = input("Enter your age : ")
g=("Thankyou for entering the detailes ")
print("here is the preview")
print(g)
print(name , age)

#printing all together 
print(name +" " + age + " " + g )
#using formatted string 
print(f"{name}{age} thankyou for the detailes")

#2 prgrm
print("THIS IS SECOND PRGM")
b = input("Enter the sentence : ")
print(b.upper())
print(b.lower())
print(b.replace(" ","_"))
print(b.strip())

#3 prgrm
print("THIS IS 3RD PRGM")

k = input("Enter the string to calculate the length but ignoaring spaces : ")
h = (k.replace(" ", ""))
print(len(h))

#4 escape sequence prgm

print("hello world \n iam dinesh") #this is to print in new lne 
print("dinesh is a good boy \t tarun is a bad boy ") #to giv tab space between lines 