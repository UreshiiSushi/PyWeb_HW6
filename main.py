import sqlite3
from datetime import datetime
from random import randint, choice

from faker import Faker

from create_db import create_db

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 3
NUMBER_COURSES = 8
NUMBER_TEACHERS = 5
NUMBER_GRADES = 1000


def gen_mock_data(num_st: int, num_te: int, num_grd: int) -> tuple:
    students = []
    groups = ["OMT-96-1", "OMT-99-2", "PTM-12-1"]
    teachers = []
    courses = [
        "Бази даних",
        "Креслення",
        "Матан",
        "Українська мова",
        "Англійська мова",
        "Економіка",
        "Теормех",
        "Металографія",
    ]
    grades = []

    fake_data = Faker("uk-UA")
    Faker.seed(0)

    for _ in range(num_st):
        students.append((fake_data.first_name_nonbinary() +
                        " " + fake_data.last_name()))

    for _ in range(num_te):
        teachers.append((fake_data.first_name_nonbinary() +
                        " " + fake_data.last_name()))

    for _ in range(num_grd):
        grades.append(randint(1, 101))

    return students, groups, teachers, courses, grades


def prep_data(raw_st, raw_gr, raw_te, raw_crs, raw_grd) -> tuple:

    groups = []
    teachers = []
    students_learn = []
    studyes = []
    grades = []

    for gr in raw_gr:
        groups.append((gr,))

    for te in raw_te:
        teachers.append((te,))

    for st in raw_st:
        students_learn.append((st, randint(1, NUMBER_COURSES)))

    for crs in raw_crs:
        studyes.append((crs, randint(1, NUMBER_TEACHERS)))

    for grd in raw_grd:
        grades.append(
            (
                grd,
                datetime(2023, randint(1, 12), randint(1, 28)).date(),
                randint(1, NUMBER_STUDENTS),
                randint(1, NUMBER_COURSES),
            )
        )

    return (students_learn, groups, studyes, teachers, grades)


def insert_to_db(students, groups, courses, teachers, grades) -> None:
    with sqlite3.connect("university.db") as conn:
        cursor = conn.cursor()

        sql_to_groups = "INSERT INTO groups(name) VALUES (?)"
        cursor.executemany(sql_to_groups, groups)

        sql_to_teachers = "INSERT INTO teachers (name) VALUES (?)"
        cursor.executemany(sql_to_teachers, teachers)

        sql_to_students = "INSERT INTO students (name, group_id) VALUES (?, ?)"
        cursor.executemany(sql_to_students, students)

        sql_to_studyes = "INSERT INTO studyes (name, teacher_id) VALUES (?, ?)"
        cursor.executemany(sql_to_studyes, courses)

        sql_to_grades = "INSERT INTO grades (grade, date, student_id, study_id) VALUES (?, ?, ?, ?)"
        cursor.executemany(sql_to_grades, grades)

        conn.commit()


if __name__ == '__main__':
    create_db()
    data = prep_data(*gen_mock_data(NUMBER_STUDENTS, NUMBER_TEACHERS, NUMBER_GROUPS))
    insert_to_db(*data)
