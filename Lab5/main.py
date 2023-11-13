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

    #ex2
    s = SavingsAccount()
    s.credit_account()
    s.credit_account()
    print("Account balance:", s.amount)
    s.update_package("Premium")
    s.credit_account()
    print("Account balance:", s.amount)
    s.update_interest_rate(100)
    print("Your balance will be:", s.calculate_interest(50), "after 50 years")

    c = CheckingAccount()
    c.make_a_deposit(200)
    print("Checking Account balance:", c.amount)
    result = c.transfer(68, s)
    if result == "Success":
        print("Transfer succeded")
        print("Balance of the account credited:", s.amount)
        print("Balance of the sender account:", c.amount)
    else:
        print(result)
    result = c.transfer(200, s)
    if result == "Success":
        print("Transfer succeded")
        print("Balance of the account credited:", s.amount)
        print("Balance of the sender account:", c.amount)
    else:
        print(result)

if __name__ == "__main__":
    main()