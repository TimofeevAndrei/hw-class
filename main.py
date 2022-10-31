class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __agrade(self, grades):
        count = 0
        _sum = 0
        for key in grades:
            count += 1
            _sum += grades[key]
        return round(_sum/count, 1)

    def rate_lc(self, lecturer, course, grades):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grades]
            else:
                lecturer.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        course_p = ", ".join(self.courses_in_progress)
        course_f = ", ".join(self.finished_courses)
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.__agrade(self.grades)}'
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

    def __agrade(self, grades):
        count = 0
        _sum = 0
        for key in grades:
            count += 1
            _sum += grades[key]
        return round(_sum/count, 1)

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.__agrade(self.grades)}')
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grades):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grades]
            else:
                student.grades[course] = [grades]
        else:
            return 'Ошибка'

    def __str__(self):
        res = (f'Имя: {self.name}\nФамилия: {self.surname}')
        return res

one_reviewer = Reviewer('Фреди', 'Крюгер')
two_reviewer = Reviewer('Джейсон', 'Стетхем')
print(one_reviewer)
print()
print(two_reviewer)
print()

one_lecturer = Lecturer('Олег', 'Булыгин')
one_lecturer.courses_attached = ['Git']
one_lecturer.grades = {'Class': 10, 'OOP': 10, 'Function': 10}

two_lecturer = Lecturer('Махрипа', 'Харипулавена')
two_lecturer.courses_attached = ['Git']
two_lecturer.grades = {'Class': 10, 'OOP': 10, 'Function': 10}
print(one_lecturer)
print()
print(two_lecturer)
print()

one_student = Student('Андрей', 'Тимофеев', 'Male')
one_student.finished_courses = ['Введение в програмирование']
one_student.courses_in_progress = ['Python', 'Git']
one_student.grades = {'Basic_python': 10, 'English': 8, 'Function': 9}

two_student = Student('Иван', 'Михалыч', 'Male')
two_student.finished_courses = ['Введение в програмирование']
two_student.courses_in_progress = ['Python', 'Git']
two_student.grades = {'Basic_python': 9, 'English': 6, 'Function': 7}
print(one_student)
print()
print(two_student)






