import functions

def main():

    print("Здравствуйте.")
    print("Введите номер студента")
    student_number = int(input())
    student = functions.get_student_by_pk(student_number)

    if student is None:
        print("У нас нет такого студента")
        return
    full_name_student = student["full_name"]
    skills_student = " ".join(student["skills"])
    learns_student = " ".join(student["learns"])

    print(f"Студента {full_name_student}")
    print(f"Знает: {skills_student}")
    print(f"Хочет изучить: {learns_student}")
    print(f"Выберите специальность для оценки студента {full_name_student}")
    profession_title = input()
    profession = functions.get_profession_by_title(profession_title)

    if profession is None:
        print("У нас нет такой специальности")
        return

    students_skills = set(student["skills"])
    profession_skills = set(profession["skills"])

    "Присвоиение переменной match функция которая возвращает данные в виде словаря"
    match = functions.check_fitness(students_skills, profession_skills)
    "присвоение переменной percent_fit_student результата совпадения % навоков студента и профессии"
    percent_fit_student = match["percent_fit"]
    student_knows = " ".join(match["has"])
    student_lacks = " ".join(match["lacks"])

    "Выводим информацию  после анализа знаний студента и необходимых навоков для специальности "
    print(f"Пригодность на - {percent_fit_student}%")
    print(f"{full_name_student} знает {student_knows}")
    print(f"{full_name_student} не знает {student_lacks}")
main()