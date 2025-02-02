import pandas as pd


def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Функція для створення нових ознак

    Inputs:
    df (pd.DataFrame): Вхідний датафрейм.
    label (str, optional): Назва стовпця, який є цільовою змінною.

    Output:
    pd.DataFrame: DataFrame з новими стовпцями ознак.

    """
    df['dayofweek'] = df['date'].dt.dayofweek
    df['quarter'] = df['date'].dt.quarter
    df['month'] = df['date'].dt.month
    df['dayofmonth'] = df['date'].dt.day
    df['weekofyear'] = df['date'].dt.isocalendar().week

    X = df[['dayofweek', 'quarter', 'month', 'dayofmonth', 'weekofyear', 'category_id', 'sales_price']]

    return X
