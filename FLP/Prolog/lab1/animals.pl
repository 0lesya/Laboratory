herbivore(rabbit).
herbivore(horse).
herbivore(cow).

predator(fox).
predator(wolf).


all(hedgehog).
all(raccoon).
all(bear).

bigger(bear, cow).
bigger(cow, horse).
bigger(horse, wolf).
bigger(wolf, fox).
bigger(fox, raccoon).
bigger(raccoon, rabbit).
bigger(rabbit, hedgehog).

bigger_than(X, Y) :- bigger(X, Y).
bigger_than(X, Y) :- 
	bigger(X, Z),
	bigger_than(Z, Y).

eat(X, Y) :-
	(predator(X); all(X)),
	bigger_than(X, Y).
