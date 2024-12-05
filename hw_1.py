class Person:
    def __init__(self,fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):#информация о человеке
        return (f' Меня зовут {self.fullname}, '
              f'мне {self.age}, '
              f'я {self.is_married}')



class Student(Person):
    def __init__(self,fullname, age, is_married, **marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def get_average(self):#средняя оценка
        average = sum(self.marks.values())/len(self.marks)
        return(f'средняя оценка: {average}')



class Teacher(Person):

    base_salary = 30000#зарплата

    def __init__(self,fullname, age, is_married,expirience):
        super().__init__(fullname, age, is_married)
        #expirience будем считать в годах работы, стаж проще говоря
        self.expirience = expirience

    def up_of_salary(self):#прибавка к зп в завис.от стажа
        if self.expirience > 3:
            Teacher.base_salary += Teacher.base_salary*0.05*(self.expirience-3)
            return(f"текущая зп с учетом повышения: {Teacher.base_salary}")

        else:
            return("ваш опыт работы меньше 3 лет")

#вся информация про учителя
bakytbek = Teacher("Болот", 21, "не женат", 7)
print(bakytbek.introduce_myself())
print(bakytbek.up_of_salary())


def create_students():#информация об учениках

    first_st = Student("Макс", 20, "не женат",
                       math=5,phylosophy=5, physic=5, geometry=5)
    second_st = Student("Калыс", 20, "не женат",
                       math=2, phylosophy=5, physic=2, geometry=3, history=3)
    third_st = Student("Назар", 20, "не женат",
                       biology=5, english=4, physic=4, geometry=5, literature=4, kyrgyz=5)
    students_list = [first_st,second_st,third_st]

    return students_list

student_list = create_students()
for student in student_list:
    print(f"{student.introduce_myself()},\n мои оценки {student.marks}, {student.get_average()}")


