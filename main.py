print(" 🌟 Jobs Jobs Jobs! 🌟 ")
print()


class job:
  name = None
  salary = None
  hours = None

  def __init__(self, name, salary, hours):
    self.name = name
    self.salary = salary
    self.hours = hours

  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")


class teacher(job):
  subject = None
  position = None

  def __init__(self, salary, hours, subject, position):
    self.name = "Teacher"
    self.salary = salary
    self.hours = hours
    self.subject = subject
    self.position = position

  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Subject: {self.subject}")
    print(f"Position: {self.position}")


class doctor(job):
  speciality = None
  years = None

  def __init__(self, salary, hours, speciality, years):
    self.name = "Doctor"
    self.salary = salary
    self.hours = hours
    self.speciality = speciality
    self.years = years

  def print(self):
    print(f"Job type: {self.name}")
    print(f"Salary: {self.salary}")
    print(f"Hours worked: {self.hours}")
    print(f"Speciality: {self.speciality}")
    print(f"Years of experience: {self.years}")


lawyer = job("Lawyer", "$ Squillions", "60")
lawyer.print()
print()

doc = doctor("$ Doing very nicely thank you", "50", "Pediatric Consultant", "7")
doc.print()
print()

teach = teacher("$ Nowhere near enough", "All of them", "Computer Science",
                "Classroom Teacher")
teach.print()
print()
