gray(List, Code):-
    length(List, N),
    gray_f(N, Code).

gray_f(0, [[]]).

gray_f(N, Code) :-
  N > 0,
  N1 is N - 1,
  gray_f(N1, Code1),
  reverse(Code1, RevCode1),
  add_zeros(Code1, Code0),
  add_ones(RevCode1, Code1Rev),
  append(Code0, Code1Rev, Code).

add_zeros([], []).
add_zeros([H|T], [[0|H]|TRes]) :-
  add_zeros(T, TRes).

add_ones([], []).
add_ones([H|T], [[1|H]|TRes]) :-
  add_ones(T, TRes).

:- begin_tests(gray).
test(zero_bit) :-
    gray([], Code),
    Code = [[]].
test(one_bit) :-
    gray([0], Code),
    Code = [[0], [1]].
test(three_bit) :-
    gray([0,0,0], Code),
    Code = [[0, 0, 0], [0, 0, 1], [0, 1, 1], [0, 1, 0], [1, 1, 0], [1, 1, 1], [1, 0, 1], [1, 0, 0]].
 :- end_tests(gray).    