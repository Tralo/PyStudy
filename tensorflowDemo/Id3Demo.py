# coding:utf-8
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC,export_graphviz

if __name__ == '__main__':
    data = pd.read_csv('./data/titanic_data.csv', encoding='utf-8')
    data.drop(['PassengerId'], axis=1, inplace=True)
    data.loc[data['Sex'] == 'male', 'Sex'] = 1
    data.loc[data['Sex'] == 'female', 'Sex'] = 0
    # print(data)
    data.fillna(int(data.Age.mean()), inplace=True)
    # print(data)
    X = data.iloc[:, 1:3]
    # print(X)
    y = data.iloc[:,0]

    dtc = DTC(criterion='entropy')
    dtc.fit(X, y)
    print('输出准确率:  ',dtc.score(X, y))

    with open('./tree.dot','w') as f:
        f = export_graphviz(dtc, feature_names=X.columns, out_file=f)








