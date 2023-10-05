
#Obtain user income
income = float(input("What was your 2022 income? "))
#Tax for the first bracket
if (income < 10275):
    first_bracket = (10275 - income) * 0.1
    print(f"First $10,275: $ {first_bracket}")
else:
    first_bracket = 10275 * 0.1
    print(f"First $10,275: $ {first_bracket}")
#Tax for the second bracket
if (income > 10275 and income < 41775):
    second_bracket = (income - 10275) * 0.12
    print(f"$10,275-$41775: $ {second_bracket}")
else: 
    second_bracket = (41775 - 10275) * 0.12
    print(f"$10,275-$41775: $ {second_bracket}")
#Tax for the third bracket
if (income > 41775 and income < 89075):
    third_bracket = (income - 41775) * 0.22
    print(f"$41,775-$89,075: $ {second_bracket}")
else:
    third_bracket = (89075 - 41775) * 0.22
    print(f"$10,275-$41775: $ {second_bracket}")
#Tax for the fourth bracket
if (income > 89075 and income < 170050):
    fourth_bracket = (income - 89075) * 0.24
else: 
    fourth_bracket = (170050 - 89075) * 0.24
#Tax for the fifth bracket
if (income > 170050 and income < 215950):
    fifth_bracket = (income - 170050) * 0.32
else:
    fifth_bracket = (215950 - 170050) * 0.32
#Tax for the sixth bracket
if (income > 215950 and income < 539900):
    sixth_bracket = (income - 215950) * 0.35
else: 
    sixth_bracket = (539900 - 215950) * 0.35
#Tax for the seventh bracket
if (income > 539900):
    seventh_bracket = (income - 539900)