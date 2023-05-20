woman(olya).
woman(katya).
woman(liza).
woman(nastya).

man(petr).
man(pavel).
man(ivan).
man(alexey).
man(sergey).

parent_child(alexey, nastya).
parent_child(alexey, pavel).
parent_child(alexey, olya).
parent_child(liza, nastya).
parent_child(liza, pavel).
parent_child(liza, olya).
parent_child(petr, sergey).
parent_child(nastya, sergey).
parent_child(olya, ivan).
parent_child(olya, katya).

father(Parent, Child) :-
	parent_child(Parent, Child),
	man(Parent).

mother(Parent, Child) :-
	parent_child(Parent, Child),
	woman(Parent).

married(alexey, liza).
married(petr, nastya).

wife_children(Man) :-
	father(Man, X),
	married(Man, W),
	mother(W, X).

brothers(Bro1, Bro2) :-
	parent_child(Parent, Bro1),
	parent_child(Parent, Bro2),
	man(Bro1),
	man(Bro2),
	Bro1 \= Bro2.

pred_potom(Pred, Potom) :-
	parent_child(Pred, Potom).
pred_potom(Pred, Potom) :-
	parent_child(Pred, Pred1),
	pred_potom(Pred1, Potom).

siblings(X, Y) :-
	man(X),
	man(Y),
	X \= Y,
	parent_child(Parent1, X),
	parent_child(Parent2, Y),
	Parent1 \= Parent2,
	parent_child(OldParent1, Parent1),
	parent_child(OldParent2, Parent2),
	OldParent1 = OldParent2.