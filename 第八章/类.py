class Student:
    school='修帝学学院'

    def __init__(self,name,age):
        print('init')
        self.name = name
        self.age = age

xiaoming = Student('张三',18)
xiaozhang = Student('李四',20)
print(xiaoming.name)
print(xiaozhang.age)
print(Student.school)