iloczyn([],1).
iloczyn([H|T], X) :- iloczyn(T, X1), X is X1*H.