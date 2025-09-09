for i in range(1, 11):
    j = 7 * i
    print("7 x", i, "=", j) 

print("this is odd or even ----------------------------------------------")

for i in range(1, 20):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

def dinesh (x,y):
    if x >70:
        if y > 70:
          print("this is working")
        else:
            print("tis isnot")
            dinesh(20,30)

