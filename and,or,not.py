high_income = True
good_credit = False 

if high_income and good_credit:
  print("Eligible for loan")
else:
  print("Not eligible for loan")

high_income = True
good_credit = False 

if high_income or good_credit:
  print("Eligible for loan")
else:
  print("Not eligible for loan")

high_income = True
good_credit = False
student = False

if not student:
  print("Eligible for loan")
else:
  print("Not eligible for loan")