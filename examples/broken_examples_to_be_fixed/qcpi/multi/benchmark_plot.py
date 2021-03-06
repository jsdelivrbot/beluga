import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
font = {'size': 12}
mpl.rc('font', **font)

def autolabel(rects, formatter=None):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        if formatter is None:
            if height > 0.1:
                label = '%.1f' % (height)
            else:
                # label = ''
                label = '%.2f' % (height)
        else:
            label = formatter(height)

        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                label,
                ha='center', va='bottom',fontsize=9)

# data to plot
n_groups = 5
# qcpi_time = (0.04,0.09,0.2,0.81,4.59)
# shooting_time = (0.2733,0.65,1.72,6.14,36.91)

qcpi_time = (0.02,0.05,0.15,0.43,2.86)
shooting_time = (0.19,0.37,1.29,3.65,26.91)

# mshoot_time_8_4c = (4.62, 4.76, 8.04, 10.01, 24.03)
# mshoot_time_4_4c = (4.81, 5.18, 7.78, 9.81, 20.31)
mshoot_time_8_8c = (2.92, 3.07, 5.05, 6.88, 15.73)
mshoot_time_4_8c = (3.89, 4.29, 6.29, 7.71, 15.11)

mshootpar_time_8_8c = (0.08, 0.16, 0.659, 2.233, 14.12)
mshootpar_time_4_8c = (0.07, 0.16, 0.595, 1.952, 11.14)

# qcpi_speedup = tuple(s_t/q_t for s_t,q_t in zip(shooting_time,qcpi_time))
qcpi_speedup = tuple(s_t/q_t for s_t,q_t in zip(mshootpar_time_4_8c,qcpi_time))

# create plot
fig, ax = plt.subplots()
fig.set_size_inches(11,8.5)

index = np.arange(n_groups)
bar_width = 0.8/(6)
opacity = 0.8

rects1 = plt.bar(index, shooting_time, bar_width,
                 alpha=opacity,
                 # color='b',
                 label='Single Shooting')


rects2 = plt.bar(index + bar_width, mshoot_time_8_8c, bar_width,
                 alpha=opacity,
                 # color='g',
                 label='Parallel Shooting Explicit (8 arcs)')

rects3 = plt.bar(index + bar_width*2, mshoot_time_4_8c, bar_width,
                 alpha=opacity,
                 # color='g',
                 label='Parallel Shooting Explicit (4 arcs)')

rects4 = plt.bar(index + bar_width*3, mshootpar_time_8_8c, bar_width,
                 alpha=opacity,
                 # color='g',
                 label='Parallel Shooting Numba (8 arcs)')

rects5 = plt.bar(index + bar_width*4, mshootpar_time_4_8c, bar_width,
                 alpha=opacity,
                 # color='r',
                 label='Parallel Shooting Numba (4 arcs)')

rects6 = plt.bar(index + bar_width*5, qcpi_time, bar_width,
                 alpha=opacity,
                 # color='g',
                 label='QCPI')

plt.xlabel('Number of Vehicles',fontsize=13)
plt.ylabel('Runtime [sec]',fontsize=13)
plt.xticks(index+bar_width*2.5, ('n=1', 'n=2', 'n=5', 'n=10', 'n=25'))
plt.legend(loc='upper left')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)
autolabel(rects5)
autolabel(rects6)
ax2 = ax.twinx()
ax2.set_ylabel('QCPI Speedup [x]', color='b')
ax2.tick_params('y', colors='b')
ax2.plot(index+bar_width*2.5, qcpi_speedup, marker='D', color='b')
ax2.set_ylim([2, 8])
ax.set_ylim([0,32.5])
plt.grid(True)
plt.tight_layout()
plt.savefig('plots/qcpi_benchmark_run_time.eps')
plt.show()


# # data to plot
# n_groups = 5
#
#
# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.35
# opacity = 0.8
#
# rects1 = plt.bar(index, qcpi_speedup, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='QCPI Speedup')
#
# # rects2 = plt.bar(index + bar_width, qcpi_time, bar_width,
# #                  alpha=opacity,
# #                  color='g',
# #                  label='QCPI')
#
# plt.xlabel('Number of Vehicles',fontsize=13)
# plt.ylabel('QCPI Speedup [x]',fontsize=13)
# # plt.title('Scores by person')
# plt.xticks(index, ('n=1', 'n=2', 'n=5', 'n=10', 'n=25'))
# # plt.legend()
#
# autolabel(rects1)
#
# plt.ylim([0,25])
# plt.grid(True)
#
# plt.tight_layout()
# plt.savefig('plots/Speedup.eps')
# plt.show()


