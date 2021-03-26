#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>
//include <stdlib.h> to use function atoi
//include <ctype.h> to use function isdigit

// declare function called encryption

string encryption(string n, int k);

// declare function called check_alnum to check if a string only consists of decimal digits 0 - 9

bool check_alnum(string argv_check);


int main(int argc, string argv[])
{



    if (argc != 2)
    {
        printf("command-line argument doesn't meet requirements\n");
        return 1;
    }


    if ((check_alnum(argv[1])) == false)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }


    int c = atoi(argv[1]);


    //atoi function converts a string that looks like a number into that number.

    if (c <= 0)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }


    //prompt user to enter plaintext
    string plain_text = get_string("plaintext:");

    //call function encryption
    string cipher_text = encryption(plain_text, c);

    printf("ciphertext:%s\n", cipher_text);

    return 0;


}


//define function called encryption to encrypt text

string encryption(string n, int k)
{

    for (int i = 0; i < strlen(n); i++)

    {
        if (n[i] >= 'A' && n[i] <= 'Z')

        {
            n[i] = (n[i] - 65 + k) % 26 + 65;

            //printf("%c", n[i]);
        }


        if (n[i] >= 'a' && n[i] <= 'z')

        {
            n[i] = (n[i] - 97 + k) % 26 + 97;

            //printf("%c", n[i]);
        }


        else
        {
            //printf("%c", n[i]);
        }

    }


    return n;


}

// define function called check_alnum, it returns bool value

bool check_alnum(string argv_check)

{
    for (int l = 0; l < strlen(argv_check); l++)
    {
        if (isdigit((int) argv_check[l]) == false)
        {
            return false;
        }

    }
    return true;

}