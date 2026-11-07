#include "collatz_conjecture.h"

int steps(int start) {
    int count = 0;
    if (start < 1) {
        return ERROR_VALUE;
    }
    while (start > 1) {
        if (start % 2 == 0) {
            start = start / 2;
            count += 1;
        }
        else {
            start = (start * 3) + 1;
            count += 1;
        }
    }
    return count;
}