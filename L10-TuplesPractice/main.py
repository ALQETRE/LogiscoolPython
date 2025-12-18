#  (student_idx, student_score)

# Input scores

scores = [ (0, 70), (1, 64), (2, 34) ]

# Student 1 = 70
# Student 2 = 64
# Student 3 = 34


# scores = ()
# for idx in range(3):
#     score = int(input(f"Student {idx} = "))
#     student = (idx, score)
#     scores.append(student)
# print(scores)






scores = ((0, 70), (1, 64), (2, 34), (3, 97), (4, 71),
          (5, 83), (6, 92), (7, 52), (8, 79), (9, 44))

# To grades

# 1 = 100% - 90%
# 2 = 90% - 75%
# 3 = 75% - 65%
# 4 = 65% - 50%
# 5 = 50% - 0%

grades = [ (0, 3), (1, 4), (2, 5), (3, 1) ]


grades = []
for student in scores:
    idx, score = student # (0, 70)
    if score >= 90:
        student = (idx, 1)
    elif score >= 75:
        student = (idx, 2)
    elif score >= 65:
        student = (idx, 3)
    elif score >= 50:
        student = (idx, 4)
    else:
        student = (idx, 5)
    grades.append(student)
# print(grades)


print()
print(scores)
print()

# Min/Max
max_score = -1
max_idx = -1

min_score = 101
min_idx = -1

for student in scores:
    idx, score = student

    if score > max_score:
        max_score = score
        max_idx = idx

    if score < min_score:
        min_score = score
        min_idx = idx

print(f"Student {max_idx} had the HIGHEST score of {max_score}%")
print(f"Student {min_idx} had the LOWEST score of {min_score}%")





# Mean score

# You are mean
# Ty jsi zlý

# Mean - Median

1, 4 ,6, 2

# (1 + 4 + 6) / 3 = Mean

# 1, 2, 4, 6 = 2 Median



total_score = 0
for student in scores:
    idx, score = student
    total_score += score
mean = total_score / len(scores)
print(f"The mean of all scores is {mean}%")


# Median grade

only_grades = []
for student in grades:
    idx, grade = student
    only_grades.append(grade)

only_grades.sort()
median = only_grades[len(only_grades)//2 -1]
print(f"The median of all grades is {median}")




# Docházka:
# Všichni online