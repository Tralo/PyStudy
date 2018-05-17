# coding:utf-8

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

if __name__ == '__main__':
    s = pd.Series([1, 3, 5, np.nan, 6, 8])
    # print(s)

    dates = pd.date_range('20180405',periods=6)
    # print(dates)

    df = pd.DataFrame(np.random.randn(6, 4), index=dates,
                      columns=list('ABCD'))
    # print(df)

    df2 = pd.DataFrame({'A': 1.,
                        'B': pd.Timestamp('20180405'),
                        'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                        'D': np.array([3] * 4, dtype='int32'),
                        'E': pd.Categorical(["test","Train","Test","train"]),
                        'F': 'foo'})
    # print(df2)
    # print(df2.dtypes)

    # print(df)
    # print(df.head())
    # print(df.tail(3))
    # print(df.reindex)
    # print(df.index)
    # print(df.columns)
    # print(df.values)
    # print(df.T)
    # print(df.sort_index(axis=1, ascending=False))

    print(df)
    # print(df['A'])
    # print(df[0:3])
    # print(df['20180406':'20180409'])
    # print(df.loc[dates[0]])
    # print(df.loc[:,['A','B']])
    # print(df.loc['20180406':'20180409',['B','D']])
    # print(df.iloc[3:])
    # print(df.iloc[1:3,0:3])
    # print(df.iloc[[2,4,5],[1,3]])




