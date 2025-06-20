import random

def main():
    
    # A list of 20 teams in the 24/25 La Liga Season
    teams = ["Deportivo Alaves", "Atletic Club", "Atletico Madrid", "FC Barcelona", "Celta Vigo", "Espanyol", "Getafe", "Girona", "Las Palmas", "Leganes", "Mallorca", "Osasuna", "Rayo Vallecano", "Real Betis", "Real Madrid", "Real Sociedad", "Sevilla", "Valencia", "Real Vallodolid", "Villareal"]
    num_team = len(teams)
    
    
    # The numbers represent the 29 matchday expected goals, and goals conceded per match, the numbers will be use to simulate the entire season of the 24/25 season
    expected_goals = [1.23, 1.54, 1.42, 1.92, 1.35, 1.01, 1.22, 1.26, 1.21, 0.99, 1.26, 1.24, 1.47, 1.57, 1.86, 1.23, 1.33, 1.22, 1.05, 1.62]
    goals_conceded_per_match = [1.52, 0.83, 0.79, 0.97, 1.45, 1.43, 0.86, 1.55, 1.66, 1.59, 1.21, 1.45, 1.07, 1.24, 1.00, 1.07, 1.34, 1.59, 2.24, 1.39]

    # The placeholder for all teams
    games_played = [0] * num_team
    goals_scored = [0] * num_team  
    goals_conceded = [0] * num_team
    points = [0] * num_team
    
    # There are 38 games in a season, the user will input the 1 to 38 games to simulate the season
    while True:
        
        try:
            
            games_per_team = int(input("How many games should each team play? (1 - 38): "))
            if 1 <= games_per_team <= 38:
                
                break
            
            print("Enter the number between 1 and 38")
            
        except Exception:
            
            print("Invalid. Please enter the number 1 and 38")
    
    
    # Calls all function into the main function
    matches(teams, expected_goals, goals_conceded_per_match, points, games_played, goals_scored, goals_conceded, games_per_team)
    
    goal_differences = [goals_scored - goals_conceded for goals_scored, goals_conceded in zip(goals_scored, goals_conceded)]
    
    table(teams, goals_scored, goals_conceded, goal_differences, points, games_played)
    
    cont()


# The matches() function will calculate the matches, goal scored, goals conceded and points awarded by the teams
def matches(teams, expected_goals, goals_conceded_per_match, points, games_played, goals_scored, goals_conceded, games_per_team):
    
    num_team = len(teams)
    
    
    # The for loop will simulate all 38 matches for the 20 teams (the team cannot play itself).
    for home_x in range(num_team):
        
        for away_x in range(num_team):
            
            if home_x == away_x:
                continue
            
            if games_played[home_x] >= games_per_team or games_played[away_x] >= games_per_team:
                
                continue
            
            # The statistical attack and defense of each team
            home_attack = expected_goals[home_x]
            home_defense = goals_conceded_per_match[home_x]
            
            away_attack = expected_goals[away_x]
            away_defense = goals_conceded_per_match[away_x]
            
            # Random Generated normal distribution of goals scored based of their expected goals multiply by goals conceded per match
            home_goals = round(random.gauss(home_attack * away_defense, 1))
            away_goals = round(random.gauss(away_attack * home_defense, 1))
            
            #Update the statistic of each team by goals scored, goals conceded and games played.
            goals_scored[home_x] += home_goals
            goals_scored[away_x] += away_goals
            goals_conceded[home_x] += away_goals
            goals_conceded[away_x] += home_goals
            games_played[home_x] += 1
            games_played[away_x] += 1
            
            # the if statement awards 3 points for the winner teams and 1 point for both teams that the match result in a draw (no points awarded by the losing team).
            if home_goals > away_goals:
                
                points[home_x] += 3
                
            elif home_goals < away_goals:
                
                points[away_x] += 3
                
            else:
                
                points[home_x] += 1
                points[away_x] += 1

# The function will draw the table will all parameters
def table(teams, goals_scored, goals_conceded, goal_differences, points, games_played):
    
    
    print("La Liga Table: 24/25 Season")
    print(" ")
    print("Rank  Team                   GP    GS    GC    GD   Pts")
    print("-------------------------------------------------------")

    # The table.data combines all data in a descending order
    table_data = list(zip(teams, games_played, goals_scored, goals_conceded, goal_differences, points))
    table_data.sort(key=lambda x: (x[5], x[4], x[2]), reverse=True)

    for rank, (team, games_played, goals_scored, goals_conceded, goal_differences, points) in enumerate(table_data, 1):
        
        print(f"{rank:<5} {team:<22} {games_played:<5} {goals_scored:<5} {goals_conceded:<5} {goal_differences:<5} {points:<4}")

# The function will call a user input if the user would continue the simulation or end the simulation. 
def cont():
            
    continue_char = input("Do you want to continue (Y/N)? ")
        
    if (continue_char == 'Y') or (continue_char == 'y'):
        print(" ")
        main()
        
    elif (continue_char == 'N') or (continue_char == 'n'):
        print("End Program")
        exit()
    else:
        print("Invalid. Please enter 'Y' or 'N'. ")
        cont()       
        
main()
