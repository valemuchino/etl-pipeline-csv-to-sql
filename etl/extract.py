from pathlib import Path
import pandas as pd

def extract_data(file_path: str) -> pd.DataFrame:
    dataset_path = Path(file_path)
    dataset_schema: dict[str, str] = {
        "Transaction ID": "string",
        "Customer ID": "string",
        "Category": "string",
        "Item": "string",
        "Price Per Unit": 'float',
        "Quantity": 'float',
        "Total Spent": 'float',
        "Payment Method": "string",
        "Location": "string",
        "Discount Applied": "boolean",
    }
    df: pd.DataFrame = pd.read_csv(dataset_path, parse_dates = ["Transaction Date"], date_format = "%Y-%m-%d", dtype = dataset_schema)
    return df