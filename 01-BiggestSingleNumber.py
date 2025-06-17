# Problem 1 - Biggest Single Number (https://leetcode.com/problems/biggest-single-number/)
import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    count = my_numbers['num'].value_counts()
    single_numbers = count[count == 1].index

    if single_numbers.empty:
        return pd.DataFrame({'num' : [None]})
    else:
        max_single = my_numbers[my_numbers['num'].isin(single_numbers)]['num'].max()
        return pd.DataFrame({'num' : [max_single]})