import pandas as pd

xn = pd.NA
print(xn)


index = ['Firefox', 'Chrome', 'Safari', 'IE10', 'Konqueror', 'A']
df = pd.DataFrame({ 'http_status': [200, 200, 404, 404, 301, 301],
                    'response_time': [0.04, 0.02, 0.07, 0.08, 1.0, 0.03],
                    'text': ['0.04', '0.02', xn, '0.02', '1.0', '1.0']
                   }, index=index)

print(df)
print(df.index)
print(pd.RangeIndex(len(df.index)))

x = df['text'].value_counts()
print(x)
y = df['text'].value_counts()['0.02']
print(y)
print(df['text'].value_counts().get('0.025', 0))



#
# print(df[df['http_status'] == 404])
# print('\n')
# print(df[df['text'].str.fullmatch(pat=r"\d+\.\d2")])
# print('\n')
# a = 0.02
# val = f"{a}"
# print(df[df['text'].str.fullmatch(pat=val)])
# print()
# print(df[df['text'] == "0.07"])
# print()
# print(df['text'].str.strip() == "0.07")
# print()
# print(df['text'].str.strip().str.fullmatch(pat=f"{a}"))






