# Interface Segregation Principle (ISP)

# The Interface Segregation Principle(ISP) deals with the disadvantages of “fat” interfaces.
# Classes that have “fat” interfaces are classes whose interfaces are not cohesive.
# In other words, the interfaces of the class can be broken up into groups of member functions.
# Each group serves a different set of clients.
# Thus some clients use one group of member functions, and other clients use the other groups.


# An interface of leader who can create a sub task and assign task
class I_Lead:
    def create_sub_task(self):
        return

    def assign_task(self):
        return


# An interface of programmer who can only work on a task
class I_Programmer:
    def work_on_task(self):
        return


# Programmer class implements the programmer interface.
class Programmer(I_Programmer):
    def work_on_task(self):
        print("work on sub task proggrammer")
        return


# Manager leader implements the manager inteface.
class Manager_Lead(I_Lead):
    def assign_task(self):
        print("assign task manager")
        return

    def create_sub_task(self):
        print("create sub task manager")
        return


# Team leader implements the manager inteface and the programmer interface
# giving him all the options.
class Team_Lead(I_Lead, I_Programmer):
    def work_on_task(self):
        print("work on sub task team_lead")
        return

    def assign_task(self):
        print("assign task team_lead")
        return

    def create_sub_task(self):
        print("create sub task team_lead")
        return


class Company():
    def __init__(self, employees):
        self.employees = employees


if __name__ == '__main__':
    employees = []

    p = Programmer()
    m = Manager_Lead()
    t = Team_Lead()

    employees.append(p)
    employees.append(m)
    employees.append(t)

    p.work_on_task()
    m.assign_task()
    m.create_sub_task()
    t.work_on_task()
    t.assign_task()
    t.create_sub_task()

    company = Company(employees)
