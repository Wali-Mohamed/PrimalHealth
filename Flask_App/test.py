import psycopg2

try:
    conn = psycopg2.connect(
        host="localhost",
        database="primal_health",
        user="postgres",
        password="your_password",
        port="7777"
    )
    print("Connection successful")
    conn.close()
except Exception as e:
    print(f"Error: {e}")
