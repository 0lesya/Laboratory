delete_all([], _, []).

delete_all([H|T], A, Acc) :-
    H==A,
    !,
    delete_all(T, A, Acc).

delete_all([H|T], A, [H|Acc]) :-
    delete_all(T, A, Acc).