import pandas as pd
from feast import FeatureStore

def main():
    store = FeatureStore(repo_path="feature_repo")
    entity_df = pd.read_csv("data/student_data.csv")[["student_id"]]
    features = store.get_historical_features(
        entity_df=entity_df,
        features=[
            "student_features:hours_studied",
            "student_features:attendance_percentage"
        ]
    ).to_df()
    features.to_csv("data/feature_data.csv", index=False)

if __name__ == "__main__":
    main()
