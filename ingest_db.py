import pandas as pd
from sqlalchemy import create_engine
import logging
import time
import os

# ---------------------------
# Setup logging
# ---------------------------
script_dir = os.getcwd()
log_file = os.path.join(script_dir, "upload_log.log")
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# ---------------------------
# Database connection
# ---------------------------
engine = create_engine("mysql+pymysql://root:Eshika@127.0.0.1:3306/banking_case")

# ---------------------------
# Upload loop
# ---------------------------
for file in os.listdir('data'):
    try:
        start_time = time.time()

        # Read CSV
        df = pd.read_csv("data/"+file)

        # Table name = file name without extension
        table_name = os.path.splitext(os.path.basename(file))[0]

        # Upload to MySQL
        df.to_sql(
            name=table_name,
            con=engine,
            if_exists="replace",
            index=False
        )

        elapsed = time.time() - start_time
        logging.info(f"SUCCESS: {file} → {table_name} | Rows: {len(df)} | Time: {elapsed:.2f} sec")

        print(f"Uploaded {file} in {elapsed:.2f} sec")

    except Exception as e:
        logging.error(f"FAILED: {file} | Error: {e}")
        print(f"Error uploading {file}: {e}")

print("All uploads completed. Check logs for details.")