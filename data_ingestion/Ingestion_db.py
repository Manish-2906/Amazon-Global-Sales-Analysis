import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
import os
import time
import logging 

logging.basicConfig(
    filename="logs/Ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)


"""Retrieve database credentials from environment or fallback to defaults"""

username = os.getenv('DB_USER', 'root')
password = os.getenv('DB_PASS', 'password')
host = os.getenv('DB_HOST', 'localhost')
port = os.getenv('DB_PORT', '3306')
database = os.getenv('DB_NAME', 'amazon')


try:    
    engine = create_engine(f"mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}")
    conn = engine.connect()
    print("Successfully connected to the database.")
except Exception as e:
    print("Failed to connect to the database:", e)


def ingested_db(df, table_name, engine):
    try:
        df.to_sql(table_name, con=engine, if_exists="replace", index=False, chunksize=10000, method='multi')
        logging.info(f"Successfully inserted table: {table_name}")
    except Exception as e:
        logging.error(f"Error inserting {table_name}: {e}")

folder_path = "C:/Users/manish/6 Month Iscale/amazon dataset"

def load_raw_data():
    start = time.time()

    for file in os.listdir(folder_path):
        if file.endswith(".xlsx"):
            df = pd.read_excel(os.path.join(folder_path, file))
            table_name = file[:-5]
            logging.info(f"Ingesting: {file}  table: {table_name}")
            ingested_db(df, table_name, engine)  

    end = time.time()
    total = (end - start) / 60

    logging.info("----------------Ingestion Completed------------------")
    logging.info(f"Total time taken: {total:.2f} minutes")


if __name__=="__main__":
    load_raw_data()
    


