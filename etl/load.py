import os
import pandas as pd
from sqlalchemy import Engine, create_engine
from dotenv import load_dotenv

load_dotenv()

db_name: str | None = os.getenv("POSTGRES_DB")
db_user: str | None = os.getenv("POSTGRES_USER")
db_password: str | None = os.getenv("POSTGRES_PASSWORD")
db_host: str | None = os.getenv("DB_HOST")
db_port: str | None = os.getenv("DB_PORT")

db_url: str = f"postgresql://{db_user}:{db_password}@{db_host}/{db_name}"


def load_data(df: pd.DataFrame, table_name: str, db_url: str = db_url) -> None:
    engine: Engine = create_engine(db_url)
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"Data loaded into {table_name} table successfully.")
    engine.dispose()
