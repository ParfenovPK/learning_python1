import json

"функция для импорта данных о студентах из документа students.json"
def load_students():
    with open ("data/students.json", "r") as file:
        data = json.load(file)
    return data

"функция для импорта данных о профессиях из документа professions.json"
def load_professions():
    with open("data/professions.json", "r") as file:
        data = json.load(file)
    return data

"функция получает словарь с данными студента по его pk"
def get_student_by_pk(pk):
    students = load_students()
    for student in students:
        if student["pk"] == pk:
            return student

"функция получает словарь с инфо о профе по названию"
def get_profession_by_title(profession_title):
    professions = load_professions()
    for profession in professions:
        if profession["title"] == profession_title.title():
            return profession

"функция которая получив студента и профессию возвращает данные в виде словаря"
def check_fitness(student, profession):
    has = list(student.intersection(profession))
    lacks = list(profession.difference(student))
    percent_fit = round(len(has)/len(profession)*100)

    return {"has": has, "lacks": lacks, "percent_fit": percent_fit}
