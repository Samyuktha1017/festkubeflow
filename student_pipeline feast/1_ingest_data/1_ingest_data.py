import pandas as pd

def main():
    df = pd.read_csv("data/student_data.csv")
    print("Student Data:")
    print(df)

if __name__ == "__main__":
    main()
