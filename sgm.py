name = input("Enter Student Name: ")

subjects = { }
while True:
    key = input("Enter Subject Name: ")
    try:
     value = int(input("Enter Subject Marks: "))
    except:
      print("Marks should be in Numbers.")
      exit()
    subjects[key] = value
    choice = input("Enter More Subjects? y/n: ")
    if choice == "n":
      break
      
def avg(subjects,name):
    Total = sum(subjects.values())
    print("Total Marks:", Total)

    Average = Total/len(subjects)
    print("Total Average:", Average)
    if Average>=90:
      print(f"{name} has A+ Grade.")
    elif Average>=85:
      print(f"{name} has A Grade.")
    elif Average>=80:
      print(f"{name} has A- Grade.")
    elif Average>=75:
      print(f"{name} has B+ Grade.")
    elif Average>=70:
      print(f"{name} has B Grade.")
    elif Average>=65:
      print(f"{name} has C+ Grade.")
    elif Average>=60:
      print(f"{name} has C Grade.")
    elif Average>=55:
      print(f"{name} has D+ Grade.")
    elif Average>=50:
      print(f"{name} has D Grade.")
    else:
      print(f"{name} failed.")
    return Average
avg(subjects,name)
