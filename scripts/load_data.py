import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    """Loads CSV into Dataframe

    Parameters
    ----------
    path : str
        Path of the csv file

    Returns
    -------
    pd.DataFrame
        Dataframe of the data
    """

    df = pd.read_csv(path)

    return df
