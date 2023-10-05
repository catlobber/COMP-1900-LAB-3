#Get user inputs
print("Starting Corner:")
starting_street = int(input("Street - "))
starting_avenue = int(input("Avenue - "))
print("Ending Corner:")
ending_street = int(input("Street - "))
ending_avenue = int(input("Avenue - "))
#Find distance needed to travel and the direction and print where to go to user
if (starting_street > ending_street):
    movementy = (starting_street - ending_street) * 750
    directiony = ('South')
    print(f'Take Avenue {starting_avenue} {directiony} for {movementy}ft until you get to Street {ending_street} ')
elif (starting_street < ending_street):
    movementy = (ending_street - starting_street) * 750
    directiony = ('North')
    print(f'Take Avenue {starting_avenue} {directiony} for {movementy}ft until you get to Street {ending_street} ') 
else: 
    movementy = 0  

#Find distance, direction, and turn and print where to go to user
if (starting_avenue > ending_avenue):
    movementx = (starting_avenue - ending_avenue) * 750
    turn = ('Right')
    directionx = ('East')
    print(f'Turn {turn} on Street {ending_street}')
    print(f'Take Street {ending_street} {directionx} for {movementx}ft until you get to Avenue {ending_avenue}')
elif (starting_street < ending_street):
    movementx = (ending_avenue - starting_avenue) * 750
    turn = ('Left')
    directionx = ('West')
    print(f'Turn {turn} on Street {ending_street}')
    print(f'Take Street {ending_street} {directionx} for {movementx}ft until you get to Avenue {ending_avenue}')
else: 
    movementx = 0  
#Final statement which always prints
print("Yay! You have arrived!")