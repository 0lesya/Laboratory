zip([], [], []).
zip([H1|T1], [H2|T2], [[H1,H2]|T]) :-
	zip(T1, T2, T).

:- begin_tests(zip).
test(zip_empty_lists):-
	zip([], [], ZippedList),
	ZippedList=[].

test(zip_same_length_lists) :-
	zip([a, b, c], [1, 2, 3], ZippedList),
	ZippedList = [[a,1], [b,2], [c,3]].

test(zip_different_length_lists) :-
	\+ zip([1,2,3], [a,b], _).

:- end_tests(zip).