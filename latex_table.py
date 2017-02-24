import numpy as np
import itertools

class latex_table():

    columns = []
    rows = []
    ncolumns = 0
    nrows = 0
    column_lengths = []
    length= 0
    names = []
    units = []
    extra_header = []

    def __init__(self):
        self.columns = []
        self.names = []
        self.rows = []
        self.units = []   
        self.extra_header = []

    def add_column(self, column_name, column_array):
        self.ncolumns += 1
        self.column_lengths.append(len(column_array))

#        if self.ncolumns == 1:
#          self.length = len(column_array)

#        if self.ncolumns > 1:
#            if len(column_array) > self.length:
#                raise NameError( "ARRAY MUST BE "+str(self.length)+ " IN LENGTH!")

        self.columns.append( list(column_array) )
        self.names.append(column_name)

    def pm(self, value, error):
        return str(value)+'$\pm$'+str(error)

    def lowhigh(self, value, low, high):
        return str(value) + '$_{' + str(low) + '}' + '^{' +str(high)+ '}$'  

    def equalize_column_length(self):
        'Find longest individual column and pad others with spaces to equal max length'
        max_length = 0
        for col in self.columns:
            length = len(col)
            if length > max_length: self.length=length

        for col in self.columns:
            if len(col) == self.length: continue
            else:
                diff = self.length - len(col)
                col.extend([' ']*diff)
        #print np.shape(self.columns)

    def write_by_column(self, out, append=False):
        if append:
            myfile = open(out, 'a')
        else:
            myfile = open(out, 'w')
        myfile.write('%s\n' % '\hline')
        myfile.write('%s\n' % '\hline')
        if self.extra_header:
            extra_header = ' & '.join(self.extra_header) + ' \\\\'
            myfile.write ("%s\n" % extra_header)
        header = ' & '.join(self.names) + ' \\\\'
        myfile.write ("%s\n" % header)
        myfile.write('%s\n' % '\hline')
        for j in range(self.length):
            test = [item[j] for item in self.columns ]
            proper = ' & '.join(str(x) for x in test) + " \\\\"
            myfile.write( "%s\n" % proper)
        #myfile.write('%s\n' % '\hline')
        myfile.close()
        self.names=[]
        self.extra_header=[]
        self.columns=[]
                          
    def set_column_names(self, names_array):
        self.names = names_array

    def set_units(self, units_array):
        self.units = units_array

    def set_extra_header(self, identifiers):
        self.extra_header = identifiers

    def add_row(self, row_array):
        self.nrows += 1
        
        if self.nrows ==1:
            self.ncolumns = len(row_array)
        if self.nrows > 1:
            if len(row_array) != self.ncolumns:
                raise NameError( "ROW MUST BE "+ str(self.ncolumns) + " IN LENGTH." )
        
        self.rows.append( list(row_array) )
     
    def write_by_row(self, outfile):
        if self.names:
            myfile = open(outfile, 'w')
            header = ' & '.join(self.names) + ' \\\\'
        myfile.write ("%s\n" % header)
        if self.units:
            header_units = ' & '.join(self.units) + ' \\\\'
            myfile.write ("%s\n" % header_units)
        for i in range(self.nrows):
            test = [j for j in self.rows[i]]
            proper = ' & '.join(str(x) for x in test) + " \\\\"
            myfile.write( "%s\n" % proper)
        myfile.close() 
       



        
