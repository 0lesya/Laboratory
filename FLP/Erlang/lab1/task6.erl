-module(task6).
-export([for/3, intersect/2]).

intersect(List1, List2) ->
    for(List1, List2, []).


for([A|B], List2, Ans) -> 
	Temp=List2--[A],
    if length(List2) > length(Temp) ->
        Answer=[A|Ans],
	for(B, Temp, Answer);
    true -> for(B, List2, Ans)
    end;

for([],_,Ans) -> lists:reverse(Ans).

