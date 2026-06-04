from scripts.load_data import load_data
from scripts.clean_data import clean_data
from scripts.split_data import split_data
from scripts.train_model import train_model
from scripts.evaluate_model import evaluate_model
from scripts.feature_importance import feature_importance
from scripts.save_model import save_model

def main():

    path_csv = "data/diabetes.csv"

    df = load_data(path_csv)
    df = clean_data(df)
    X, X_train, X_test, y_train, y_test = split_data(df)
    model = train_model(X_train, y_train)
    evaluate_model(X_test, y_test, model)
    feature_importance(X, model)
    save_model(model)

if __name__ == "__main__":
    main()
