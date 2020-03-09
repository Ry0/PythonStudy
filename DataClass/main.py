from dataclasses import dataclass
from typing import List, Dict
from dataclasses_json import dataclass_json


@dataclass
class position:
    """[summary] 位置格納用データクラス

        x: int = x座標
        y: int = y座標
    """
    x: int = 0
    y: int = 0


@dataclass(init=False)
class TeachPoint:
    pos: position
    name: str = ""


@dataclass_json
@dataclass(init=False)
class TeachPointList:
    positions: List[TeachPoint]


def print_teach_point(points: List[TeachPoint]):
    for p in points:
        print(p.name)
        print("(" + str(p.pos.x) + ", " + str(p.pos.y) + ")")


def main():
    poslist = TeachPointList()
    tp1 = TeachPoint()
    p1 = position()
    p1.x = 1
    p1.y = 2
    tp1.pos = p1
    tp1.name = "test1"

    tp2 = TeachPoint()
    p2 = position()
    p2.x = 5
    p2.y = 7
    tp2.pos = p2
    tp2.name = "test2"

    point_list = []
    point_list.append(tp1)
    point_list.append(tp2)

    # データクラスに代入
    poslist.positions = point_list

    # 格納したデータの確認
    print_teach_point(poslist.positions)

    # json出力確認
    config_json = poslist.to_json(indent=4, ensure_ascii=False)
    print(config_json)


if __name__ == "__main__":
    main()
