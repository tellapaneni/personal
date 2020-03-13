import matplotlib.pyplot as plt
import csv
import numpy as np
import urllib.request
import matplotlib.dates as mdates

# x =[1,2,3,4,5]
# y =[1,4,6,8,10]
# xy=[[1,2,3,4,5],
#     [2,3,4,5,6],
#     [4,5,6,7,8],
#     [10,11,12,13,14]]

# plt.plot(x,y)
# plt.scatter(x,y,edgecolors="green")
#
# slices = [7,2,2,13]
# activities = ['sleeping','eating','working','playing']
# cols = ['c','m','r','b']
# #
# plt.pie(slices,
#         labels=activities,
#         colors=cols,
#         startangle=90,
#         shadow= True,
#         explode=(0,0.3,0,0),
#         autopct='%1.1f%%')

# x = []
# y = []
#
# with open('example.txt','r') as csvfile:
#     plots = csv.reader(csvfile, delimiter=',')
#     for row in plots:
#         x.append(int(row[0]))
#         y.append(int(row[1]))
#
# plt.plot(x,y, label='Loaded from file!')
# plt.violinplot(slices)
plt.xlabel('x values')
plt.ylabel('ylabel')
plt.title('This is a stupid graph')
plt.show()

# def bytespdate2num(fmt, encoding='utf-8'):
#     strconverter = mdates.strpdate2num(fmt)
#
#     def bytesconverter(b):
#         s = b.decode(encoding)
#         return strconverter(s)
#
#     return bytesconverter
#
#
# def graph_data(stock):
#     fig = plt.figure()
#     ax1 = plt.subplot2grid((1, 1), (0, 0))
#
#     # Unfortunately, Yahoo's API is no longer available
#     # feel free to adapt the code to another source, or use this drop-in replacement.
#     stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
#     source_code = urllib.request.urlopen(stock_price_url).read().decode()
#     stock_data = []
#     split_source = source_code.split('\n')
#     for line in split_source[1:]:
#         split_line = line.split(',')
#         if len(split_line) == 7:
#             if 'values' not in line and 'labels' not in line:
#                 stock_data.append(line)
#
#     date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
#                                                                       delimiter=',',
#                                                                       unpack=True,
#                                                                       # %Y = full year. 2015
#                                                                       # %y = partial year 15
#                                                                       # %m = number month
#                                                                       # %d = number day
#                                                                       # %H = hours
#                                                                       # %M = minutes
#                                                                       # %S = seconds
#                                                                       # 12-06-2014
#                                                                       # %m-%d-%Y
#                                                                       converters={0: bytespdate2num('%Y-%m-%d')})
#
#     ax1.plot_date(date, closep, '-', label='Price')
#     for label in ax1.xaxis.get_ticklabels():
#         label.set_rotation(45)
#     ax1.grid(True)  # , color='g', linestyle='-', linewidth=5)
#
#     plt.xlabel('Date')
#     plt.ylabel('Price')
#     plt.title('Interesting Graph\nCheck it out')
#     plt.legend()
#     plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
#     plt.show()
#
# graph_data('TSLA')

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19680801)
data = np.random.randn(2, 100)

fig, axs = plt.subplots(2, 2, figsize=(5, 5))
axs[0, 0].hist(data[0])
axs[1, 0].scatter(data[0], data[1])
axs[0, 1].plot(data[0], data[1])
axs[1, 1].hist2d(data[0], data[1])

plt.show()