import math

#ex1
class Shape:
    #those functions will be overwritten
    def print_class_name():
        print("Shape")
    def calculate_area(self):
        pass
    def calculate_perimeter(self):
        pass

class Circle(Shape):
    pi = 3.14159

    def __init__(self, radius):
        if radius < 0:
            return "Error: Radius can't be < 0"

        super().__init__()
        self.radius = radius
        self.diameter = 2 * radius

    def print_class_name():
        print("Circle")

    #the circle doesn't have area
    def calculate_disk_area(self):
        return self.radius * Circle.pi

    def calculate_perimeter(self):
        return 2 * Circle.pi * self.radius

class Rectangle(Shape):
    def __init__(self, height, lenght):
        if height < 0:
            return "Error: Height can't be < 0"
        if lenght < 0:
            return "Error: Length can't be < 0"

        super().__init__()
        self.height = height
        self.length = lenght

    def print_class_name():
        print("Rectangle")

    def calculate_area(self):
        return self.length * self.height

    def calculate_perimeter(self):
        return 2 * self.length + 2 * self.height

class Triangle(Shape):
    def __init__(self, a, b, c):
        if not (a + b > c and b + c > a and c + a > b):
            return "Error: The given edges can't make a triangle"

        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def print_class_name():
        print("Triangle")

    def calculate_area(self):
        semi_parameter = self.calculate_perimeter() / 2
        return math.sqrt(semi_parameter * (semi_parameter - self.a) * (semi_parameter - self.b) * (semi_parameter - self.c))

    def calculate_perimeter(self):
        return self.a + self.b + self.c

#ex2
class Account:
    def __init__(self) -> None:
        self.amount = 0

class SavingsAccount(Account):
    def __init__(self) -> None:
        super().__init__()
        self.interest_rate = 4 #default interest rate
        self.current_package = "Default"
        self.earn = "Yearly"
        self.amount = 1

    def update_package(self, package):
        if not isinstance(package, str):
            return "Error: Please input a valid package"

        if package == "Premium":
            self.earn = "Monthly"
            self.interest_rate = 2
            self.current_package = package

        elif package == "Deluxe":
            self.earn = "Weekly"
            self.interest_rate = 0.7
            self.current_package = package

        elif package == "Default":
            self.earn = "Yearly"
            self.interest_rate = 4
            self.current_package = package

        else:
            return "Error: Please input a valid package"

    def update_interest_rate(self, new_interest_rate):
        if not isinstance(new_interest_rate, (int, float)) or new_interest_rate <= 1:
            return "Error: Please input a valid interest rate"

        if new_interest_rate > 5:
            print("What are you doing!? Trying to make our costumer rich??")
            return None

        self.interest_rate = new_interest_rate

    def calculate_interest(self, years):
        if not isinstance(years, int):
            return "Error: please enter a valid number of years"

        result = self.amount
        while years != 0:
            result = result * self.interest_rate
            years -= 1
        
        return result

    def credit_account(self):
        self.amount = self.amount * self.interest_rate

class CheckingAccount(Account):
    def __init__(self) -> None:
        super().__init__()

    def make_a_deposit(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            return "Error: Please input a valid amount"
        self.amount = self.amount + amount

    def withdraw(self, amount):
        if not isinstance(amount, int) or amount <= 0:
            return "Error: Please input a valid amount"

        if self.amount < amount:
            return "Error: Insufficient founds"

        self.amount = self.amount - amount
        return self.amount

    def transfer(self, amount, account):
        if not isinstance(amount, int) or amount <= 0:
            return "Error: Please input a valid amount"

        if not isinstance(account, Account):
            return "Error: Invalid account"

        if self.amount < amount:
            return "Error: Insufficient founds"

        self.amount = self.amount - amount
        account.amount = account.amount + amount
        return "Success"

#ex3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

class Car(Vehicle):
    def __init__(self, make, model, year, range, fuel_capacity):
        super().__init__(make, model, year)
        self.range = range
        self.fuel_capacity = fuel_capacity

    def calculate_mileage(self):
        return self.range / self.fuel_capacity

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, range, fuel_capacity):
        super().__init__(make, model, year)
        self.range = range
        self.fuel_capacity = fuel_capacity

    def calculate_mileage(self):
        return self.range / self.fuel_capacity

class Truck(Vehicle):
    def __init__(self, make, model, year, horse_power, engine_torqe, weight):
        super().__init__(make, model, year)
        self.horse_power = horse_power
        self.engine_torqe = engine_torqe
        self.weight = weight

    def calculate_towing_capacity(self):
        return self.engine_torqe * self.horse_power / (self.weight / 20)

