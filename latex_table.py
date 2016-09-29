
class latex_table():

    columns = []
    rows = []
    ncolumns = 0
    nrows = 0
    length = 0
    names = []

    def __init__(self):
        self.columns = []
        self.names = []
        self.rows = []

    def add_column(self, column_name, column_array):
        self.ncolumns += 1
        if self.ncolumns == 1:
            self.length = len(column_array)

        if self.ncolumns > 1:
            if len(column_array) > self.length:
                raise NameError( "ARRAY MUST BE "+str(self.length)+ " IN LENGTH!")

        self.columns.append( list(column_array) )
        self.names.append(column_name)


    def write_by_column(self, out):
        myfile = open(out, 'w')
        header = ' & '.join(self.names) + ' \\\\'
        myfile.write ("%s\n" % header)
        for j in range(self.length):
            test = [item[j] for item in self.columns ]
            proper = ' & '.join(str(x) for x in test) + " \\\\"
            myfile.write( "%s\n" % proper)
        myfile.close()
                          

    def set_column_names(self, names_array):
        self.names = names_array

    def add_row(self, row_array):
        self.nrows += 1
        
        if self.nrows ==1:
            self.length = len(row_array)
        if self.nrows > 1:
            if len(row_array) != self.length:
                raise NameError( "ROW MUST BE "+ str(self.length) + " IN LENGTH." )
        
        self.rows.append( list(row_array) )

    def write_by_row(self, outfile):
        myfile = open(outfile, 'w')
        header = ' & '.join(self.names) + ' \\\\'
        myfile.write ("%s\n" % header)
        for j in range(self.length):
            test = [item[j] for item in self.rows ]
            proper = ' & '.join(str(x) for x in test) + " \\\\"
            myfile.write( "%s\n" % proper)
        myfile.close()




        
