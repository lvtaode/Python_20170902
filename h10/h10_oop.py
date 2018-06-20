# OOP: Object Oriented Programming

'''
// Java:
public class Human extends Object {
  private String name;
  private int age;

  public Human(String name, int age) {
    this.name = name;
    this.age = age;
  }

  public void printInfo() {
    System.out.println(this.name);
    System.out.println(this.age);
  }
}
'''


class Human:

    # self 是 Python 类中所有函数的第一个参数
    # 调用函数时，不用给 self 传值
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)


tom = Human('Tom', 18)
tom.print_info()

print(tom.name)
print(tom.age)

print(tom)

jerry = Human('Jerry', 18)

print(jerry)

print(Human)
