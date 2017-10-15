import pandas
from scipy import stats

smInInch = 2.54

minHeight = 170 / smInInch # минимальный рост в дюймах
maxHeight = 180 / smInInch # максимальный --//--
# вес - в фунтах

data = pandas.read_csv('hw_25000.csv', delimiter=';', names = ['index', 'height', 'weight'], header = 1)
sample = data[(data['height'] >= minHeight) & (data['height'] <= maxHeight)].head(20) # колонка с весом 20 человек больше 170 и менее 180 см

# Cмотрим на средний вес нашей выборки и всех данных
# Вывод: 132.92411 127.07942116079916
print(sample['weight'].mean(), data['weight'].mean())


# Одновыборочный критерий
# Ttest_1sampResult(statistic=2.2438433326713279, pvalue=0.036952752151255777)
print(stats.ttest_1samp(sample['weight'], data['weight'].mean()))

# Двухвыборочный критерий
# Ttest_indResult(statistic=2.2406349413640894, pvalue=0.02505847065887213)
print(stats.ttest_ind(sample['weight'], data['weight']))


# Различие значимо, так как Pvalue меньше 0.05 в обеих случаях
