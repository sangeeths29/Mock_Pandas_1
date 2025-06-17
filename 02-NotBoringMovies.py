# Problem 2 - Not Boring Movies (https://leetcode.com/problems/not-boring-movies/)
import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    odd_number = cinema['id'] % 2 != 0
    not_boring = ~cinema['description'].str.contains('boring')
    df = cinema[odd_number & not_boring].sort_values(by=['rating'], ascending=False)
    return df
