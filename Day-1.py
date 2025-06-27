#Create a file called practice.txt and write 3 lines into it.
#Read and print the contents of practice.txt.
#Append a new line to practice.txt and read it again.
#Read practice.txt line by line using a loop.
#Try opening a file that doesn’t exist and handle it using a try-except.

with open("practice.txt","w") as file:
    file.write("This is Line 1.\n")
    file.write("This is Line 2.\n")
    file.write("This is Line 3.\n")

with open("practice.txt","a") as file:
    file.write("This is Line 4 which has been appended.\n")

with open("practice.txt","r") as file:
    content=file.read()
    print(content)

with open("practice.txt","r") as file:
    for line in file:
        print(line.strip())

#this above sort of simple loop is better since it doesnt load the entire file onto
#the memoery and rather goes line by line unlike readline() function

try:
    with open("random.txt","r") as another_file:
        content= another_file.read()
except FileNotFoundError:
    print("The requested file does not exist")
