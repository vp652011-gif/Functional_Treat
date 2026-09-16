print("Functional Treat")

marks = [21, 35, 37, 40, 45, 50, 52, 55, 58, 60, 65, 70, 72, 79, 80, 84, 87, 92, 97, 100]


totalstudent = len(marks)
highest = max(marks)
lowest = min(marks)
totalmarks = sum(marks)
average = totalmarks / totalstudent

passed = 0
failed = 0

for mark in marks:
    if mark >= 40:
        passed = passed + 1
    else:
        failed = failed + 1

hundred = marks.count(100)

passpercentage = (passed / totalstudent) * 100
print("Total Student:", totalstudent)
print("Highest Marks:", highest)
print("Lowest Marks:", lowest)
print("Average Marks:", average)
print("Passed Student:", passed)
print("Failed Student:", failed)
print("Pass Percentage:", passpercentage) 

ascending = sorted(marks)
descending = sorted(marks, reverse=True)

print("Sorted Marks:", ascending)
print("Descending Marks:", descending)

secondhighestmark = descending[1]
secondlowestmark = ascending[1]

print("Second Highest:", secondhighestmark)
print("Second Lowest:", secondlowestmark)


allstudentpassed = all(mark >= 40 for mark in marks)

anystudentfailed = any(mark < 40 for mark in marks)

print("All Students Passed:", allstudentpassed)
print("Any Student Failed:", anystudentfailed)


search = int(input("Enter a mark to search: "))
if search in marks:
    print("Mark exists in the list.")
else:
    print("Mark does not exist in the list.")

A = 0
B = 0
C = 0
D = 0
E = 0
F = 0

for mark in marks:

    if mark >= 90:
        A = A + 1

    elif mark >= 80:
        B = B + 1

    elif mark >= 70:
        C = C + 1

    elif mark >= 60:
        D = D + 1

    elif mark >= 40:
        E = E + 1

    else:
        F = F + 1

print("Grade A:", A, "Students")
print("Grade B:", B, "Students")
print("Grade C:", C, "Students")
print("Grade D:", D, "Students")
print("Grade E:", E, "Students")
print("Grade F:", F, "Students")
