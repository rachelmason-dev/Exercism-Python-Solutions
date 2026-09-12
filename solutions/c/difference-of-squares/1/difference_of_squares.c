#include "difference_of_squares.h"

unsigned int sum_of_squares(unsigned int number)
{
    unsigned int square;
    unsigned int sum = 0;
    for (unsigned int i = 1; i <= number; i++)
    {
        square = i * i;
        sum += square;
    }
    return sum;
}

unsigned int square_of_sum(unsigned int number)
{
    unsigned int sum = 0;
    for (unsigned int i = 1; i <= number; i++)
    {
        sum += i;
    }
    return sum * sum;
}

unsigned int difference_of_squares(unsigned int number)
{
    unsigned int result = square_of_sum(number) - sum_of_squares(number);
    return result;
}