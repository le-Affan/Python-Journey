# Create a dictionary with 3 student names as keys and their Roll No. as values.
# Add a new student to the dictionary.
# Update the Roll no. of one student.
# Print all the keys and values from the dictionary.
# Remove one student from the dictionary.


students = {"Affan":4,
            "Ankon":14,
            "Anjali":12}

students["Aish"]=7

students["Affan"]=6

print("Keys: ",list(students.keys()))
print("Values: ",list(students.values()))
print("Items: ",list(students.items()))
print(students)

students.pop("Affan")


