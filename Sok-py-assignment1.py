#select number of courses
num_of_courses = int(input("How many courses did you finish?"))



#counter of courses
counter = 1
course_mark = []
while int(counter) <= num_of_courses:
    course_mark.append(float(input(f"Enter your mark for Course {counter}:")))
    counter +=1

#Array loops
for elem in course_mark:
    print(elem)

#totals
total = 0
for number in course_mark:
    total = total + number
    

#average calculation
avg = 0
for num in course_mark:
    avg = total/num_of_courses
result = input(f"Your average for your {num_of_courses} courses is:  {avg}")

average = round(total/num_of_courses,2)

#print(f"Your average for your {num_of_courses} courses is: {average}")


#average calculator
if avg >= 90  and avg <= 100:
    print("your grade is A++")
if avg >= 80 and avg <=89:
    print("your grade is B++")
if avg >= 70 and avg <=79:
    print("your grade is C+")
if avg >= 60 and avg <= 69:
    print("your grade is D")
if avg < 60:
    print("your grade is F")