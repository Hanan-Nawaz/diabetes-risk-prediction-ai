from sklearn.model_selection import train_test_split
import pandas as pd

def split_data(df: pd.DataFrame):
    """Split data into train and test

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame
    """

    X = df.drop("Outcome", axis=1)
    y = df["Outcome"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

    return X_train, X_test, y_train, y_test