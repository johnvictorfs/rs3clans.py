import pytest
from rs3clans import players

"""
Test Account created for the purpose of those tests:

In-game Name: pyTestAcc
Clan: None
Total Exp: 1_254
Private Profile: False
Woodcutting Exp: 100
Woodcutting Level: 2
Constitution Exp: 1_154
"""


@pytest.fixture
def valid_player():
    valid_player = players.Player('pytestacc')
    return valid_player


def test_player_doesnt_exist_no_runemetrics():
    player = players.Player('non_existent_player_99999', runemetrics=False)
    assert not player.exists


def test_player_doesnt_exist():
    player = players.Player('non_existent_player_99999')
    assert not player.exists


def test_player_doesnt_exist_with_spaces():
    player = players.Player('non existent player with spaces')
    assert not player.exists


def test_player_clan(valid_player):
    assert not valid_player.clan


def test_player_exists(valid_player):
    assert valid_player.exists


def test_player_name(valid_player):
    assert valid_player.name == 'pyTestAcc'


def test_player_exp(valid_player):
    assert valid_player.exp == 1_254


def test_attribute_types(valid_player):
    assert isinstance(valid_player.exp, int)
    assert isinstance(valid_player.skill_values, list)
    assert isinstance(valid_player.exists, bool)
    assert isinstance(valid_player.title, str)


@pytest.mark.parametrize("skill, result",
                         [
                             ('woodcutting', 2),
                             ('wOoDcutTing', 2),
                             ('atTaCk', 1),
                             ('attack', 1),
                             ('ConstItuTion', 10),
                             ('constitution', 10),
                             (3, 10),
                             (8, 2),
                             (0, 1),
                             (26, 1),
                             (13, 1),
                         ])
def test_skill_level(valid_player, skill, result):
    assert valid_player.skill(skill).level == result


@pytest.mark.parametrize("skill, result",
                         [
                             ('woodcutting', 100),
                             ('WoOdcuttIng', 100),
                             ('constitution', 1_154),
                             ('CoNsTiTutioN', 1_154),
                             ('attack', 0),
                             ('aTTacK', 0),
                             (3, 1_154),
                             (8, 100),
                             (0, 0),
                             (26, 0),
                             (13, 0),
                         ])
def test_skill_exp(valid_player, skill, result):
    assert valid_player.skill(skill).exp == result


def test_status_codes(valid_player):
    assert valid_player.runemetrics_status_code == 200
    assert valid_player.details_status_code == 200
