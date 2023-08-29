# for i in range(8):
#     print(i)
# else:
#     print("Sorry No i")


for i in range(8):
    print(i)
    if i == 4:
        break
else:
    print("Sorry No i") # else simply means full loop are executed 

for x in range(5):
    print("Iteration no {} for loop".format(x+1))
else:
    print("Loop are executed")
print("Out of loop")