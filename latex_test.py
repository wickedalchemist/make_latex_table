import latex_table 
import numpy as np


#MAKE TABLE BY ADDING COLUMNS
x = np.arange(10)
y = np.arange(10)+5

z = y +3

new_table = latex_table.latex_table()

new_table.add_column('col1', x)
new_table.add_column('col2', y)
new_table.add_column('col2', z)

new_table.write_by_column('test_columns.txt')

#MAKE TABLE BY ADDING ROWS
new_table = latex_table.latex_table()

x = [1,2,3,4,5]
y = ['a','b','c','d',3]
z = [6,7,8,9,0]

new_table.set_column_names(['x','y','z']) 
new_table.add_row(x)
new_table.add_row(y)
new_table.add_row(z)

new_table.write_by_row('test_row.txt')
