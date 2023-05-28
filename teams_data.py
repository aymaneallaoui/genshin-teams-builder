# Importing necessary libraries
import json

# Reading the JSON file
with open('characters.json') as file:
    data = json.load(file)

# Defining a function to calculate the total talent level of a character
def total_talent_level(character):
    return character['talent']['auto'] + character['talent']['skill'] + character['talent']['burst']

# Defining a function to calculate the team score
def team_score(team):
    score = 0
    for character in team:
        score += total_talent_level(character)
    return score

# Finding all possible team combinations
all_teams = []
for i in range(len(data['characters'])):
    for j in range(i+1, len(data['characters'])):
        for k in range(j+1, len(data['characters'])):
            for l in range(k+1, len(data['characters'])):
                team = [data['characters'][i], data['characters'][j], data['characters'][k], data['characters'][l]]
                all_teams.append(team)

# Finding the team with the highest score
best_team = max(all_teams, key=team_score)

# Printing the best team
print("Best team:")
for character in best_team:
    print("- " + character['key'])