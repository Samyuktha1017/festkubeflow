import pandas as pd
from feast import FeatureStore

def main():
    store = FeatureStore(repo_path="feature_repo")
    store.apply()

if __name__ == "__main__":
    main()
