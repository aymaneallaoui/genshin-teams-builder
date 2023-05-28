// This program reads in a JSON file containing information about Genshin Impact characters and their stats
// It then calculates the best team compositions based on those stats, and outputs the top 5 teams

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// define struct for each character
struct character {
    char key[20]; // name of character
    int level; // level of character
    int constellation; // number of constellations unlocked
    int ascension; // current ascension level
    struct talent {
        int auto; // level of auto attack talent
        int skill; // level of skill talent
        int burst; // level of burst talent
    } talent;
};

// define function to read in JSON file
void read_json(char* filename, struct character* characters) {
    // read in file
    FILE* fp = fopen(filename, "r");
    if (fp == NULL) {
        printf("Error: could not open file\n");
        exit(1);
    }
    char buffer[100];
    fgets(buffer, 100, fp);
    fclose(fp);
    
    // parse JSON and store in character structs
    // ...
}

// define function to calculate team scores
int calculate_score(struct character* team) {
    // calculate total score for the team based on character stats
    // ...
}

// define function to output top 5 teams
void output_top_teams(struct character** teams) {
    // output the top 5 teams in order of score
    // ...
}

int main() {
    // read in JSON file and store characters in array of structs
    struct character characters[4];
    read_json("characters.json", characters);
    
    // generate all possible team compositions
    struct character* teams[5];
    // ...
    
    // calculate scores for each team
    int scores[5];
    for (int i = 0; i < 5; i++) {
        scores[i] = calculate_score(teams[i]);
    }
    
    // output top 5 teams based on score
    output_top_teams(teams);
    
    return 0;
}