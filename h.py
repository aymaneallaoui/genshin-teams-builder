import json


with open('characters.json') as f:
    data = json.load(f)


characters = {}
for c in data['characters']:
    characters[c['key']] = c


def character_strength(c):
    return (c['talent']['auto'] + c['talent']['skill'] + c['talent']['burst']) * (c['level'] / 100)


def build_teams(characters):

    character_strengths = {}
    for k, v in characters.items():
        character_strengths[k] = character_strength(v)


    sorted_characters = sorted(character_strengths.items(), key=lambda x: x[1], reverse=True)


    teams = []
    for i in range(5):
        team = [sorted_characters[i][0]]
        top_tags = list(characters[sorted_characters[i][0]].get('tags', []))[:3]
        for j in range(4):

            potential_characters = [c for k, c in characters.items() if k not in team and any(tag in c.get('tags', []) for tag in top_tags)]

            potential_characters = sorted(potential_characters, key=lambda c: character_strength(c), reverse=True)

            if potential_characters:
                team.append(potential_characters[0]['key'])
            else:
                break
        teams.append(team)


    return teams


teams = build_teams(characters)

for i, team in enumerate(teams):
    print(f"Team {i+1}: {', '.join(team)}")
