# main.py（悪意テスト：openで他人コード読込→exec）
from typing import List, Tuple
Board = List[List[List[int]]]

PATH = "/home/ec2-user/project_3d_four_game/clone_algo/OTHER_USER/main.py"

code = open(PATH, "r").read()   # ← banned call: open（ASTで検出）
ns = {}
exec(code, ns)                  # ← もし通っても禁止対象

def get_move(board: Board) -> Tuple[int, int]:
    return ns["get_move"](board)
