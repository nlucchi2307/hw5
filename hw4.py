# 1) 
from functools import reduce
def count_simba(data):
    return reduce(lambda a, b: a + b, map(lambda s: s.count("Simba"), data))

data = ["Simba and Nala are lions.", "I laugh in the face of danger.",
           "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

result = count_simba(data)
print(result) 

# 2) 
import pandas as pd
from datetime import date
def get_day_month_year(data):
    day_month_year_list = list(map(lambda d: (d.day, d.month, d.year), data))
    df = pd.DataFrame(day_month_year_list, columns=['day', 'month', 'year'])
    return df

data = [date(2000, 7, 23), date(1999, 1, 7), date(2005, 6, 20)]
df = get_day_month_year(data)
print(df)

# 3) 
from geopy.distance import geodesic
def compute_distance(data):
    return list(map(lambda coords: geodesic(coords[0], coords[1]).km, data))

data = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
distances = compute_distance(data)
print(distances)

# 4) 
def flatten(data):
    return reduce(lambda acc, val: acc + (flatten(val) if isinstance(val, list) else [val]), data, [])

def sum_general_int_list(data):
    flat_list = flatten(data)
    return reduce(lambda x, y: x + y, flat_list)

data = [[2], 3, [[1, 2], 5]]
result = sum_general_int_list(data)
print(result) 
