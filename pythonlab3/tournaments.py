#task2

import csv
import random


def load_teams_from_csv(file_path):
    teams = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            teams.append(row)
    return teams


def simulate_round(teams):
    winners = []
    for i in range(0, len(teams), 2):
        team1 = teams[i]
        team2 = teams[i + 1]

        rating1 = float(team1['rating'])
        rating2 = float(team2['rating'])
        prob_team1_wins = rating1 / (rating1 + rating2)
        
        winner = team1 if random.random() < prob_team1_wins else team2
        winners.append(winner)
    return winners


def simulate_tournament(teams):
    while len(teams) > 1:
        teams = simulate_round(teams)
    return teams[0]


def simulate_multiple_tournaments(teams, num_simulations):
    win_counts = {team['name']: 0 for team in teams}
    
    for _ in range(num_simulations):
        winner = simulate_tournament(teams)
        win_counts[winner['name']] += 1
    
    return win_counts


if __name__ == "__main__":

    file_path = 'teams.csv'  
    teams = load_teams_from_csv(file_path)


    num_simulations = 10000  
    
    results = simulate_multiple_tournaments(teams, num_simulations)


    print(f"Results after simulating {num_simulations} tournaments:")
    for team, count in results.items():
        print(f"{team}: {count} wins")
