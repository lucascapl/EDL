fatorial(0,1).
fatorial(N,W):-
    N > 0,
    SEQ is N - 1,
    fatorial(SEQ, R),
    W is N*R.
