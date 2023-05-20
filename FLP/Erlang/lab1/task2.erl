-module(task2).
-import(lists, [reverse/1]).
-export([init/1]).
init(List) ->
	RevList = reverse(List),
	[A|B]=RevList,
	Result = reverse(B),
	io:fwrite("~p~n",[Result]).