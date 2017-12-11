from strategy import Strategy

o = Strategy()

bwins = 0
wwins = 0

i = 0
while i < 10:
	board = o.initial_board()
	player = '@'
	while not o.finished(board):
		INF = float('Inf')
		if player == 'o':
			m = o.ai_strategy(player, board, 4)
		else:
			m = o.random_strategy(player, board)
		o.make_move(m, player, board)
		print(o.print_board(board))
		player = o.next_player(board, player)
	if o.winner(board) == "@":
		bwins = bwins + 1
	elif o.winner(board) == 'o':
		wwins = wwins + 1
	i = i + 1

print("Black wins: %s White wins: %s"%(bwins, wwins))