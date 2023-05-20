my_flatten([], []).

my_flatten([H|T], Flat) :-
    is_list(H),
    !,
    my_flatten(H, HFlat),
    my_flatten(T, TFlat),
    append(HFlat, TFlat, Flat).

my_flatten([H|T], [H|TFlat]) :-
    \+ is_list(H),
    my_flatten(T, TFlat).

:- begin_tests(my_flatten).

test(empty_list):-
my_flatten([], Flat),
Flat=[].

test(no_nested_lists) :-
    my_flatten([1,2,3], Flat),
    Flat = [1,2,3].

test(one_level_nested_list) :-
    my_flatten([1,[2], [3,4]], Flat),
    Flat = [1,2,3,4].

test(multiple_level_nested_list) :-
    my_flatten([1,[2,[3,[4]]],5], Flat),
    Flat = [1,2,3,4,5].

:- end_tests(my_flatten).