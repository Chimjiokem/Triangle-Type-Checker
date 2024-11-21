#A Python program that determines the type of a triangle based on its three side length
x = float(input('What is the length of the first side of the triangle? '))
y = float(input('What is the length of the second side of the triangle? '))
z = float(input('What is the length of the third side of the triangle? '))

if x + y <= z or y + z <= x or z + x <= y:
    print('Error! Triangle does not exist.') 

else:
    if x == y == z:
        print('This isan equilateral triangle.\nThe three sides and three angles are equal.')
    elif x == y == z or z == x:
        print('This is an isoceles triangle.\nTwo sides have equal lengths.')
    else:
        print('This is a scalene triangle.\nThree sides and three angles have different lengths')

# Use map and split to take three space-separated integers as input, then converting them to a list of integers
# sidelengths_of_triangle = list(map(int, input(). split()))

#     print('Yes')  # Print 'Yes' if the condition is met
# else:
#     print('No')   # Print 'No' if the condition is not met
