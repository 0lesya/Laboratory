-module(counter).
-export([start/0, incr/0, stop/0, loop/1]).

start() ->
    	register(counter, spawn(counter, loop, [0])),
	whereis(counter).

incr() ->
    counter ! increment.

stop() ->
    counter ! stop.

loop(Counter) ->
    receive
        increment ->
            NewCounter = Counter + 1,
            io:format("Incremented counter value ~w~n", [NewCounter]),
            loop(NewCounter);
        stop ->
            	io:format("Final counter value: ~w~n", [Counter]),
		io:format("Stopped!~n"),
            	ok
    end.
