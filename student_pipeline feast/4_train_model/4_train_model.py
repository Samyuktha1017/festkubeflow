import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

def main():
    df = pd.read_csv("data/feature_data.csv")
    X = df[["hours_studied", "attendance_percentage"]]
    y = df["label"].apply(lambda x: 1 if x == "pass" else 0)

    model = RandomForestClassifier()
    model.fit(X, y)

    joblib.dump(model, "data/student_model.pkl")

if __name__ == "__main__":
    main()
