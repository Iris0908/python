
n = int(input("Please input your number:\n"))
q = n
a = []
while(q != 0):
    a.append(int(q % 2))
    q = int(q / 2)
    
print("Lenth: ", len(a))
#for index in range(1,len(a)):
#    print (a[index])
print(a)
