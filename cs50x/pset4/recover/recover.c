#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <cs50.h>

#define buffer_size 512

//uint8_t is the same as a byte. A type of unsigned integer of length 8 bits
typedef uint8_t BYTE;

int main(int argc, char *argv[])
{
    // check usage
    if (argc != 2)
    {
        printf("Please provide only one name of an image.");
        return 1;
    }

    // open file
    FILE *source_pointer = fopen(argv[1], "r");
    if (!source_pointer)
    {
        printf("Couldn't open file.");
        return 1;
    }

    FILE *image_pointer = NULL; // initialise image pointer
    int image_count = 0;
    char image_name[8]; // OR string image_name;
    BYTE buffer[buffer_size];

    while (fread(buffer, buffer_size, 1, source_pointer))
    {
        // fread(data, size, number, inptr) returns number of items of size "size" were read
        // determine when fread reads up to the end of a file

        if (buffer[0] == 0xff & buffer[1] == 0xd8 & buffer[2] == 0xff & (buffer[3] & 0xf0) == 0xe0)
        {
            if (image_count >= 1)
            {
                fclose(image_pointer);
            }

            // print to string
            sprintf(image_name, "%03i.jpg", image_count);

            image_pointer = fopen(image_name, "w");

            image_count++;
        }

        if (image_pointer != NULL)
        {
            fwrite(buffer, buffer_size, 1, image_pointer);
        }

    }

    fclose(source_pointer);
    fclose(image_pointer);

    return 0;

}