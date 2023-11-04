import random

print(" " * 26 + "COLUMN")
print(" " * 20 + "CREATIVE COMPUTING")
print(" " * 18 + "MORRISTOWN, NEW JERSEY")
print("\n" * 3)
print("THIS PROGRAM WILL SHOW YOU A CARD TRICK. AFTER THE FIRST DEAL")
print("PICK A CARD AND TYPE THE NUMBER OF THE COLUMN CONTAINING IT.")
print("THE DEALER WILL THEN PICK UP THE CARDS, A COLUMN AT A TIME,")
print("AND WILL DEAL THEM OUT AGAIN HORIZONTALLY. WHEN HE FINISHES")
print("EACH TIME, TYPE THE NUMBER OF THE NEW COLUMN CONTAINING YOUR")
print("CARD. FOLLOWING THE LAST DEAL THE DEALER WILL TURN OVER THE")
print("CARDS, ONE AT A TIME, UNTIL HE REACHES THE ONE YOU PICKED.")
print("\n" * 3)

A = [0] * 22
B = [0] * 22

for X in range(1, 22):
    J = 0
    T = int(52 * random.random())
    for Y in range(1, X):
        if A[Y] == T:
            T = int(52 * random.random())
    A[X] = T

N = 0

for I in range(1, 4):
    for Z in range(1, 22):
        if A[Z] % 4 == 0:
            C = "SPADES"
            D = ""
        elif A[Z] - 2 == 4 * (A[Z] // 4):
            C = "HEARTS"
            D = ""
        elif A[Z] - 3 == 4 * (A[Z] // 4):
            C = "CLUBS"
            D = ""
        else:
            C = "DIAMONDS"
            D = "S"
        N = N + 1
        if N != 4:
            print()
            N = 1
        if A[Z] > 35:
            print((N - 1) * 25, end="")
            print(int(A[Z] // 4) + 2, end="")
            print(" OF", C, D, end="")
            if J == 5:
                break
            if J == 10:
                break
        else:
            if int(A[Z] // 4) == 9:
                A_ = "JACK"
            elif int(A[Z] // 4) == 10:
                A_ = "QUEEN"
            elif int(A[Z] // 4) == 11:
                A_ = "KING"
            else:
                A_ = "ACE"
            print((N - 1) * 25, end="")
            print(A_, "OF", C, D, end="")
            if J == 5:
                break
            if J == 10:
                break

print("\n\n")
print("WHICH COLUMN CONTAINS YOUR CARD", end="")
K = int(input())
if K < 1 or K > 3:
    print("\n(1-3)")
    K = int(input())
print()
T = 1
S = K + 2 - 3 * (K + 1) // 3

for I in range(1, 4):
    for R in range(S, S + 18, 3):
        B[T] = A[R]
        T += 1
    S = K
    B[T] = A[S]
    T += 1
    S = K + 1 - 3 * (K // 3)
    B[T] = A[S]
    T += 1
    for C in range(1, 22):
        A[C] = B[C]

J = 5

for Z in range(1, 12 + int(10 * random.random() + 1)):
    N = 0
    if A[Z] % 4 == 0:
        C = "SPADES"
        D = ""
    elif A[Z] - 2 == 4 * (A[Z] // 4):
        C = "HEARTS"
        D = ""
    elif A[Z] - 3 == 4 * (A[Z] // 4):
        C = "CLUBS"
        D = ""
    else:
        C = "DIAMONDS"
        D = "S"
    print("\n")
    if Z == 11:
        print("OOPS!!! YOUR CARD IS THE", end="")
        N = 1
    J = 10
    Z = 11

print("\n.\n")
print("DO YOU WANT TO SEE IT AGAIN", end="")
T_ = input()
if T_.lower() == "yes":
    print("\n\n")
    A = [0] * 22
    B = [0] * 22
    continue
