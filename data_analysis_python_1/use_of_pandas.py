# A basic Pandas example

import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data_folder = os.path.join("input")

path = os.path.join(data_folder, "usagov_bitly_data2012-03-16-1331923249.txt")

records = [json.loads(line) for line in open(path)]
frame = pd.DataFrame(records)
tz_counts = frame['tz'].value_counts()

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10])
# following are the options for plot kind in pandas data-frame plot for arg type

# line : line plot (default)
# bar : vertical bar plot
# barh : horizontal bar plot
# hist : histogram
# box : boxplot
# kde : Kernel Density Estimation plot
# density : same as kde
# area : area plot
# pie : pie plot
# scatter : scatter plot
# hexbin : hexbin plot

tz_counts[:10].plot(kind='bar', rot=90)  # plot 1
plt.show()  # Mandatory to use for pycharm

results = pd.Series([x.split()[0] for x in frame.a.dropna()])
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
print(indexer[:5])
count_subset = agg_counts.take(indexer)[-10:]
print(count_subset)
count_subset.plot(kind='barh', stacked=True)  # plot 2
plt.show()

normed_subset = count_subset.div(count_subset.sum(1), axis=0)
normed_subset.plot(kind='barh', stacked=True)  # plot 3
plt.show()
