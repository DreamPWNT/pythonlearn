sides_quantity = int(input('Enter quantity of figure sides: '))

if sides_quantity < 3 or sides_quantity > 10:
    print('Invalid sides quantity')
elif sides_quantity == 3:
    print('Is triangle')
elif sides_quantity == 4:
    print('Is rectangle')
elif sides_quantity == 5:
    print('Is pentagon')
elif sides_quantity == 6:
    print('Is hexagon')
elif sides_quantity == 7:
    print('Is heptagon')
elif sides_quantity == 8:
    print('Is octagon')
elif sides_quantity == 9:
    print('Is nonagon')
elif sides_quantity == 10:
    print('Is decagon')
