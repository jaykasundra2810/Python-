# i = 0
# while(True):
#     if i < 5:
#         i=i+1
#         continue
#
#     print(i , end=" ")
#     if i == 45:
#         break
#     i=i+1

while(1):
    i = int(input("Enter a number"))
    if i > 100:
        print("Congratulaions you have entered a number greater than 100 ")
        break
    else:
        print("Try again")
        continue
