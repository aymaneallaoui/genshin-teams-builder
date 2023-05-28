
import json


with open('characters.json') as f:
    data = json.load(f)


def calculate_power(team):
    total_power = 0
    for character in team:
        power = character['level'] + character['constellation'] + character['ascension'] + sum(character['talent'].values())
        total_power += power
    return total_power


best_teams = []
best_power = 0

for i in range(len(data['characters'])):
    for j in range(i+1, len(data['characters'])):
        for k in range(j+1, len(data['characters'])):
            for l in range(k+1, len(data['characters'])):

                current_team = [data['characters'][i], data['characters'][j], data['characters'][k], data['characters'][l]]
                current_power = calculate_power(current_team)

                if current_power > best_power:
                    best_teams = [current_team]
                    best_power = current_power
                elif current_power == best_power:
                    best_teams.append(current_team)

print("The top 5 best teams are:")
for i, team in enumerate(best_teams[:5]):
    print(f"{i+1}. Team power: {calculate_power(team)}")
    for character in team:
        print(f"\t- {character['key']}")