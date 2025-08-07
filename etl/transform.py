import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.dropna(subset=["item"])
    df.loc[df["discount_applied"].isna(), "discount_applied"] = False
    return df