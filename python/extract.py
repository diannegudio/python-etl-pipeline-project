from pathlib import Path

import pandas as pd


# Locate the project directory
PROJECT_DIR = Path(__file__).resolve().parent.parent
RAW_DATA_DIR = PROJECT_DIR / "data" / "raw"


def extract_data():
    """Read raw e-commerce CSV files into pandas DataFrames."""

    files = {
        "customers": "customers.csv",
        "products": "products.csv",
        "orders": "orders.csv",
        "order_items": "order_items.csv",
        "payments": "payments.csv",
    }

    data = {}

    for table_name, filename in files.items():
        file_path = RAW_DATA_DIR / filename

        if not file_path.exists():
            raise FileNotFoundError(
                f"CSV file not found: {file_path}"
            )

        df = pd.read_csv(file_path)
        data[table_name] = df

        print(
            f"{table_name}: {len(df)} rows extracted"
        )

    return data


if __name__ == "__main__":
    extracted_data = extract_data()

    for table_name, df in extracted_data.items():
        print(f"\n{table_name} preview:")
        print(df.head())
