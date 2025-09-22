import pandas as pd
import pymysql

# Подключение к базе
conn = pymysql.connect(
    host="localhost",
    user="root",              # твой логин MySQL
    password="Allaadil2005@",   # твой пароль MySQL
    database="football",
    charset="utf8mb4"
)

# Список SQL-запросов (можно вставить свои 10, но для примера возьмём 3)
queries = {
    "top_players": """
        SELECT name, market_value_in_eur
        FROM players
        ORDER BY market_value_in_eur DESC
        LIMIT 10;
    """,
    "top_clubs": """
        SELECT c.name, SUM(v.market_value_in_eur) AS total_value
        FROM player_valuations v
        JOIN clubs c ON v.current_club_id = c.club_id
        GROUP BY c.name
        ORDER BY total_value DESC
        LIMIT 10;
    """,
    "top_countries": """
        SELECT country_of_citizenship, COUNT(*) AS total_players
        FROM players
        GROUP BY country_of_citizenship
        ORDER BY total_players DESC
        LIMIT 10;
    """
}

# Выполняем и сохраняем результаты
for title, query in queries.items():
    print(f"\n=== {title} ===")
    df = pd.read_sql(query, conn)
    print(df)  # вывод в терминал
    df.to_csv(f"{title}.csv", index=False, encoding="utf-8-sig")  # сохраняем в CSV
    df.to_excel(f"{title}.xlsx", index=False)  # сохраняем в Excel

conn.close()
