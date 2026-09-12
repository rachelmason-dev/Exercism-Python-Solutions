#include "grains.h"

uint64_t double_num(uint64_t number);
    
uint64_t square(uint8_t index)
{
    if (index == 0)
    {
        return 0;
    }
    else if (index == 1)
    {
        return 1;
    }
    uint64_t amount = 1;
    for (uint64_t i = 2; i <= index; i++)
    {
        amount = double_num(amount);
    }
    return amount;
}

uint64_t total(void)
{
    uint64_t sum = 0;
    for (uint64_t i = 0; i <= 64; i++)
    {
        sum+= square(i);  
    }
    return sum;
}

uint64_t double_num(uint64_t number)
{
    return number * 2;
}