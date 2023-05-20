contains_duplicates(List) :-
    containsDuplicates(List).

containsDuplicates([H|T]) :-
    member(H, T),
    !.
containsDuplicates([_|T]) :-
    containsDuplicates(T).

member(H, [H|_]) :- !.
member(X, [_|T]) :- member(X,T).

:- begin_tests(contains_duplicates).

test(empty_list, fail) :-
    contains_duplicates([]).

test(no_duplicates, fail) :-
    contains_duplicates([a,b,c]).

test(with_duplicates, true) :-
    contains_duplicates([a,b,a,b,c,c,a]).

:- end_tests(contains_duplicates).