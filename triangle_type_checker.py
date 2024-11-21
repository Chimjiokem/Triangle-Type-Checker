x = float(input('What is the length of the first side of the triangle? '))
y = float(input('What is the length of the second side of the triangle? '))
z = float(input('What is the length of the third side of the triangle? '))

if x + y <= z or y + z <= x or z + x <= y:
    print('Error! Triangle does not exist.') 

else:
    if x == y == z:
        print('This is an equilateral triangle.\nThe three sides and three angles are equal.')
    elif x == y == z or z == x:
        print('This is an isoceles triangle.\nTwo sides have equal lengths.')
    else:
        print('This is a scalene triangle.\nThree sides and three angles have different lengths')
