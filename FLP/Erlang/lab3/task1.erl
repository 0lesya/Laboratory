-module(task1).
-export([empty/0, node/3, data/1, left/1, right/1, count_leaves/2]).

%% Тип tree
-type tree() :: empty | {node, any(), tree(), tree()}.

%%% Конструкторы

-spec empty() -> tree(). %% возвращает пустое дерево
empty() -> empty.

-spec node(Data::any(), Left::tree(), Right::tree()) -> tree(). %% возвращает непустое дерево с данными Data, левым наследником Left и правым наследником Right
node(Data, Left, Right) -> {node, Data, Left, Right}.

-spec data(tree()) -> any(). %% возвращает данные, если они есть (т.е. дерево непусто), выкидывает ошибку, если дерево пусто
data({node, Data, _, _}) -> Data.

-spec left(tree()) -> tree(). %% возвращает левое поддерево, выкидывает ошибку, если дерево пусто
left({node, _, Left, _}) -> Left.

-spec right(tree()) -> tree(). %% возвращает правое поддерево, выкидывает ошибку, если дерево пусто
right({node, _, _, Right}) -> Right.

count_leaves({node, _, Left, Right}, count) ->
	if
		Right==false -> count = count+1;
		Left == false -> count = count+1;
	true -> count_leaves(Left, count)
	end;

count_leaves({node, _, Left, Right}, 0) ->
	if
		Right==false -> count = 1;
		Left == false -> count = 1;
	true -> count_leaves(Left, count)
	end.