import random
import pandas as pd
import time

def generate_fake_query():

    queries = [
        ("SELECT * FROM sales", 3500, 2000000000000, 1, 92),
        ("SELECT id FROM users WHERE id=10", 120, 20000000000, 0, 20),
        ("SELECT * FROM transactions JOIN users", 4200, 1800000000000, 1, 88),
        ("SELECT name FROM customers", 90, 1000000000, 0, 10),
        ("SELECT * FROM orders", 3000, 1500000000000, 1, 85)
    ]

    q = random.choice(queries)

    return {
        "query_id": f"Q{random.randint(200,999)}",
        "user": "live_user",
        "execution_time": q[1],
        "bytes_scanned": q[2],
        "spill_to_disk": q[3],
        "warehouse_load": random.randint(30,95),
        "query_text": q[0]
    }


def stream_queries(df):

    new_query = generate_fake_query()
    df = pd.concat([df, pd.DataFrame([new_query])], ignore_index=True)

    return df