import pandas
import pandas as pd
from sqlalchemy import create_engine
from app.config import config


def load_data():
    return pandas.read_csv("data.csv")


def save_data(filename: str):

    data = pd.read_csv(filename)

    engine = create_engine(
        f"postgresql://{config.POSTGRES_USER}:{config.POSTGRES_PASSWORD}@{config.POSTGRES_SERVER}/{config.POSTGRES_DB}"
    )

    # Save data to PostgreSQL
    data.to_sql("table_name", engine, if_exists="replace", index=False)
