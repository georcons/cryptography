/*
Задача 6.
Линеен регистър с период 21.

*/

#include <stdio.h>

typedef struct {
    int one;
    int two;
    int three;
    int four;
    int five;
} Binary;

typedef struct {
    Binary first;
    Binary second;
    Binary third;
    Binary fourth;
    Binary fifth;
} BinaryState;

void print_binary(Binary bin) {
    printf("%d%d%d%d%d ", bin.one, bin.two, bin.three, bin.four, bin.five);
}

void print_state(BinaryState state) {
    print_binary(state.first);
    print_binary(state.second);
    print_binary(state.third);
    print_binary(state.fourth);
    print_binary(state.fifth);
}

BinaryState registry(BinaryState state) {
    BinaryState output;
    output.first = state.fifth;
    output.second = state.first;
    output.third = state.second;
    output.fourth = state.third;
    Binary sum;
    sum.one = state.fourth.one ^ state.fifth.one;
    sum.two = state.fourth.two ^ state.fifth.two;
    sum.three = state.fourth.three ^ state.fifth.three;
    sum.four = state.fourth.four ^ state.fifth.four;
    sum.five = state.fourth.five ^ state.fifth.five;
    output.fifth = sum;
    return output;
}

int main() { 
    Binary A = {1, 0, 0, 0, 0};
    Binary B = {0, 1, 0, 0, 0};
    Binary C = {0, 0, 1, 0, 0};
    Binary D = {0, 0, 0, 1, 0};
    Binary E = {0, 0, 0, 0, 1};
    BinaryState state = {A, B, C, D, E};
    
    for (int i = 0; i <= 21; ++i) {
        printf("%d. ", i);
        print_state(state);
        printf("\n");

        state = registry(state);
    }
    
    return 0;
}