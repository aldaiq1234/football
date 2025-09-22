USE football;

-- 1. Топ-10 самых дорогих игроков
SELECT '=== 1. Топ-10 самых дорогих игроков ===' AS Info;
SELECT name, market_value_in_eur
FROM players
WHERE market_value_in_eur IS NOT NULL
ORDER BY market_value_in_eur DESC
LIMIT 10;

-- 2. Топ-10 клубов по общей стоимости состава
SELECT '=== 2. Топ-10 клубов по общей стоимости состава ===' AS Info;
SELECT c.name AS club_name, SUM(v.market_value_in_eur) AS total_value
FROM player_valuations v
JOIN clubs c ON v.current_club_id = c.club_id
GROUP BY c.name
ORDER BY total_value DESC
LIMIT 10;

-- 3. Топ-10 самых дорогих трансферов
SELECT '=== 3. Топ-10 самых дорогих трансферов ===' AS Info;
SELECT player_name, from_club_name, to_club_name, transfer_fee
FROM transfers
WHERE transfer_fee IS NOT NULL
ORDER BY transfer_fee DESC
LIMIT 10;

-- 4. Топ-10 бомбардиров
SELECT '=== 4. Топ-10 бомбардиров ===' AS Info;
SELECT p.name, COUNT(e.game_event_id) AS total_goals
FROM game_events e
JOIN players p ON e.player_id = p.player_id
WHERE e.type = 'Goals'
GROUP BY p.name
ORDER BY total_goals DESC
LIMIT 10;

-- 5. Топ-10 игроков по жёлтым карточкам
SELECT '=== 5. Топ-10 игроков по жёлтым карточкам ===' AS Info;
SELECT player_name, SUM(yellow_cards) AS total_yellow
FROM appearances
GROUP BY player_name
ORDER BY total_yellow DESC
LIMIT 10;

-- 6. Топ-10 игроков по красным карточкам
SELECT '=== 6. Топ-10 игроков по красным карточкам ===' AS Info;
SELECT player_name, SUM(red_cards) AS total_red
FROM appearances
GROUP BY player_name
ORDER BY total_red DESC
LIMIT 10;

-- 7. Топ-10 клубов по проценту побед (если сыграли > 50 матчей)
SELECT '=== 7. Топ-10 клубов по проценту побед (если сыграли > 50 матчей) ===' AS Info;
SELECT c.name,
       SUM(cg.is_win) * 100.0 / COUNT(cg.game_id) AS win_percentage,
       COUNT(cg.game_id) AS total_games
FROM clubs c
JOIN club_games cg ON c.club_id = cg.club_id
GROUP BY c.name
HAVING COUNT(cg.game_id) > 50
ORDER BY win_percentage DESC
LIMIT 10;

-- 8. Средняя посещаемость по сезонам
SELECT '=== 8. Средняя посещаемость по сезонам ===' AS Info;
SELECT season, AVG(attendance) AS avg_attendance
FROM games
WHERE attendance IS NOT NULL
GROUP BY season
ORDER BY season;

-- 9. Топ-10 стадионов по средней посещаемости
SELECT '=== 9. Топ-10 стадионов по средней посещаемости ===' AS Info;
SELECT stadium, AVG(attendance) AS avg_attendance
FROM games
WHERE attendance IS NOT NULL
GROUP BY stadium
ORDER BY avg_attendance DESC
LIMIT 10;

-- 10. Топ-10 стран по количеству игроков
SELECT '=== 10. Топ-10 стран по количеству игроков ===' AS Info;
SELECT country_of_citizenship, COUNT(*) AS total_players
FROM players
GROUP BY country_of_citizenship
ORDER BY total_players DESC
LIMIT 10;
