class Mathematician:
  in_school = True
  def __init__(self,name,iq):
    self.name = name
    self.iq = iq

  def greeting(self):
    print(f'Hi friends, my name is {self.name}')

  def adding_things(cls, num1, num2):
    return num1 + num2

teacher1 = Mathematician('fred', 100)
teacher2 = Mathematician('Miss Nucci', 5000)

miss_nucci = teacher2
print(miss_nucci.greeting())

print(miss_nucci.adding_things(100,200))

teacher3 = Mathematician.adding_things({}, 22,33)

print(teacher3)


