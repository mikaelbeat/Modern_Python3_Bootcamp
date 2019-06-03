
midterms = [80, 91, 78]
finals = [98, 89, 53]
students = ["Dan", "Angela", "Kate"]

# final_grades = {pair[0]:max(pair[1], pair[2]) for pair in zip(students, midterms, finals)}
# print(final_grades)

grades = zip ( 
    students,
    map(
        lambda pair: max(pair),
        zip(midterms, finals)
    )
)

print(dict(grades))



avg_grades = dict(
    zip( 
        students,
        map(
            lambda pair: ((pair[0] + pair[1]) / 2),
            zip(midterms, finals)
        )
    )
)

print(avg_grades)