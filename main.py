# Approach 1 ( Use a string to store reversed string and print)
def approach_1(passedString, passedLength):
    a = ""
    for i in range(passedLength - 1, -1, -1):
        a = a + passedString[i]
    print(a)

# Approach 2 (Print the reversed string directly)
def approach_2(passedString, passedLength):
    for i in range(passedLength - 1, -1, -1):
        print(passedString[i], end="")


inputString = input("Enter the string: ")
length = len(inputString)
print("Which approach to reverse the string?")
print("1) Approach 1")
print("2) Approach 2")
print("3) Exit")

while True:
    try:
        choice = int(input("\nChoice:"))
    except ValueError:
        print("Wrong Input")
        continue
    if choice == 1:
        approach_1(inputString, length)
    elif choice == 2:
        approach_2(inputString, length)
    elif choice == 3:
        break
    else:
        print("Wrong Input")
