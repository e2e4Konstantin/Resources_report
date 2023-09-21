import pandas as pd

index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror']
df = pd.DataFrame({'http_status': [200, 200, 404, 404, 301],
                  'response_time': [0.04, 0.02, 0.07, 0.08, 1.0]}, index=index)

print(df)
print(df.index)
print(pd.RangeIndex(len(df.index)))

# df.index = pd.RangeIndex(len(df.index))

df.index = range(1, len(df.index)+1)
print(df)
print('--')
print(df.loc[:4])
print('--')
print(len(df.index))
print(df.shape[0])
print(df[df.columns[0]].count())



#
#
# new_index = list(range(1,5))
# print(new_index)
# print(df.reindex(new_index))
#
# print(df.reset_index(drop=True))