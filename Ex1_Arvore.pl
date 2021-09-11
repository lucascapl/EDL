%Fatos
pai(gustavo, lucas).
pai(gustavo, guilherme).
pai(gustavo, beatriz).
pai(chagas, gustavo).

mae(neuza, gustavo).
mae(ana, lucas).
mae(ana, guilherme).
mae(ana, beatriz).
mae(beatriz, bernardo).

feminino(neuza).
feminino(ana).
feminino(beatriz).

masculino(chagas).
masculino(gustavo).
masculino(lucas).
masculino(guilherme).
masculino(bernardo).

%Predicado
son(X,Y):-
    pai(Y,X);
    mae(Y,X).

brother(X,Y) :-
    pai(W,X),
    pai(W,Y),
    X\=Y.

uncle(X,Y) :-
    pai(W,X),
    pai(W,Z),
    mae(Z,Y),
    X\=Z;
    pai(W,X),
    pai(W,Z),
    pai(Z,Y),
    X\=Z.

grandpa(X,Y) :-
    pai(Z,Y),
    pai(X,Z);
    mae(Z,Y),
    pai(X,Z).

