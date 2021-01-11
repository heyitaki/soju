from pytest import fixture
from src.models.boards.round_board import RoundBoard
from src.models.champion import Champion
from src.models.player import Player
from src.models.points.offset_point import OffsetPoint as Offset


@fixture
def player1():
    p1 = Player(id=1, name="player1")
    p1.board.add_champ(Champion.from_name("Veigar"), Offset(0, 0))
    return p1


def test_setup_hexes(player1):
    rb = RoundBoard((player1, player1))
    assert rb.get(Offset(0, 0)) == rb.get(Offset(7, 7))
