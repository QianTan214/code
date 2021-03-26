#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>

int count_letters(string s);
int count_words(string s);
int count_sentences(string s);

int main(void)
{

    string text = get_string("Text: ");

    float index;
    float L, S;
    int number_of_letters = count_letters(text);
    int number_of_words = count_words(text);
    int number_of_sentences = count_sentences(text);

    //be careful integer divided by integer you get an integer with digits after decimal place truncated

    L = (float) 100 * number_of_letters / number_of_words;
    S = (float) 100 * number_of_sentences / number_of_words;
    index = 0.0588 * L - 0.296 * S - 15.8;

    // printf("%i letter(s)\n", count_letters(text));
    // printf("%i word(s)\n", count_words(text));
    // printf("%i sentence(s)\n", count_sentences(text));


    if (index >= 16)
    {
        printf("Grade 16+\n");
    }

    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }

    else
    {

        printf("Grade %i\n", (int) round(index));
    }


}


// below is the function to count how many letters in a sentence

int count_letters(string s)
{
    int letter=0;

    for (int i = 0, n = strlen(s); i < n;  i++)

    {

        if ((s[i] >= 'a' && s[i] <= 'z') || (s[i] >= 'A' && s[i] <= 'Z'))

        {
            letter=letter+1;
        }
    }

    return letter;

}


// below is the function to count how many words in a sentence
// assume a sentence will not start or end with a space

int count_words(string s)
{
    int space = 0;

    for (int i = 0, n = strlen(s); i < n;  i++)

    {
        if (s[i] == ' ')

            {
                space = space + 1;
            }
    }

    int word = space + 1;

    return word;

}


// below is the function to count how many sentences in a text
// assume any sequence of characters that ends with a . or a ! or a ? to be a sentence

int count_sentences(string s)
{
    int period = 0;

    for (int i = 0, n = strlen(s); i < n;  i++)

    {
        if (s[i] == '.' || s[i] == '!' || s[i] == '?')

            {
                period = period + 1;
            }
    }

    int sentence = period;

    return sentence;

}






