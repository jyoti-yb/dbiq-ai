from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    features = df[["execution_time", "bytes_scanned", "spill_to_disk"]]

    model = IsolationForest(contamination=0.2, random_state=42)
    df["anomaly"] = model.fit_predict(features)

    return df