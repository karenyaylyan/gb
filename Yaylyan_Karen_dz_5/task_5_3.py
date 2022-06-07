def klass_gen(tutors, klasses):
    border = 0
    for tutor, klass in zip(tutors, klasses):
        yield tutor, klass
        border += 1
    if len(tutors) > len(klasses):
        for i in range(border, len(tutors)):
            yield tutors[i], None


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

tutor_klass = klass_gen(tutors, klasses)
print(type(tutor_klass))

for x in tutor_klass:
    print(x)
