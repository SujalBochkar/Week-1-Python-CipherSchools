x , y =input("Enter the name and the single character from it: " ).split(",")
print(len(x))
# print(x.lower().count(y.lower()))
# print(x.upper().count(y.upper()))
print(x.strip().lower().count(y.strip().lower()))

# if we want to remove the spaces
# x.strip().lower().count(y.strip().lower())
# y.strip().lower()