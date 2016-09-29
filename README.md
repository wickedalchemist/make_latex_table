# make_latex_table
Make properly formated LaTeX tables as simple as assigning arrays as columns or rows.

If I never have to mindlessly add '&'s between columns of values again it will be too soon. This scipt lets you make a properly formatted latex table column-wise or row-wise. It checks that your column/row lengths are all the same and adds a header with column names to each table if you feel like supplying them.

# To install:
Just put latex_table.py in your path. Now you can create a latex_table object and start adding columns/rows!

# MAKE TABLE BY ADDING COLUMNS

Let's make up some columns (strings also work):
~~~
x = np.arange(10)
y = np.arange(10)+5
z = y + 3
~~~
Create instance of latex_table object: 
~~~
new_table = latex_table.latex_table()
~~~
Add columns to object. The order in which you add columns is the order (left to right) they will appear in your table
~~~
new_table.add_column('col1', x)
new_table.add_column('col2', y)
new_table.add_column('col2', z)
~~~

Write out the properly formated latex table to a text file
~~~
new_table.make_latex_table('test_columns.txt')
~~~
**Text produced:**
~~~
col1 & col2 & col2 \\
0 & 5 & 8 \\
1 & 6 & 9 \\
2 & 7 & 10 \\
3 & 8 & 11 \\
4 & 9 & 12 \\
5 & 10 & 13 \\
6 & 11 & 14 \\
7 & 12 & 15 \\
8 & 13 & 16 \\
9 & 14 & 17 \\
~~~

# MAKE TABLE BY ADDING ROWS

Create instance of latex_table object
~~~
new_table = latex_table.latex_table()
~~~
Make up some rows...
~~~
x = [1,2,3,4,5]
y = ['a','b','c','d',3]
z = [6,7,8,9,0]
~~~

Set the column names. In theory you could also just add a row that is an array of your column names.
~~~
new_table.set_column_names(['x','y','z']) 
~~~
Add rows. The order you add rows in the order (top to bottom) they will appear in the table
~~~
new_table.add_row(x)
new_table.add_row(y)
new_table.add_row(z)
~~~
Write a properly formatted latex table to a text file
~~~
new_table.write_by_row('test_row.txt')
~~~
**Text produced:**
~~~
x & y & z \\
1 & a & 6 \\
2 & b & 7 \\
3 & c & 8 \\
4 & d & 9 \\
5 & 3 & 0 \\
~~~

# Final step:
Copy and past your newly generated latex table into your latex document!
