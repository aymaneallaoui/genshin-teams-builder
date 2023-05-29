
import json


with open('characters.json') as file:
    data = json.load(file)


def total_talent_level(character):
    return character['talent']['auto'] + character['talent']['skill'] + character['talent']['burst']


def team_score(team):
    score = 0
    for character in team:
        score += total_talent_level(character)
    return score


all_teams = []
for i in range(len(data['characters'])):
    for j in range(i+1, len(data['characters'])):
        for k in range(j+1, len(data['characters'])):
            for l in range(k+1, len(data['characters'])):
                team = [data['characters'][i], data['characters'][j], data['characters'][k], data['characters'][l]]
                all_teams.append(team)


best_team = max(all_teams, key=team_score)


print("Best team:")
for character in best_team:
    print("- " + character['key'])