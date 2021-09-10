pessoa(lucas ,data(11, dezembro, 2000)).
pessoa(matheus, data(25, janeiro, 1999)).
pessoa(guilherme,data(06, junho, 2005)).
pessoa(isabela, data(18, maio, 2001)).
pessoa(gustavo, data(04, dezembro, 1975)).
pessoa(ana, data(31, outubro, 1973)).
pessoa(jeferson, data(07, fevereiro, 2001)).
pessoa(leonardo, data(13, abril, 2007)).
pessoa(amanda, data(26, agosto, 2004)).
pessoa(cleiton, data(27, julho, 1965)).

%Buscar as pessoas com aniversario em determinado dia,mes ou ano
%Basta alterar os parametros dentro de "data"
%Neste caso esta para filtrar os aniversariantes de dezembro.
aniversario(X,Y,Z) :-
    pessoa(X, data(Y,dezembro,Z)).
