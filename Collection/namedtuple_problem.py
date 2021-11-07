from collections import namedtuple
no_of_students = int(input())
Student = namedtuple('Student', input())
total = 0
for _ in range(no_of_students):
    c1 = Student(*input().split())
    total += int(c1.MARKS)
print(total/no_of_students)
