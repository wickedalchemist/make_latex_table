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

new_table.make_latex_table('test_columns.txt')

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



# # import good_clusters
# # import cluster_class

# # clusters = good_clusters.get_good_clusters('f110')

# # kts = []
# # ms = []
# # zs = []
# # kinds = []
# # for i in range(len(clusters)):
# #     info = cluster_class.cluster(clusters[i])
# #     zs.append(info.z)
# #     kinds.append(info.kind)
# #     kts.append(str(info.kT) + '$_{' + str(info.kT_low) + '}' + '^{' +str(info.kT_high)+ '}$' )
# #     ms.append(np.round(info.get_m500fromkT(info.z, info.kT).value/1e14, decimals=2))

# # new_table = latex_table.latex_table()
# # new_table.add_column('Cluster', clusters)
# # new_table.add_column('z', zs)
# # new_table.add_column('kT', kts)
# # new_table.add_column('M_500 [10$^{14}$ M$_\odot$]', ms)
# # new_table.add_column('Source', kinds)
# # new_table.make_latex_table('sample_table.txt')

