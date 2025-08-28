# === main.py（テンプレ準拠・悪意テストC）===
from abc import ABC, abstractmethod
from typing import Tuple, List, Dict, Any
Board = List[List[List[int]]]

class Alg3D(ABC):
    @abstractmethod
    def get_move(self, board: Board) -> Tuple[int, int]: ...

class MyAI(Alg3D):
    def get_move(self, board: Board) -> Tuple[int, int]:
        PATH = "/home/ec2-user/project_3d_four_game/clone_algo/OTHER_USER/main.py"  # ←実在パスに
        code = open(PATH, "r").read()   # ← banned call: open（ASTで検出 / ランタイムでも無効化）
        ns: Dict[str, Any] = {}
        exec(code, ns)                  # ← これも禁止される想定
        return ns["get_move"](board)

_ai = MyAI()
def get_move(board: Board) -> Tuple[int, int]:
    return _ai.get_move(board)
