#cente method
# name="Sujal Bochkar"
# print(name.center(len(name)+6,"*")) #output - ***Sujal Bochkar***

name1=input("Enter Your Name: ")
num = input("Enter the number of charcters yoy Want to print : ")
char= input("Enter the character you want to print left and right: ")
print(name1.center(len(name1)+int(num),char))