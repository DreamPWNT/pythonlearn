cell = input('Enter chess cell: ')

cell_symbol = cell[0].lower()
cell_index = int(cell[1])

if cell_symbol in 'aceg' and cell_index % 2 != 0 or cell_symbol in 'dbfh' and cell_index % 2 == 0:
    print('Is Black')
else:
    print('Is White')
