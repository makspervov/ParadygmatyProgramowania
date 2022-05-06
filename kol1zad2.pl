lubi(kinga, gory).
lubi(kinga, morze).
lubi(piotr, morze).
lubi(piotr, jezioro).
lubi(mieczyslaw, las).
lubi(halina, las).
lubi(pawel, morze).
bratniadusza(X, Y) :- lubi(X, S), lubi(Y, S),X \= Y.