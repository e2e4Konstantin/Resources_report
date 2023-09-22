import numpy as np
from pandas import DataFrame, isna

arr = np.array([('5', '1.19-2-3', 'Мощность', '0.75', '0.75', 'кВт', np.nan, '1')], dtype=[('A', 'O'), ('B', 'O'), ('C', 'O'), ('D', 'O'), ('E', 'O'), ('F', 'O'), ('G', 'O'), ('H', 'O')])
print(arr)
options = {x['C']: x['D'] for x in arr}
print(options)

w = [arr[x].item() for x in arr.dtype.names[3:]]
print(w)

z = {x['C']: [arr[x].item() for x in arr.dtype.names[3:]] for x in arr}
print(z)

e = arr.flatten().tolist()
print(e, e[0])
print(type(e), type(e[0]))

e = arr.tolist()
print(e, e[0])
print(type(e), type(e[0]))

option_value = ('0.75', '0.75', 'кВт', np.nan, '1')
option_value = ["" if isna(value) else value for value in option_value]
print(option_value)

# array = options_df.to_records(index=False)
# options = {option_i['C']: [array[value_i].item() for value_i in array.dtype.names[3:]] for option_i in array}

