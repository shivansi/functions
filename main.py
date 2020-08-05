#functions are intructions to do a certain action

#2 things required for functions: we define them, we call them to work

#!)define function
def greeting():
  print("hello")

#2) call the function to work
greeting()

def goodbye(name):
  print("byeee, "+name)

goodbye("mario")

def add(num):
  for i in range(5):
    sum=num+1
    print(sum)

    if sum<5:
      print("less than 5")
    else:
      print("greater than 5")

add(3)