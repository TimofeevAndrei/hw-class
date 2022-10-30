class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lc(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        course_p = ", ".join(self.courses_in_progress)
        course_f = ", ".join(self.finished_courses)
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.grades}'
        f'\nКурсы в процессе изучения: {course_p}\nЗавершенные курсы: {course_f}')
        return res


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.grades}')
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res

one_reviewer = Reviewer('Freddy', 'Kruger')
two_reviewer = Reviewer('Frodo', 'Beggins')
print(one_reviewer)
print()

one_lecturer = Lecturer('Oleg', 'Buligin')
one_lecturer.courses_attached = ['Git']
print(one_lecturer)
print()

one_student = Student('Andy', 'Tim', 'Male')
one_student.finished_courses = ['Введение в програмирование']
one_student.courses_in_progress = ['Python', 'Git']
print(one_student)






