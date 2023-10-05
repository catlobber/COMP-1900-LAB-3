
# Get user input for hourly rate & hours worked for the week
hourly_payrate = float(input("Enter base hourly rate: "))
hours_worked = float(input("Enter total hours worked for the week: "))
holiday_hours = float(input(f"How many of those {hours_worked} were on the holidays? "))
# Find base hours
base_hours = 0
hours_worked -= holiday_hours
if (hours_worked <= 40 and hours_worked > 0):
  base_hours = hours_worked
elif (hours_worked > 40 ):
  base_hours = 40
# Find overtime hours
if (hours_worked - (holiday_hours + 40)) > 0: 
  overtime_hours = (hours_worked - 40) 
else:
  overtime_hours = 0
#Calculate pay rate for overtime and holiday
overtime_payrate = hourly_payrate * 1.5
holiday_payrate = hourly_payrate * 2.0
#Calculate pay for the type of hours and total pay
base_pay = base_hours * hourly_payrate
overtime_pay = overtime_hours * overtime_payrate
holiday_pay = holiday_hours * holiday_payrate
total_pay = base_pay + overtime_pay + holiday_pay
# Print to user
print(f'Base:     $ {hourly_payrate} x {base_hours} hours =  $ {base_pay}')
print(f'Overtime: $ {overtime_payrate} x {overtime_hours} hours = $ {overtime_pay}')
print(f'Holiday:  $ {holiday_payrate} x {holiday_hours} hours = $ {holiday_pay}')
print(f'Total pay:$                 = $ {total_pay}')