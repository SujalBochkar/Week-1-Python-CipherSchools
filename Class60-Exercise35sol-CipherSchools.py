x = input("Enter the name: ")
x.lower()
a = 0
i = 0
while i < (len(x)):
    print(f"{x[i]} : {x.count(x[i])}")
    i = i + 1
