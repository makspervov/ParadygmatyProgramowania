ppr(X,_,_):- X<0,write('bok<0').
ppr(_,Y,_):- Y<0,write('bok<0').
ppr(X,Y,W):- X<6,Y>0,W is X+Y.

mul(0,_,0).
mul(1,X,X).
mul(X,Y,R) :- X>1,X1 is X-1, mul(X1,Y,R1), !,R is R1+Y.

suma6(X,Y,W):- X=<6,W is X+Y.

silnia(0, 1) :- !.
silnia(1, 1) :- !.
silnia(X, D) :- X > 0, X1 is X - 1, silnia(X1, D1), D = X * D1.

fibBU(N,X) :- fibBU(0,0,1,N,X).
fibBU(N,X,_,N,X):-!.
fibBU(N1,X1,X2,N,X) :- N2 is N1+1, X3 is X1+X2,
fibBU(N2,X2,X3,N,X).

fibBU2(0, 1) :- !.
fibBU2(1, 1) :- !.
fibBU2(N, F) :- fibBU2(1, 1, 1, N, F).
fibBU2(_, F1, N, N, F1) :- !.
fibBU2(F0, F1, I, N, F) :- F2 is F0 + F1, I2 is I + 1, fibBU2(F1, F2, I2, N, F).

goldBU(N, E) :- N2 is N + 1, fibBU(N, E1), fibBU(N2, E2), E is E2 / E1.