from pybaseball import *

date_start = "2024-03-28"
data_end = None

df_batting = batting_stats_range(date_start, data_end)
df_batting = df_batting[df_batting["Tm"] == "St. Louis"]
print(f"\nBatting Stats - Cardinals Players - {date_start} to {data_end}")
print(df_batting)

print()

df_pitching = pitching_stats_range(date_start, data_end)
df_pitching = df_pitching[df_pitching["Tm"] == "St. Louis"]
print(f"\nPitching Stats - Cardinals Players - {date_start} to {data_end}")
print(df_pitching)


print()

df_STL = schedule_and_record(2024, "STL")
print("\nAll Season by-Game Box-Score - Cardinals")
print(df_STL)

print()

df_STL_logs = team_game_logs(2024, "STL", "batting")
print("\nBatting Game Logs - Cardinals")
print(df_STL_logs)


