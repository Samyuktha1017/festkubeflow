import argparse
import json
import os
import joblib
import pandas as pd
from sklearn.metrics import accuracy_score

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    parser.add_argument("--X_test", type=str, required=True)
    parser.add_argument("--y_test", type=str, required=True)
    parser.add_argument("--predictions", type=str, required=True)
    parser.add_argument("--accuracy", type=str, required=True)
    args = parser.parse_args()

    # Load model and test data
    model = joblib.load(args.model)
    with open(args.X_test, "r") as f:
        X_test = pd.DataFrame(json.load(f))
    with open(args.y_test, "r") as f:
        y_test = json.load(f)

    # Predict and calculate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    # Ensure output directory exists
    os.makedirs(os.path.dirname(args.predictions), exist_ok=True)
    os.makedirs(os.path.dirname(args.accuracy), exist_ok=True)

    # Save outputs
    with open(args.predictions, "w") as f:
        json.dump(y_pred.tolist(), f)
    with open(args.accuracy, "w") as f:
        f.write(str(accuracy))

if __name__ == "__main__":
    main()
