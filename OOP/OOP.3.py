class Human:
    def __init__(self,first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

   # добавьте метод awake, который выводит сообщение 'Я просыпаюсь в 8 утра'
   # переопределите метод sleep для классов Teacher и Student

   
    def awake(self):
        print('Я просыпаюсь в 8 утра')

    def eat(self):
        print('I am eating')

    def sleep(self):
        print('Я ложусь в 10 вечера')


class Teacher(Human):
    
    def __init__(self, first_name, last_name, age, sex, subject):
        super().__init__(first_name, last_name, age, sex)
        self.subject = subject

    def teach(self,group):
        print('f Учит группу {group}')

    def awake(self):
        print('Я просыпаюсь в 6  утра')
        
    def sleep(self):
        print('Я ложусь в 12 ночи')

class Teacher:
    def __init__(self, name):
        self.name = name
        
    def check_homework(self, student_name, subject):
        print(f'Проверил домашнее задание по {subject} студента {student_name}')

    

class Student(Human):
    def __init__(self, first_name, last_name, age, sex, course, group, speciality):
        super().__init__(first_name, last_name, age, sex)
        
        self.course = course
        self.group = group
        self.speciality = speciality

    def study(self, teacher_first_name, teacher_subjest):
        print(f'Учит {teacher_subjest} у {teacher_first_name}')

    
    def awake(self):
        print('Я просыпаюсь в  7 утра')

    def sleep(sleep):
        print('Я ложусь в 2 ночи')

class Student:
    def __init__(self, name):
        self.name = name

    def submit_hemework(self, subject):
        print(f'Сдал домашнее задание по {subject}')
        


    

human = Human('Raxat', 'M', 30, 'femele')
student = Student('Venera', 'Sh',  36, 'femele', 1,'A', 'Computer Science')
teacher = Teacher('Nyriya', 'J', 30, 'femele', 'desember')
teacher.teach(student.group)
teacher.teach('Б')
teacher.teach('В')

student.study('Аида', 'Физика')
student.study('Бермет', 'Физика')
student.study(teacher.first_name, teacher.subject)

student= Student('Бермет')
teacher = Teacher('Асанова')

student.submit_hemework('Математика')
teacher.check_homework('Бермет', 'Математика')


human.eat()
student.eat()
teacher.eat()

human.sleep()
student.sleep()
teacher.sleep()

human.awake()
student.awake()
teacher.awake()



