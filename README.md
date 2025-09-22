The project of the course work: analysis of the database of football players, matches and clubs.

## Project goal
- Create a database of football players, clubs and matches.
- Analyze statistics of players and teams using SQL.
- Visualize the results and export them to Python.
- Prepare conclusions on various metrics (for example, the cost of players, the effectiveness of clubs and players).

## Repository structure
- `queries.sql' — 10 SQL queries for database analysis.
- `football.py ` is a Python script for connecting to MySQL, executing queries, and saving results.
- `screenshots/` — screenshots of query execution and results.
- 'er_diagram.png' is an ER diagram of the database to see the relationships of the tables.
- `data/csvfile.csv' is a small example of data for testing the script.

## Contents of SQL queries
Examples of queries that are included in `queries.sql`:
1. Top 10 football players by market value.
2. The total cost of players by club.
3. The players with the most goals.
4. The clubs with the most wins.
5. The players under 21 with the most potential.
6. The average age of players by club.
7. Comparison of players' performance in home and away matches.
8. The leagues with the highest average player value.
9. The players with the most cards.
10. The clubs with the most wins in a season.

*(Full SQL queries are located in `queries.sql'.)*

####  Основные таблицы футбольной базы

Для анализа игроков, клубов и матчей база данных содержит следующие основные таблицы:

| Таблица            | Основные поля                                         | Связи                                               |
|-------------------|------------------------------------------------------|---------------------------------------------------|
| `players`         | `player_id`, `name`, `age`, `position`, `nationality` | Связь с `clubs` через `club_id` и с `player_valuations` |
| `clubs`           | `club_id`, `name`, `league`, `country`              | Связь с `players` и с `matches`                 |
| `matches`         | `match_id`, `date`, `home_club_id`, `away_club_id`, `home_score`, `away_score` | Связь с `clubs` для домашних и выездных команд |
| `player_valuations` | `valuation_id`, `player_id`, `current_club_id`, `market_value_in_eur`, `date` | Связь с `players` и `clubs`                     |
| `goals` (опционально) | `goal_id`, `match_id`, `player_id`, `minute`      | Связь с `players` и `matches`                  |
| `cards` (опционально) | `card_id`, `match_id`, `player_id`, `type`       | Связь с `players` и `matches`                  |

---
![5368719467032479586](https://github.com/user-attachments/assets/9b302515-2557-4906-96a9-2b37d868d961)

##  Docker and project launch

Docker is used to run the entire project conveniently. This allows you to work with the project without installing Python and all dependencies on a local computer. It is enough to build a Docker image that contains all the necessary libraries and project files, and launch the container. Using a container, the Python script automatically connects to the database, executes all SQL queries, and saves the results in a separate folder. This approach ensures the same working environment on any machine and simplifies project portability.

![5370971266846161470](https://github.com/user-attachments/assets/6a46b524-bce7-42d6-a19d-fbe76210c627)

## Secret key and security

All data for connecting to the database and secret keys are stored in a separate Python file. It contains:

- login and password to the database,
- database server address,
- database name,
- a secret key for the internal needs of the project
![5370971266846161473](https://github.com/user-attachments/assets/7f0b195a-af21-4212-a113-ae0f18592a36)


