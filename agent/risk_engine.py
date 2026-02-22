def calculate_risk(query):
    risk = 0

    if query["execution_time"] > 1800:
        risk += 30

    if query["bytes_scanned"] > 1e12:
        risk += 25

    if query["spill_to_disk"] > 0:
        risk += 30

    if "SELECT *" in query["query_text"]:
        risk += 15

    if query["warehouse_load"] > 80:
        risk += 20

    return min(risk, 100)