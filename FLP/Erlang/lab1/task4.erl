-module(task4).
-import(lists, [reverse/1]).
-export([degree/2, convert/2, binary_to_int/1]).

degree(_,0) -> 1;
degree(Num, 1) -> Num;
degree(Num, N) -> Num * degree(Num, N-1).

convert([],_) -> 0;
convert([A|B], N) -> 
	if 
	A==1 ->
	convert(B, N+1) + degree(2, N);
	A==49 ->
	convert(B, N+1) + degree(2, N);
	true ->
	convert(B, N+1)
	end.

binary_to_int(Bin) ->
	X = reverse(Bin),
	Y = convert(X, 0),
	Y.