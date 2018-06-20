# OOP: Object Oriented Programming

'''
// Java:
public class Human {
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


class Human(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name)
        print(self.age)


tom = Human('Tom', 18)
tom.print_info()

