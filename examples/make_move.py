import chess

def make_move(board_fen, match_id, user_color):
    board = chess.Board(board_fen)
    legal_moves = list(board.legal_moves)
    move = legal_moves[0]
    return move.uci()