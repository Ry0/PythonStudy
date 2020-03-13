import tsfresh.feature_extraction.feature_calculators as feature_calculators
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

timeline = np.arange(10000)

data = np.sin(timeline / 100) + np.cos((timeline / 100) * 3) + \
    (np.random.rand(len(timeline))) * 0.2

plt.plot(timeline[:1000], data[:1000])
plt.xlabel('time')
plt.ylabel('data')
plt.show()


range_data = data[:600]

mean_abs_change = feature_calculators.mean_abs_change(data)
# 前後のポイント間での差分の平均値
# np.mean(np.abs(np.diff(x))) と等しい

first_location_of_maximum = feature_calculators.first_location_of_maximum(data)
# 最大値が観測される位置

fft_aggregated = feature_calculators.fft_aggregated(
    data, [{'aggtype': 'skew'}])
# フーリエ変換

number_peaks = feature_calculators.number_peaks(data[:1000], 50)
# ピークの数

index_mass_quantile = feature_calculators.index_mass_quantile(
    data[:1000], [{'q': 0.5}, {'q': 0.1}])
# パーセンタイル処理

linear_trend = feature_calculators.linear_trend(
    range_data, [{'attr': "slope"}, {'attr': 'intercept'}, {'attr': 'rvalue'}])
# 単純なトレンド分析。attrに関しては下記を参照
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html

autocorrelation = feature_calculators.autocorrelation(data, 100)
# 自己相関の計算

plt.plot(fft_aggregated)
plt.show()
