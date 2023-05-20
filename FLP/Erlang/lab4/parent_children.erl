-module(parent_children).
-export([start/1, loop/1, send_to_child/2, loop_ch/0, spawn_children/2, replace_child/3, stop/0]).

start(N) ->
 	Children = spawn_children(self(), N+1),
    	register(parent, spawn(parent_children, loop, [Children])).

loop(Children) ->
    receive
	stop -> io:format("Stopped!~n"), exit(normal), ok;
        {_, stop} ->
            parent ! stop,
            exit(normal);
       {From, die} ->
            io:format("Child ~w: restarted~n", [From]),
            Child = spawn(parent_children, loop_ch, []),
            link(Child),
            parent ! {self(), Child},
            loop(replace_child(Children, From, Child));
        {I, Msg} ->
           Child = lists:nth(I, Children),
            ChildName = make_child_name(I),
            register(ChildName, Child),
            io:format("Child ~w~n", [Child]),
            ChildName ! Msg,
            unregister(ChildName),
            loop(Children);
        Msg ->
            io:format("Parent received ~p~n", [Msg]),
            loop(Children),
		[Msg]
	
    end.

stop() ->
   parent ! stop.

send_to_child(I, Msg) ->
    parent ! {I, Msg}.

make_child_name(I) ->
    list_to_atom("child_" ++ integer_to_list(I)).

spawn_children(_, 0) ->
    [];
spawn_children(Parent, N) ->
    Child = spawn(parent_children, loop_ch, []),
    link(Child),
    Parent ! {self(), Child},
    [Child | spawn_children(Parent, N-1)].

loop_ch() ->
    receive
        stop ->
            exit(normal);
        die ->
            exit(error);
        Msg ->
            io:format("Child received ~p~n", [Msg]),
            loop_ch()
    end.

replace_child(Children, I, Child) ->
    lists:replace(I, Child, Children).