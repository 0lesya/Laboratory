-module(task3).
-export([tailF/2, f/2, split/2]).
f([], _) -> [];
f([A|B], N) -> 
	if 
		N>0 -> [A|f(B, N-1)];
	true -> f([],0)
	end.

tailF([_|B], N) -> if N>1 -> tailF(B, N-1);
	true -> B
	end.

split(List, N) -> 
	Head=f(List, N),
	Tail = tailF(List, N),
	Answer={Head, Tail},
	Answer.
