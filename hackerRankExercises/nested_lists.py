# Given the names and grades for each student in a class of  students, 
# store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

# Note: If there are multiple students with the second lowest grade, 
# order their names alphabetically and print each name on a new line.

# Example

# The ordered list of scores is , so the second lowest score is . There are two students with that score: . Ordered alphabetically, the names are printed as:

# alpha
# beta

records = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    records.append([name,score])
scores = sorted({stud[1] for stud in records})
second_lowest = scores[1]

second_lowest_studs = [name for name, score in records if score == second_lowest]

for name in sorted(second_lowest_studs):
    print(name)