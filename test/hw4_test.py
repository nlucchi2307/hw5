# test/test_hw4.py
import sys
import os
# Add the hw5 directory (where hw4.py is located) to the Python path
sys.path.insert(0, r'C:\Users\marta\hw5')

import pytest
from hw4 import count_simba, get_day_month_year, compute_distance, sum_general_int_list
from datetime import date
import pandas as pd

def test_count_simba():
    data = ["Simba and Nala are lions.", 
            "I laugh in the face of danger.",
            "Hakuna matata", 
            "Timon, Pumba and Simba are friends, but Simba could eat the other two."]
    result = count_simba(data)
    assert result == 3

def test_get_day_month_year():
    data = [date(2000, 7, 23), date(1999, 1, 7), date(2005, 6, 20)]
    result = get_day_month_year(data)
    expected = pd.DataFrame({
        'day': [23, 7, 20],
        'month': [7, 1, 6],
        'year': [2000, 1999, 2005]
    })
    pd.testing.assert_frame_equal(result, expected)

def test_compute_distance():
    data = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
    result = compute_distance(data)
    expected = [31.131865222052042, 157.005827868894]
    assert result == pytest.approx(expected, rel=1e-3)

def test_sum_general_int_list():
    data = [[2], 3, [[1, 2], 5]]
    result = sum_general_int_list(data)
    assert result == 13 
