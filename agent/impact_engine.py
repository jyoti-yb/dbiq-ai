def calculate_impact(query_row):

    execution_time = query_row["execution_time"]
    bytes_scanned = query_row["bytes_scanned"]
    risk = query_row["risk_score"]

    # simulate AI improvement logic
    time_saved = execution_time * 0.4
    bytes_reduced = bytes_scanned * 0.5
    cost_saved = (bytes_scanned / 1e12) * 5  # fake $ per TB model
    block_prevented = risk > 70

    return {
        "time_saved": time_saved,
        "bytes_reduced": bytes_reduced,
        "cost_saved": cost_saved,
        "block_prevented": block_prevented
    }