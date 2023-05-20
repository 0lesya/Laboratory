-module(task5_2).
-export([sliding_average/2, slide/5]).

sliding_average(List, WindowSize) ->
	slide(List, WindowSize,0, [], []).

slide([A|B], N, Count, Acc, Part) ->
	case Count <N of
		true-> 
			Part2 = [A|Part],
			slide(B, N, Count+1, Acc, Part2);
		false ->
			Part2 = lists:reverse(Part),
			Acc2=[Part2|Acc],
			slide(B, N, 1, Acc2,[A])
		end;
slide([], _,_, Acc,Part) ->
	Part2= lists:reverse(Part),
	Acc2 = [Part2|Acc],
	Result = lists:reverse(Acc2),
	Result. 