#ex4
class Employee:
    def __init__(self, name, email, phone_number, salary) -> None:
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.salary = salary

    def raise_salary(self, amount):
        if not isinstance(amount, (int, float)) or amount < 0:
            return "Error: Please input a valid amount"
        self.salary = self.salary + amount

    def __str__(self) -> str:
        result = "{\n"
        result += f"\tName: {self.name};\n"
        result += f"\tEmail: {self.email};\n"
        result += f"\tPhone #: {self.phone_number};\n"
        result += f"\tSalary: {self.salary};\n"
        result += "}"
        return result

class Manager(Employee):
    def __init__(self, name, email, phone_number, salary):
        if not isinstance(salary, (int, float)) or salary < 0:
            return "Error: Please input a valid salary"
        super().__init__(name, email, phone_number, salary)
        self.department = "No assigned department"
        self.employees = []
    
    def assign_to(self, department):
        self.department = department
        print(f"{self.name} is now managing {self.department} department.")

    def hire(self, employee):
        if not isinstance(employee, Employee):
            return "Error: Please input a valid employee"
        self.employees.append(employee)

    def print_employees(self):
        for e in self.employees:
            print(str(e))

class Engineer(Employee):
    def __init__(self, name, email, phone_number, salary, language):
        if not isinstance(salary, (int, float)) or salary < 0:
            return "Error: Please input a valid salary"
        super().__init__(name, email, phone_number, salary)
        self.known_languages = [language]
        self.projects = []

    def assign_to_project(self, project):
        self.projects.append(project)
        print(f"{self.name} is now working on the {project} project")

    def learn_a_new_language(self, language):
        self.known_languages.append(language)

    def print_known_languages(self):
        for l in self.known_languages:
            print(l, end=" ")

class Salesperson(Employee):
    def __init__(self, name, email, phone_number, salary, product_dict):
        if not isinstance(salary, (int, float)) or salary < 0:
            return "Error: Please input a valid salary"
        super().__init__(name, email, phone_number, salary)
        self.product_dict = product_dict

    def add_product_to_stock(self, product, quantity):
        if product not in self.product_dict:
            self.product_dict[product] = quantity
        else:
            self.product_dict[product] += quantity

    def sell_product(self, product, quantity):
        if product not in self.product_dict:
            return "Error: Product isn't in the catalog"
        elif self.product_dict[product] < quantity:
            return "Error: Insufitient stock"
        else:
            self.product_dict[product] -= quantity
            return "Sold"

#ex5
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

class Mammal(Animal):
    def __init__(self, name, habitat, fur_color, num_legs):
        super().__init__(name, habitat)
        self.fur_color = fur_color
        self.num_legs = num_legs

    def run(self):
        return f"{self.name} is running on {self.num_legs} legs."

    def eat(self, food):
        print(f"{self.name} is now eating {food}")

class Bird(Animal):
    def __init__(self, name, habitat, can_fly):
        super().__init__(name, habitat)
        self.lifetime_egg_record = 0
        self.can_fly = can_fly

    def lay_an_egg(self):
        self.lifetime_egg_record += 1

    def fly(self):
        if self.can_fly:
            print(f"{self.name} is now flying")
        else:
            print(f"Give {self.name} a parachute and throw it off the cliff to see want happens")

class Fish(Animal):
    def __init__(self, name, habitat, water_type, is_predator):
        super().__init__(name, habitat)
        self.water_type = water_type
        self.is_predator = is_predator

    def explore(self, water_type):
        if water_type != self.water_type:
            print(f"{self.name} died because it couldn't swim int the {water_type} water")
        else:
            print(f"{self.name} explored some unknown territory")

    def hunt(self, fish):
        if self.is_predator:
            print(f"{self.name} succesfully hunted {fish}")
        else:
            print(f"{self.name} returned hungry because it ran all day from a predator")

#ex6
class LibraryItem:
    def __init__(self, title, author, item_id):
        self.title = title
        self.author = author
        self.item_id = item_id
        self.checked_out = False

    def check_out(self):
        if self.checked_out:
            print(f"{self.title} is already checked out.")
        else:
            self.checked_out = True
            print(f"{self.title} has been checked out.")

    def return_item(self):
        if self.checked_out:
            self.checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is not checked out.")

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Item ID: {self.item_id}")
        print(f"Checked Out: {self.checked_out}")

class Book(LibraryItem):
    def __init__(self, title, author, item_id, num_pages):
        super().__init__(title, author, item_id)
        self.num_pages = num_pages

    def display_info(self):
        super().display_info()
        print(f"Number of Pages: {self.num_pages}")

class DVD(LibraryItem):
    def __init__(self, title, author, item_id, cd_type, contents):
        super().__init__(title, author, item_id)
        self.cd_type = cd_type
        self.contents = contents

    def display_info(self):
        super().display_info()
        print(f"CD type: {self.cd_type}")
        print("CD contents: ", end="")
        for file in self.contents:
            print(file, end=" ")
        print()

class Magazine(LibraryItem):
    def __init__(self, title, author, item_id, series):
        super().__init__(title, author, item_id)
        self.series = series

    def display_info(self):
        super().display_info()
        print(f"Series: {self.series}")

