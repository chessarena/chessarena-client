import chess

def make_move(board, match_id, user_id):
   legal_moves = board.legal_moves  
   move = legal_moves[0]
   return move
