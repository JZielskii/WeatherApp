import pandas as pd
import os
from common.config import AppConfig

FILE = AppConfig.FILENAME

def save_to_excel(dataset):
    try:
        new_df = pd.DataFrame(dataset)

        if os.path.exists(FILE):
            old_df = pd.read_excel(FILE)
            df = pd.concat([old_df,new_df])
        else:
            df = new_df
        df.to_excel(FILE, index = False)

        print(f"Dane zostały zapisane w  pliku {FILE}")

    except Exception as e:
        print(e)

def read_excel(filename):
    try:
        if not filename.endswith(".xlsx"):
            print("Plik nie ma rozszerzenia .xlsx")
            return

        read_df = pd.read_excel(filename)
        return read_df
    except Exception as e:
        print(e)