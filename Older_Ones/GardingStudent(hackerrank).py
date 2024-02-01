def gradingStudents(grades):
    list = []
    for i in grades:
        if i % 5 > 2 and i > 35:
            list.append(i+(5-(i % 5)))
        else:
            list.append(i)
    return list


print(gradingStudents([4, 6, 34, 54, 73, 65, 76, 5645, 45, 62]))
