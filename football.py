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
    # 1. Топ-10 игроков по рыночной стоимости
    "top_players": """
        SELECT name, market_value_in_eur
        FROM players
        ORDER BY market_value_in_eur DESC
        LIMIT 10;
    """,

    # 2. Топ-10 клубов по суммарной стоимости игроков
    "top_clubs": """
        SELECT c.name, SUM(v.market_value_in_eur) AS total_value
        FROM player_valuations v
        JOIN clubs c ON v.current_club_id = c.club_id
        GROUP BY c.name
        ORDER BY total_value DESC
        LIMIT 10;
    """,

    # 3. Топ-10 стран по количеству игроков
    "top_countries": """
        SELECT country_of_citizenship, COUNT(*) AS total_players
        FROM players
        GROUP BY country_of_citizenship
        ORDER BY total_players DESC
        LIMIT 10;
    """,

    # 4. Игроки с наибольшим количеством голов
    "top_scorers": """
        SELECT p.name, COUNT(g.goal_id) AS goals
        FROM goals g
        JOIN players p ON g.player_id = p.player_id
        GROUP BY p.name
        ORDER BY goals DESC
        LIMIT 10;
    """,

    # 5. Клубы с наибольшим количеством побед
    "top_winning_clubs": """
        SELECT c.name, SUM(CASE WHEN cg.is_win=1 THEN 1 ELSE 0 END) AS wins
        FROM clubs c
        JOIN club_games cg ON c.club_id = cg.club_id
        GROUP BY c.name
        ORDER BY wins DESC
        LIMIT 10;
    """,

    # 6. Игроки младше 21 года с наибольшей стоимостью
    "young_top_players": """
        SELECT name, age, market_value_in_eur
        FROM players
        WHERE age < 21
        ORDER BY market_value_in_eur DESC
        LIMIT 10;
    """,

    # 7. Средний возраст игроков по клубам
    "average_age_by_club": """
        SELECT c.name, ROUND(AVG(p.age), 2) AS avg_age
        FROM players p
        JOIN clubs c ON p.club_id = c.club_id
        GROUP BY c.name
        ORDER BY avg_age ASC;
    """,

    # 8. Сравнение результативности игроков в домашних и выездных матчах
    "player_home_away_goals": """
        SELECT p.name,
               SUM(CASE WHEN m.home_club_id = p.club_id THEN g.goal_id ELSE 0 END) AS home_goals,
               SUM(CASE WHEN m.away_club_id = p.club_id THEN g.goal_id ELSE 0 END) AS away_goals
        FROM players p
        JOIN goals g ON p.player_id = g.player_id
        JOIN matches m ON g.match_id = m.match_id
        GROUP BY p.name
        ORDER BY (home_goals + away_goals) DESC
        LIMIT 10;
    """,

    # 9. Лиги с наибольшей средней стоимостью игроков
    "league_avg_value": """
        SELECT c.league, ROUND(AVG(v.market_value_in_eur), 2) AS avg_value
        FROM player_valuations v
        JOIN clubs c ON v.current_club_id = c.club_id
        GROUP BY c.league
        ORDER BY avg_value DESC
        LIMIT 10;
    """,

    # 10. Игроки с наибольшим количеством карточек
    "most_cards_players": """
        SELECT p.name, COUNT(c.card_id) AS total_cards
        FROM cards c
        JOIN players p ON c.player_id = p.player_id
        GROUP BY p.name
        ORDER BY total_cards DESC
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

