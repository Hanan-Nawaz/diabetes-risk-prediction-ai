import pandas as pd

def feature_importance(X, model):

    feature_imp = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values(
        by="Importance",
        ascending=False
    )

    feature_imp.to_csv(
        "results/feature_importance.csv",
        index=False
    )