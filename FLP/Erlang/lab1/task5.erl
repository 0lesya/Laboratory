-module(task5).
-export([sliding_average/2, slide/6]).

sliding_average(List, WindowSize) ->
	slide(List, WindowSize, 0, 0, List, []).
	
slide([A|B], N, Count, Sum, AllList, Acc) ->
	case Count < N of
		true-> 
			slide(B, N, Count+1, Sum+A, AllList, Acc);
		false->
			[_|Tail] = AllList, 
			Ans = Sum/N,
			Answer = [Ans|Acc],
			slide(Tail, N, 0, 0, Tail, Answer)
		end; 

slide([], N, _, Sum, _, Acc) -> Ans = Sum/N,  Answer= [Ans|Acc], lists:reverse(Answer).
