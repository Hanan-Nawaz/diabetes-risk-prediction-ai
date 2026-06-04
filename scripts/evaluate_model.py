from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, roc_auc_score
import pandas as pd

def evaluate_model(X_test, y_test, model):

    # Predictions
    y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_prob)

    # Classification report -> DataFrame
    report = classification_report(
        y_test,
        y_pred,
        output_dict=True
    )

    report_df = pd.DataFrame(report).transpose()

    # Confusion matrix -> DataFrame
    cm = confusion_matrix(y_test, y_pred)

    cm_df = pd.DataFrame(
        cm,
        index=["Actual_No", "Actual_Yes"],
        columns=["Pred_No", "Pred_Yes"]
    )

    # Summary metrics
    metrics_df = pd.DataFrame({
        "Metric": ["Accuracy", "ROC_AUC"],
        "Value": [accuracy, auc]
    })

    # Save
    report_df.to_csv("results/classification_report.csv")
    cm_df.to_csv("results/confusion_matrix.csv")
    metrics_df.to_csv("results/model_metrics.csv")
