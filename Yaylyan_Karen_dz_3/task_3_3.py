def thesaurus(*args):
    employee_name = {}

    for arg in args:
        if arg[0] in employee_name:
            employee_name[arg[0]].append(arg)
        else:
            employee_name[arg[0]] = [arg]

    return employee_name


employees = thesaurus("Мария", "Илья", "Петр", "Иван")
print(dict(sorted(employees.items(), key=lambda name: name[0])))
