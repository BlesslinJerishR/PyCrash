# 11.3
class Employee:

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        # 5000 $
        if salary_raise == 5000:
            self.salary += 5000
        else:
            self.salary += salary_raise

