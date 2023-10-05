#Initialize all brackets
first_bracket = 0
second_bracket = 0
third_bracket = 0
fourth_bracket = 0
fifth_bracket = 0
sixth_bracket = 0
seventh_bracket = 0
#Obtain user income
income = float(input("What was your 2022 income? "))
#Tax for the first bracket
if (income < 10275):
    first_bracket = (10275 - income) * 0.1
    print(f"First $10,275: $ {first_bracket:.2f}")
elif(income >= 10275):
    first_bracket = 10275 * 0.1
    print(f"First $10,275: $ {first_bracket:.2f}")
    #Tax for second bracket
    if (income > 10275 and income < 41775):
     second_bracket = (income - 10275) * 0.12
     print(f"$10,275-$41775: $ {second_bracket:.2f}")
    elif (income >= 41775): 
     second_bracket = (41775 - 10275) * 0.12
     print(f"$10,275-$41775: $ {second_bracket:.2f}")
     #Tax for third bracket
     if (income > 41775 and income < 89075):
      third_bracket = (income - 41775) * 0.22
      print(f"$41,775-$89,075: $ {third_bracket:.2f}")
     elif (income >= 89075):
      third_bracket = (89075 - 41775) * 0.22
      print(f"$41,775-$89,075: $ {third_bracket:.2f}")
      #Tax for fourth bracket
      if (income > 89075 and income < 170050):
       fourth_bracket = (income - 89075) * 0.24
       print(f"$89,075-$170,050: $ {fourth_bracket:.2f}")
      elif (income >= 170050): 
        fourth_bracket = (170050 - 89075) * 0.24
        print(f"$89,075-$170,050: $ {fourth_bracket:.2f}")
        #Tax for fifth bracket
        if (income > 170050 and income < 215950):
         fifth_bracket = (income - 170050) * 0.32
         print(f"$170,050-$215,950: $ {fifth_bracket:.2f}")
        elif (income >= 215950):
         fifth_bracket = (215950 - 170050) * 0.32
         print(f"$170,050-$215,950: $ {fifth_bracket:.2f}")
         #Tax for sixth bracket
         if (income > 215950 and income < 539900):
          sixth_bracket = (income - 215950) * 0.35
          print(f"$215,950-$539,900: $ {sixth_bracket:.2f}")
         elif (income >= 539900): 
          sixth_bracket = (539900 - 215950) * 0.35
          print(f"$215,950-$539,900: $ {sixth_bracket:.2f}")
          #Tax for seventh bracket
          if (income > 539900):
           seventh_bracket = (income - 539900)
           print(f"$539,900+: $ {seventh_bracket:.2f}")
#Total Taxes
total_taxes = first_bracket + second_bracket + third_bracket + fourth_bracket + fifth_bracket + sixth_bracket + seventh_bracket
#Effective tax rate
eff_tax_rate = total_taxes/income
print(f"Total Tax Owed: ${total_taxes:.2f}")
print(f"Effective Tax Rate = {eff_tax_rate*100:.1f}%")