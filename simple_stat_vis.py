import pandas as pd
import matplotlib.pyplot as plt
import prefectures

# Visualizing resampled search data
search = pd.read_csv('./5%_search.csv')
search.info()

search.index = pd.to_datetime(search['created'])
search_groupby_day = search.groupby(pd.Grouper(freq='D'))
s_count_by_d = search_groupby_day.count()['created']
s_count_by_d.plot(xlabel="day",ylabel="count", linewidth=0.7, color='orange');

plt.title('# of searches by day')
plt.show()


print(prefectures.prefecture)

