triangle(1, 1).
triangle(N, NthTriangle) :-
    N > 1,
    N1 is N - 1,
    triangle(N1, PrevTriangle),
    NthTriangle is N + PrevTriangle.
