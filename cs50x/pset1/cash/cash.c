#include <stdio.h>
#include <string.h>
#include <math.h>
#include <cs50.h>


int main(void)
{
    float dollars; // can define in do(), has to be defined before for while loop

    do
    {
        dollars = get_float("Change owed:\n");
    }
    while (dollars <= 0);

    int cents = round(dollars * 100);

//C/C++整数除法会舍去小数部，例如 int a=15/10; a的结果为1
    int n = 0;

    if (cents >= 25)
    {
        n = n + cents / 25;
        cents = cents - (cents / 25) * 25;
    }

    if (cents >= 10 && cents < 25)
    {
        n = n + cents / 10;
        cents = cents - (cents / 10) * 10;

    }

    if (cents >= 5 && cents < 10)
    {
        n = n + cents / 5;
        cents = cents - (cents / 5) * 5;

    }

    if (cents < 5)
    {
        n = n + cents / 1;

    }

    printf("%i\n", n);

}










