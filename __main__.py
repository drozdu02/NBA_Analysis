from nba.NBARepository import NBARepository

file = open("data/nba_salaries.csv")

nbaRepo = NBARepository(file)

salaries = nbaRepo.find({"select": ["Salary", "Position"]})
position_count = nbaRepo.countColumn("Position")

position_average_salaries = []
for pos_count in position_count:

    average_item = {}
    salary_sum = 0

    for salary in salaries:
        
        if salary["Position"] == pos_count["Position"]:
            salary_sum += int(salary["Salary"])

    average_item = {"Position": pos_count["Position"], "Average": salary_sum // pos_count["count"]}
    position_average_salaries.append(average_item) 


for row in position_average_salaries:
    print(row)


team = nbaRepo.find({"select": ["Salary", "Team"]})
team_count = nbaRepo.countColumn("Team")

team_avarage_salaries = []
for t_count in team_count:


    average_item = {}
    salary_sum = 0

    for salary in team:

        if salary["Team"] == t_count["Team"]:
            salary_sum += int(salary["Salary"])
    
    average_item = {"Team": t_count["Team"], "Salary Per Team": salary_sum // t_count["count"]}
    team_avarage_salaries.append(average_item)


for row in team_avarage_salaries:
    print(row)


minute = nbaRepo.find({"select": ["Salary", "MP"]})
minutes_count = nbaRepo.countColumn("MP")

salary_per_minute = []
for minute_count in minutes_count:


    average_item = {}
    salary_sum = 0
   
    for salary in minute_count:

        if salary["MP"] == minute_count["MP"]:
            salary_sum += int(salary["MP"])
    
    average_item = {"MP":minute_count["MP"], "Salary Per Minute": salary_sum // minute_count["count"]}
    salary_per_minute.append(average_item)

for row in salary_per_minute:
    print(row)


points_per_game = nbaRepo.find({"select": ["Salary", "Team"]})
points_per_game_count = nbaRepo.countColumn(["PTS"])

salary_PTS = []
for pts in points_per_game_count:


    average_item = {}
    team = 0

    for salary in pts:

        if salary["PTS"] == pts["PTS"]:
            team += int(salary["PTS"])

    average_item = {"PTS":pts["PTS"], "Team": team["count"]}
    salary_PTS.append(average_item)

for row in salary_PTS:
    print(row)



avg_age_team = nbaRepo.find({"select": ["Team", "Age"]})
team_count = nbaRepo.countColumn("Team")

team_counter = []
for team in team_count:

    average_item = {}
    team_1 = 0

    for age in team:

        if age["Team"] == team["Team"]:
            team_1 += int(age["Team"])
    
    average_item = {"Team": team["Team"], "Avarage age per team": age // team_count["count"]  }
    team_counter.append(average_item)

for row in team_counter:
    print(row)