#
#
# # data to plot
# n_groups = 5
# qcpi_compile_time = (2.74,3.6,7.28,18.9,98.63)
# shooting_compile_time = (1.37,1.49,2.22,2.97,6.7)
#
# # create plot
# fig, ax = plt.subplots()
# index = np.arange(n_groups)
# bar_width = 0.35
# opacity = 0.8
#
# rects1 = plt.bar(index, shooting_compile_time, bar_width,
#                  alpha=opacity,
#                  color='b',
#                  label='Shooting Method')
#
# rects2 = plt.bar(index + bar_width, qcpi_compile_time, bar_width,
#                  alpha=opacity,
#                  color='g',
#                  label='QCPI')
#
# plt.xlabel('Number of Vehicles',fontsize=13)
# plt.ylabel('Compile time [sec]',fontsize=13)
#
# plt.xticks(index + bar_width/2, ('n=1', 'n=2', 'n=5', 'n=10', 'n=25'))
# autolabel(rects1)
# autolabel(rects2)
# plt.ylim([0,110])
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('plots/qcpi_benchmark_compile_time.eps')
# plt.show()
#

# # Speedup comparison by number of cores
#
# # qcpi_data = np.recarray((2,) ,formats=['i4','f8','f8','f8','f8'],
# #                               names=('n','C1','C2','C4','C8'))
# #
# labels = ['One Core', 'Two Cores', 'Four Cores', 'Eight Cores']
# x = [1,2,3,4]
#
# qcpi_data = np.array([(25,47.2,33.55,24.83,4.59),
#                       (10,4.65,3.36,2.27,0.81)])
#
# shoot_data = np.array([[25,114.39,96.72,75.2,36.91],
#                        [10,33.62,25.94,19.26,6.14]])
#
# fig, ax = plt.subplots()
# box = ax.get_position()
# # ax.set_position([box.x0, box.y0, box.width * 0.9, box.height])
# plt.xticks(x,labels,rotation=30)
#
# ax.plot(x, qcpi_data[0,1:],'*-', lw=1.5, ms=7, label='QCPI n=25')
# ax.plot(x, qcpi_data[1,1:],'o-', lw=1.5, ms=7, label='QCPI n=10')
# ax.plot(x, shoot_data[0,1:],'d-',lw=1.5, ms=7, label='Shooting n=25')
# ax.plot(x, shoot_data[1,1:],'h-',lw=1.5, ms=7, label='Shooting n=10')
# ax.set_ylabel('Runtime [sec]')
# ax.tick_params('y')
# plt.subplots_adjust(bottom=0.18,right=0.85)
# # Put a legend to the right of the current axis
# ax.legend(loc='upper left', bbox_to_anchor=(0.75, 1.0))
# plt.grid(True)
# plt.savefig('plots/qcpi_benchmark_cores_run_time.eps')
#
# fig, ax = plt.subplots()
# box = ax.get_position()
# plt.xticks(x,labels,rotation=30)
#
# ax.plot(x, qcpi_data[0,1]/qcpi_data[0,1:],'*-', lw=1.5, ms=7, label='QCPI n=25')
# ax.plot(x, qcpi_data[1,1]/qcpi_data[1,1:],'o-', lw=1.5, ms=7, label='QCPI n=10')
# ax.plot(x, shoot_data[0,1]/shoot_data[0,1:],'D-',lw=1.5, ms=7, label='Shooting n=25')
# ax.plot(x, shoot_data[1,1]/shoot_data[1,1:],'h-',lw=1.5, ms=7, label='Shooting n=10')
# ax.set_ylim([0,11])
# # ax.plot(x, shoot_data[0,1:]/qcpi_data[0,1:],'*-', lw=1.5, label='n=25')
# # ax.plot(x, shoot_data[1,1:]/qcpi_data[1,1:],'o-', lw=1.5, label='n=10')
# ax.set_ylabel('Speedup against single-core [x]')
# ax.tick_params('y')
# plt.subplots_adjust(bottom=0.15)
# # Put a legend to the right of the current axis
# ax.legend(loc='upper left')
# plt.grid(True)
# plt.savefig('plots/qcpi_benchmark_cores_speedup.eps')
# plt.show()
#
import tabulate
tbl1 = tabulate.tabulate(
                [('QCPI',*qcpi_time),
                 ('Single Shooting',*shooting_time),
                 ('Parallel Shooting Explicit (8 arcs)',*mshoot_time_8_8c),
                 ('Parallel Shooting Explicit (4 arcs)',*mshoot_time_4_8c),
                 ('Parallel Shooting Numba (8 arcs)',*mshootpar_time_8_8c),
                 ('Parallel Shooting Numba (4 arcs)',*mshootpar_time_4_8c)],
                headers=['Solver','$n=1$','$n=2$','$n=5$','$n=10$','$n=25$',],
                tablefmt='latex_raw')
print(tbl1,end='\n\n')
#
# tbl2 = tabulate.tabulate(
#                 [('QCPI',*qcpi_data[0,:]),
#                  ('QCPI',*qcpi_data[1,:]),
#                  ('Shooting',*shoot_data[0,:]),
#                  ('Shooting',*shoot_data[1,:])],
#                 headers=['Solver','$n$','Single core [sec]','Two cores [sec]','Four cores [sec]','Eight cores [sec]'],
#                 tablefmt='latex_raw')
# print(tbl2,end='\n\n')
#
