#include <cs50.h>
#include<stdio.h>
#include<string.h>

#define MAX 9

typedef struct{
    string name;
    int votes;
}candidate;

candidate candidates[MAX]

int candidate_count;

// functino prototyes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    if (argc<2)
    {
        printf("Usage:plurality [candidate ...]\n");
        return 1;
    }

    candidate_count = argc - 1;
    if(candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i=0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i+1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    //loop over all voters
    for (i=0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");
        if (!vote(name))
        {
            printf("invalid vote.\n")
        }
    }

    print_winner();
}

bool vote(string name)
{
    for(int i=0; i < candidate_count; i++)
    {
        if (strcmp(name, candidates[i].name)==0)
        {
            candidates[i].vote++;
            return true;
        }
    }
    return false;
}


void print_winner(void)
{
    int maxvote = 0;

    for (i=0; i<candidate_count; i++)
    {
        if(maxvote < candidates[i].votes)
        {
            maxvote = candidates[i].votes;
        }
    }

    for (i=0; i<candidate_count; i++)
    {
        if(candidates[i].votes == maxvote)
        {
            printf("winner is %s\n", candidates[i].name);
        }
    }
}