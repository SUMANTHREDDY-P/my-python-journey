
class Student:
  def __init__(self,name):
    self.name=name
    self.marks=[]

  def get_grade(self):
    if len(self.marks) == 0:
     return "No marks"
    sum_marks=sum(self.marks)
    average = sum_marks / len(self.marks)
    print('-'*10)
    if average >= 90:
      return "A grade"
    elif average >= 80:
      return "B grade"
    elif average >= 60:
      return 'C grade'
    elif average >= 50:
      return 'D grade'
    else:
      return("F fail")
    
  def insert_marks(self):
    marks_input = input(
            f"Enter marks for {self.name} (Maths, Physics, Chemistry) [m,p,c]: "
        )
    mark=marks_input.split(",")
    for m in mark:
      try:
        self.marks.append(int(m))
      except ValueError:
        print(f"Invalid mark '{m}', please enter numbers only")
student=students = [
    "Sumanth", "HARI", "BUNNY", "NAVEEN",
    "PRIYA", "RAHUL", "ANITA", "KARTHIK",
    "DEEPA", "VIKRAM", "MEENA", "ARJUN"
]
stu_info=[]
for stu in student:

  st=Student(stu)
  st.insert_marks()
  grade=st.get_grade()
  print(grade)
  stu_info.append(f'{stu.upper()} your {st.marks}-->{grade} ')
print("##\nAll Student Grades:")
for info in stu_info:
  print(info)