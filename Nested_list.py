
#n = int(raw_input())

#name = raw_input()
#score = float(raw_input())
#marksheet = [[name,score ] for _ in range(n)]
##print marksheet
#marksheet.sort()
#marksheet.remove(min(marksheet))
#print min((marksheet))
N = int(raw_input())
students = []
for i in xrange(N):
    grade = [raw_input(), float(raw_input())]
    students.append(grade)
students = sorted(students, key=lambda x: x[1])
second_highest = students[0][1]
for name, grade in students:
    if grade > second_highest:
        second_highest = grade
        break
print('\n'.join([name for name, grade in sorted(students) if grade == second_highest]))