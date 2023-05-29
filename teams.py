import json


with open('characters.json') as f:
    data = json.load(f)

characters = data['characters']


teams = []


def calculate_team_score(team):
    score = 0
    for character in team:
        score += character['talent']['auto'] + character['talent']['skill'] + character['talent']['burst']
    return score
# TODO ugrade the algorithm

for i in range(len(characters)):
    for j in range(i+1, len(characters)):
        for k in range(j+1, len(characters)):
            for l in range(k+1, len(characters)):
                team = [characters[i], characters[j], characters[k], characters[l]]

                if 'RaidenShogun' in [c['key'] for c in team] and 'Eula' in [c['key'] for c in team]:
                    teams.append(team)


teams.sort(key=calculate_team_score, reverse=True)


for i, team in enumerate(teams[:5]):
    print(f'Team {i+1}:')
    for character in team:
        print(f'{character["key"]}, level {character["level"]}, constellation {character["constellation"]}, ascension {character["ascension"]}, talent: auto {character["talent"]["auto"]}, skill {character["talent"]["skill"]}, burst {character["talent"]["burst"]}')
    print(f'Total score: {calculate_team_score(team)}\n')