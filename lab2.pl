lubi(jan, tatry).
lubi(jan, beskidy).
lubi(jerzy, beskidy).
lubi(jerzy, bieszczady).
lubi(jozef, bieszczady).
lubi(karol, beskidy).
lubi(justyna, swietokrzyskie).
bratniadusza(X, Y) :- lubi(X, S), lubi(Y, S),X \= Y.

czas(t1, 120).
czas(t2, 90).
czas(t3, 135).
dystans(t1, 9600).
dystans(t2, 8100).
dystans(t3, 13500).
predkosc(X, Ac) :- czas(X, C),dystans(X, D), Ac is D/C.