import numpy as np
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean dataframe and replace zero's with median

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with zero as values

    Returns
    -------
    pd.DataFrame
        Dataframe without zero as values
    """

    cols = ["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]

    df[cols] = df[cols].replace(0, np.nan)
    df[cols] = df[cols].fillna(df[cols].median())

    return df