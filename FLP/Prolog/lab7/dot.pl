dot(List1, List2, DotProduct) :-
    dot_func(List1, List2, DotProduct).

dot_func([], [], 0).
do_func([X|XT], [Y|YT], DotProduct) :-
    dot_func(XT, YT, RestDotProduct),
    DotProduct is X * Y + RestDotProduct.
