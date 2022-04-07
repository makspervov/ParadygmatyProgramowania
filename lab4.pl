czyLista([]).
czyLista([_|T]) :- write(T), czyLista(T).

ostatni([X],X).
ostatni([H|T],X) :- ostatni(T,X).

isMember(X,[Y|_]) :- X=Y.
isMember(X,[_|Y]) :- isMember(X,Y).

ile([], 0).
ile([H|T], N) :- ile(T, X), N is X+1.

suma([],0).
suma([H|T], X) :- suma(T, X1), X is X1+H.

suma2([],A,A).
suma2([H|T],A,X) :- suma2(T,A,X1), X is X1+H.