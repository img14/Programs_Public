import Othello_Core as core
import random
import os, signal
import time
from multiprocessing import Process, Value

class Strategy(core.OthelloCore):
	def best_strategy(self, board, player, best_move, still_running):
		best_move.value = self.ai_strategy(player, board, 3)
		for d in range(4,20):
			if still_running.value > 0:
				best_move.value = self.ai_strategy(player, board, d)

	def get_move(self, player, board):
		best_move = Value("i",0)
		running = Value("i",1)
		p = Process(target=self.best_strategy, args=(board, player,  best_move, running)) # create a sub process
		p.start()	# start it
		t1 = time.time()
		print("starting %i" % p.pid)
		p.join(5)		# give the process time to run, and rejoin (works if it's done)
		if p.is_alive():
			print("Not finished within time limit")
			time.sleep(3)		# let it run a little longer
			running.value = 0	# tell it we're about to stop
			time.sleep(0.1)		# wait a bit
			p.terminate()		# terminate
			time.sleep(0.1)		# wait a bit

		if p.is_alive(): 
			print("STILL ALIVE: Force Kill")
			os.kill(p.pid, signal.SIGKILL)	# make the OS destroy it
		t2 = time.time()
		
		move = best_move.value	# get the final best move

		print("Ended  %i" % p.pid)
		print("Elapsed time: %3.5f" % (t2 - t1))
		print("Best move (i.e. number of seconds running*100 = )", best_move.value)
		return  move
			
	def random_strategy(self, player, board):
		if self.any_legal_move(player, board):
			return random.choice(self.legal_moves(player, board))
		return None

	def human_strategy(self, player, board):
		m = int(input("Enter a move: "))
		while not self.is_legal(m, player, board):
			print("Not a legal move! Try Again")
			m = int(input("Enter a move: "))
		return m

	def ai_strategy(self, player, board, maxdepth):
		return self.alpha_beta_search(player, board, maxdepth)

	def alpha_beta_search(self, player, board, maxdepth):
		INF = float('Inf')
		if player == '@':
			return self.max_func(player, board, -INF, INF, 0, maxdepth)[1]
		else:
			return self.min_func(player, board, -INF, INF, 0, maxdepth)[1]

	def max_func(self, player, board, a, b, currentdepth, maxdepth):
		if self.finished(board) or currentdepth >= maxdepth:
			return self.evaluate(player, board), None
		else:
			maxx = -10000000000000
			move = -1
			c = self.legal_moves(player, board)
			random.shuffle(c)
			for i in c:
				newboard = self.make_move(i, player, list(board))
				next = self.next_player(newboard, player)
				if next == player:
					newval = self.max_func(next, newboard, a, b, currentdepth + 1, maxdepth)[0]
				else:
					newval = self.min_func(next, newboard, a, b, currentdepth + 1, maxdepth)[0]
				if newval > maxx:
					maxx = newval
					move = i
				if maxx >= b:
					return maxx, move
				a = max(a, maxx)
			return maxx, move

	def min_func(self, player, board, a, b, currentdepth, maxdepth):
		if self.finished(board) or currentdepth >= maxdepth:
			return self.evaluate(self.opponent(player), board), None
		else:
			minn = 10000000000000
			move = -1
			c = self.legal_moves(player, board)
			random.shuffle(c)
			for i in c:
				newboard = self.make_move(i, player, list(board))
				next = self.next_player(newboard, player)
				if next == player:
					newval = self.min_func(next, newboard, a, b, currentdepth + 1, maxdepth)[0]
				else:
					newval = self.max_func(next, newboard, a, b, currentdepth + 1, maxdepth)[0]
				if newval < minn:
					minn = newval
					move = i
				if minn <= a:
					return minn, move
				b = min(a, minn)
			return minn, move

	def is_valid(self, move):
		if move >= 11 and move <= 88 and 1 <= move%10 <= 8:
			return True
		return False

	def opponent(self, player):
		if player == core.BLACK:
			return core.WHITE
		else:
			return core.BLACK

	def find_bracket(self, square, player, board, direction):
		opp = self.opponent(player)
		m = square + direction
		if board[m] == core.EMPTY or board[m] == player:
			return None
		while self.is_valid(m) and board[m] == opp:
			m = m + direction
		if board[m] == player:
			return m
		return None

	def is_legal(self, move, player, board):
		if not self.is_valid(move):
			return False
		if not board[move] == core.EMPTY:
			return False
		for d in core.DIRECTIONS:
			if self.find_bracket(move, player, board, d) != None:
				return True
		return False

	def make_move(self, move, player, board):
		if self.is_legal(move,player,board):
			board[move] = player
			for d in core.DIRECTIONS:
				b = self.find_bracket(move, player, board, d)
				if b != None:
					self.make_flips(move, player, board, d)
		else:
			print("not a legal move")
		return board

	def make_flips(self, move, player, board, direction):
		m = move+direction
		while self.is_valid(m) and not board[m] == player:
			board[m] = player
			m = m + direction

	def legal_moves(self, player, board):
		legal_moves = []
		for i in range(11,89):
			if self.is_legal(i, player, board):
				legal_moves.append(i)
		return legal_moves

	def any_legal_move(self, player, board):
		l = self.legal_moves(player, board)
		if not l:
			return False
		return True

	def next_player(self, board, prev_player):
		opp = self.opponent(prev_player)
		if self.any_legal_move(opp, board):
			return opp
		elif self.any_legal_move(prev_player, board):
			return prev_player
		return None

	def num_pieces(self, player, board):
		num = 0
		for i in range(100):
			if board[i] == player:
				num = num + 1
		return num

	def score(self, player, board):
		return self.num_pieces(player, board) - self.num_pieces(self.opponent(player), board)

	def evaluate(self, player, board):
		SQUARE_WEIGHTS = [0,0,0,0,0,0,0,0,0,0,0,120,-20,20,5,5,20,-20,120,0,0,-20,-40,-5,-5,-5,-5,-40,-20,0,0,20,-5,15,3,3,15,-5,20,0,0,5,-5,3,3,3,3,-5,5,0,
				0,5,-5,3,3,3,3,-5,5,0,0,20,-5,15,3,3,15,-5,20,0,0,-20,-40,-5,-5,-5,-5,-40,-20,0,0,120,-20,20,5,5,20,-20,120,0,0,0,0,0,0,0,0,0,0,0]
		MAX = 0
		for i in range(100):
			MAX = MAX + SQUARE_WEIGHTS[i]
		MAX = MAX + 1
		MIN = -MAX
		if self.finished(board):
			if self.winner(board) == core.BLACK:
				return MAX
			else:
				return MIN
		scoring_matrix = [0]*100
		for i in range(100):
			if board[i] == player:
				scoring_matrix[i] = 1
			elif board[i] == self.opponent(player):
				scoring_matrix[i] = -1
		score = 0
		for i in range(100):
			score = score + scoring_matrix[i]*SQUARE_WEIGHTS[i]
		return score

	def finished(self, board):
		if not self.any_legal_move(core.BLACK, board) and not self.any_legal_move(core.WHITE, board):
			return True
		else:
			return False

	def winner(self, board):
		if self.score(core.BLACK, board) > 0:
			return core.BLACK
		else:
			return core.WHITE