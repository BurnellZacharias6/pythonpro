class Student:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def age1(self):
        return self.__age

    @age1.setter
    def age1(self, age):
        if age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = age

stu= Student("Alice", 20)
print(stu.name)  # 输出: Alice
print(stu.age1)  # 输出: 20
stu.set_age = 25  # 设置年龄
print(stu.age1)  # 输出: 25