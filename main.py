from pandas import DataFrame
from etl.extract import extract_data
from etl.transform import clean_data
# from etl.load import load_data

def run_pipeline() -> None:
    df: DataFrame = extract_data("dataset/retail_store_sales.csv")
    df_clean: DataFrame = clean_data(df)
    print(df_clean)

if __name__ == "__main__":
    run_pipeline()