# src/data_loader.py
import pandas as pd
import os

def load_keel_dataset(path: str) -> pd.DataFrame:
    """
    Load a KEEL-format .dat file, skip metadata, return a cleaned DataFrame.
    Raises FileNotFoundError if the file doesn't exist.
    """
    if not os.path.isfile(path):
        raise FileNotFoundError(f"No such data file: {path!r}")
    with open(path, 'r') as f:
        lines = f.readlines()

    data_start = False
    rows = []
    for line in lines:
        line = line.strip()
        if not data_start:
            if line.lower() == '@data':
                data_start = True
            continue
        if line:
            parts = [x if x != '?' else None for x in line.split(',')]
            rows.append(parts)

    df = pd.DataFrame(rows)
    return df.apply(pd.to_numeric, errors='coerce').dropna()