def main():
    # #ex1
    # c = Circle(2)
    # Circle.print_class_name()
    # print("Disk area:", c.calculate_disk_area())
    # print("Circle perimeter:", c.calculate_perimeter())
    # print()

    # r = Rectangle(2, 3)
    # Rectangle.print_class_name()
    # print("Rectangle area:", r.calculate_area())
    # print("Rectangle perimeter:", r.calculate_perimeter())
    # print()

    # t = Triangle(4, 5, 6)
    # Triangle.print_class_name()
    # print("Triangle area:", t.calculate_area())
    # print("Triangle perimeter:", t.calculate_perimeter())

    # #ex2
    # s = SavingsAccount()
    # s.credit_account()
    # s.credit_account()
    # print("Account balance:", s.amount)
    # s.update_package("Premium")
    # s.credit_account()
    # print("Account balance:", s.amount)
    # s.update_interest_rate(100)
    # print("Your balance will be:", s.calculate_interest(50), "after 50 years")

    # c = CheckingAccount()
    # c.make_a_deposit(200)
    # print("Checking Account balance:", c.amount)
    # result = c.transfer(68, s)
    # if result == "Success":
    #     print("Transfer succeded")
    #     print("Balance of the account credited:", s.amount)
    #     print("Balance of the sender account:", c.amount)
    # else:
    #     print(result)
    # result = c.transfer(200, s)
    # if result == "Success":
    #     print("Transfer succeded")
    #     print("Balance of the account credited:", s.amount)
    #     print("Balance of the sender account:", c.amount)
    # else:
    #     print(result)

    # #ex3
    # c = Car("VW", "Golf mk 2", 2000, 500, 30)
    # print(c.calculate_mileage())

    # m = Motorcycle("Yamaha", "VMAX", 1988, 200, 7)
    # print(m.calculate_mileage())

    # t = Truck("Ford", "F-150", 2016, 565, 700, 2500)
    # print(t.calculate_towing_capacity())

    # #ex4
    # e1 = Employee("Andrew", "a@email.com", "07568312312", 2000)
    # e2 = Employee("Laura", "l@email.com", "0230234765", 2200)
    # e3 = Employee("Batman", "badman@gmail.com", "0788888888", 0)
    # e3.raise_salary(5000)
    # m = Manager("Bob", "bob.manager@email.com", "07878787878", 10000)
    # m.hire(e1)
    # m.hire(e2)
    # m.hire(e3)
    # m.print_employees()
    
    # e4 = Engineer("Py Fan", "pytonmaster@email.com", "0707234567", 2700, "Pyton 3.1")
    # e4.learn_a_new_language("Python 2.0")
    # e4.learn_a_new_language("C")
    # e4.assign_to_project("Pyton 4.0")
    # print(f"{e4.name} knows the following languages:")
    # e4.print_known_languages()
    # print()

    # products = {
    #     "sofware1": 1000000000,
    #     "gaming_pc": 120,
    #     "lama": 27
    # }

    # s = Salesperson("Jason Capital", "richbastard@email.com", "023056550702", 100, products)
    # s.add_product_to_stock("gaming_pc", 140)
    # print(s.sell_product("lama", 40))
    # print(s.sell_product("software11", 20)) 
    # print(s.sell_product("sofware1", 20)) 

    # #ex5
    # m = Mammal("Kangaroo", "Savana", "orange", 2)
    # m.eat("wet grass")
    # print(m.run())
    # print()

    # b1 = Bird("Duffy Duck", "Bugs Bunny's hose", False)
    # b2 = Bird("Canard", "Grandma's Cage", True)
    # b1.fly()
    # b2.lay_an_egg();b2.lay_an_egg();b2.lay_an_egg();b2.lay_an_egg()
    # print(f"{b2.name} layed {b2.lifetime_egg_record} eggs")
    # print()

    # f1 = Fish("Jaws", "Pacific", "Deep water", True)
    # f2 = Fish("Nemo", "Underwater", "blue", False)
    # f1.hunt("salmon")
    # f2.explore("blue")

    #ex6
    i1 = LibraryItem("Pen", "Pen inventor", "124")
    i1.check_out()
    i2 = LibraryItem("Music Theory", "A gud music profesor", "ISBN-1234-5555-1234567")
    i2.return_item()
    print()

    b1 = Book("Fundamentele Algebrice ale Informaticii", "FLT", "ISBN-3268-5141-132424", 606)
    b1.display_info()
    print()

    cont = ["music1", "a file", "another_file"]
    d = DVD("dvd bomba", "eu", "25", "DVD", cont)
    d.display_info()
    print()

    m = Magazine("La gatit cu Gamila Cusine", "Camila Cusine", "12048357t48", "Mastar da art of cooking vol 5")
    m.display_info()

if __name__ == "__main__":
    main()