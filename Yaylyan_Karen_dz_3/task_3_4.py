def thesaurus_adv(*args):
    employee_name = {}

    for arg in args:
        name, surname = arg.split()
        if (surname[0] in employee_name
                and name[0] in employee_name[surname[0]]):
            employee_name[surname[0]][name[0]].append(arg)

        elif surname[0] in employee_name:
            employee_name[surname[0]][name[0]] = [arg]

        else:
            employee_name[surname[0]] = {name[0]: [arg]}

    return employee_name


employees = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                          "Илья Иванов", "Анна Савельева")
print(dict(sorted(employees.items(), key=lambda name: name[0])))
