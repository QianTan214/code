#include "helpers.h"


//check50 cs50/problems/2020/x/filter/less

#include <stdio.h>
#include <math.h>
#include <string.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {

            float temp1 = image[i][j].rgbtBlue;
            float temp2 = image[i][j].rgbtGreen;
            float temp3 = image[i][j].rgbtRed;
            float temp = (temp1 + temp2 + temp3) / 3;
            temp = (int) round(temp);
            image[i][j].rgbtBlue = temp;
            image[i][j].rgbtGreen = temp;
            image[i][j].rgbtRed = temp;

        }

    }


    return;
}



// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width; j++)
        {
            int temp1 = image[i][j].rgbtBlue;
            int temp2 = image[i][j].rgbtGreen;
            int temp3 = image[i][j].rgbtRed;
            double tempBlue = (0.131 * temp1 + 0.534 * temp2 + 0.272 * temp3);
            double tempGreen = (0.168 * temp1 + 0.686 * temp2 + 0.349 * temp3);
            double tempRed = (0.189 * temp1 + 0.769 * temp2 + 0.393 * temp3);

            if (tempBlue > 255)
            {
                tempBlue = 255;
            }

            if (tempGreen > 255)
            {
                tempGreen = 255;
            }

            if (tempRed > 255)
            {
                tempRed = 255;
            }

            image[i][j].rgbtBlue = (int) round(tempBlue);
            image[i][j].rgbtGreen = (int) round(tempGreen);
            image[i][j].rgbtRed = (int) round(tempRed);



        }
    }


    return;
}



// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
    {
//if width is even number
        if (width % 2 == 0)
        {
            for (int j = 0; j < (width / 2); j++)
            {
                int temp1 = image[i][j].rgbtBlue;
                int temp2 = image[i][j].rgbtGreen;
                int temp3 = image[i][j].rgbtRed;
                image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
                image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
                image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
                image[i][width - 1 - j].rgbtBlue = temp1;
                image[i][width - 1 - j].rgbtGreen = temp2;
                image[i][width - 1 - j].rgbtRed = temp3;
            }
        }

//if width is odd number
        if (width % 2 == 1)
        {
            for (int j = 0; j < ((width + 1) / 2); j++)
            {
                int temp1 = image[i][j].rgbtBlue;
                int temp2 = image[i][j].rgbtGreen;
                int temp3 = image[i][j].rgbtRed;
                image[i][j].rgbtBlue = image[i][width - j - 1].rgbtBlue;
                image[i][j].rgbtGreen = image[i][width - j - 1].rgbtGreen;
                image[i][j].rgbtRed = image[i][width - j - 1].rgbtRed;
                image[i][width - 1 - j].rgbtBlue = temp1;
                image[i][width - 1 - j].rgbtGreen = temp2;
                image[i][width - 1 - j].rgbtRed = temp3;
            }
        }

    }

    return;
}



// Blur image
// Use 4 loops to solve this question

void blur(int height, int width, RGBTRIPLE image[height][width])
{

//declare RGB variables.
//variable counter represents the number of iterations.

    int blue_sum;
    int green_sum;
    int red_sum;
    float counter;

//create a RGBTRIPLE data structure variable called temp
    RGBTRIPLE temp[height][width];

//loop through rows and columns of the image
    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width; j++)
        {
            //these variables have to be initialised inside the for loop, otherwise their values would not change.
            blue_sum = 0;
            green_sum = 0;
            red_sum = 0;
            counter = 0.0;

            //m is the rows around the current row. n is the columns around the current column
            for (int m = -1; m < 2; m++)
            {
                for (int n = -1; n < 2; n++)
                {
                    //ensure scanning does not go out of image bounds
                    if ((i + m) != -1 && (i + m) != height && (j + n) != -1 && (j + n) != width)

                    {

                        blue_sum = blue_sum + image[i + m][j + n].rgbtBlue;
                        green_sum = green_sum + image[i + m][j + n].rgbtGreen;
                        red_sum = red_sum + image[i + m][j + n].rgbtRed;

                        counter++;
                    }


                }

            }

            temp[i][j].rgbtBlue = (int) round(blue_sum / counter);
            temp[i][j].rgbtGreen = (int) round(green_sum / counter);
            temp[i][j].rgbtRed = (int) round(red_sum / counter);


        }


    }

    for (int i = 0; i < height; i++)
    {

        for (int j = 0; j < width; j++)
        {
            image[i][j].rgbtBlue = temp[i][j].rgbtBlue;
            image[i][j].rgbtGreen = temp[i][j].rgbtGreen;
            image[i][j].rgbtRed = temp[i][j].rgbtRed;
        }

    }

    return;


}
