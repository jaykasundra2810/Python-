# lis1 =['Jay', 'Saurabh', "Karan", 'Vasu']
# lis1 = [['Jay', 22], ['Saurabh',22], ['Karan', 21], ['Vasu',20]]
# dic1= dict(lis1)

# for a,b in dic1.items():
#   print(a,b)
# for a in dic1:
#   print(a)

lis1 = ['Jay', 22, 'Saurabh', 23, 'Karan ', 21, 'Vasu', 19]

for a in lis1:
    if str(a).isnumeric() and a > 6:

        print(a)


