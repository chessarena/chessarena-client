import argparse
from arenachess.engine_runner import start_engine, stop_engine

def main():
    parser = argparse.ArgumentParser(description="ArenaChess CLI")
    parser.add_argument("user_token", type=str, help="User token for authentication")
    parser.add_argument("command", type=str, choices=["start", "stop"], help="Command to execute")
    parser.add_argument("path_to_make_move", type=str, nargs="?", help="Path to make_move.py")

    args = parser.parse_args()

    if args.command == "start":
        start_engine(args.user_token, args.path_to_make_move)
    elif args.command == "stop":
        stop_engine(args.user_token)
