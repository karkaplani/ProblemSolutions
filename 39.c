#include <stdio.h>
#include <math.h>

int countSolution(int perimeter) {
    int counter = 0;
    for(int a = 1; a <= perimeter; a++) {
        for(int b =1; b <= perimeter; b++) {
            if(sqrt(a*a+b*b) == perimeter-(a+b)) {
                counter++;
            }
        }
    }
    return counter/2;
}

int main()
{
    int result = 0;
    int maxCount = 0;
    
    for(int p = 1; p <= 1000; p++) {
        if(countSolution(p) >= maxCount) {
            maxCount = countSolution(p);
            result = p;
        }
    }
    printf("Result is %d",result);
}