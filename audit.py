import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("Billing-Auditor")

def run_cost_anomaly_audit(csv_path: str, threshold: float = 2.5) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    df['rolling_mean'] = df['daily_spend'].rolling(window=7, min_periods=1).mean()
    df['rolling_std'] = df['daily_spend'].rolling(window=7, min_periods=1).std().fillna(1.0)
    df['z_score'] = (df['daily_spend'] - df['rolling_mean']) / df['rolling_std']
    return df[df['z_score'].abs() > threshold]

if __name__ == "__main__":
    pass

# Refactored update: stage 3 checkpoint - 2026-04-17
