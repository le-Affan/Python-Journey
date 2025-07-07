class Students:

    graduation_year=2027
    program="AI&DS"
    student_count=0

    def __init__(self,name,roll_number):
        self.name=name
        self.roll_number=roll_number
        Students.student_count+=1

s1=Students("Affan","16014223006")
s2=Students("Ankon","16014223014")
s3=Students("Anjali","16014223012")

print(f"The {Students.program} batch of {Students.graduation_year} has {Students.student_count} students")
print(f"{s1.name}:{s1.roll_number}")
print(f"{s2.name}:{s2.roll_number}")
print(f"{s3.name}:{s3.roll_number}")
