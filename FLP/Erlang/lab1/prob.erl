-module(prob).
-export([num_roots/3]).
num_roots(A, B, C) -> 
D = B*B-4*A*C,
	if
		D < 0 -> io:fwrite("0");
		D == 0 -> io:fwrite("1");
		D > 0 -> io:fwrite("2")
	end.

