# Criei uma lista
# media = []
# for i in range(3):
#     height = input("Informe a altura em cm: ")
#     media.append(height)
# print(media)

student_heights = input("Input a list of studant heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = (student_heights[n])
print(student_heights)

media = 0
for height in student_heights:
    media = media + int(height)
average_height = round(media / (n + 1))
print(average_height)


### RESOLUCAO PROPOSTA
# tota_height = 0
# for height in student_heights:
#     # tota_height = tota_height + (height)
#     tota_height += height
# print(tota_height)

# number_of_student = 0
# for student in student_heights:
#     # tota_height = tota_height + (height)
#     number_of_student += 1
# print(number_of_student)

# average_height = round(total_height / number_of_student)

# average_height = round(tota_height / number_of_student)
# print(average_height)

### OUTRA RESOLUCAO SEM LAÇO FOR
# total_heights = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_heights / number_of_students)
# print(average_height)