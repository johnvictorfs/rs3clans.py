import pytest
from rs3clans import clans
from rs3clans import ClanNotFoundError
import requests
import csv


CLAN_NAME = 'Atlantis'


def get_clan_list(clan_name):
    clan_url = f'http://services.runescape.com/m=clan-hiscores/members_lite.ws?clanName={clan_name}'
    with requests.Session() as session:
        download = session.get(clan_url)
        decoded = download.content.decode('windows-1252')
        clan_list = list(csv.reader(decoded.splitlines(), delimiter=','))
        if clan_list[0][0] != "Clanmate":
            raise ClanNotFoundError(f"Couldn't find clan: {clan_name}")
        for row in clan_list:
            row[0] = row[0].replace(r"\xa0", " ")
    return clan_list


def get_clan_exp(clan_list):
    return sum(int(row[2]) for row in clan_list[1:])


@pytest.fixture
def valid_clan():
    valid_clan = clans.Clan(CLAN_NAME, set_exp=True)
    return valid_clan


@pytest.fixture
def valid_clan_list():
    return get_clan_list(CLAN_NAME)


@pytest.fixture
def valid_clan_exp(valid_clan_list):
    return get_clan_exp(valid_clan_list)


def test_attribute_types(valid_clan, valid_clan_list):
    assert isinstance(valid_clan.name, str)
    assert isinstance(valid_clan.exp, int)
    assert isinstance(valid_clan.member, dict)
    assert isinstance(valid_clan.avg_exp, float) or isinstance(valid_clan_exp.avg_exp, int)
    assert isinstance(valid_clan.count, int)
    assert isinstance(valid_clan.get_member(valid_clan_list[1][0]), dict)


def test_clan_name(valid_clan):
    assert valid_clan.name == CLAN_NAME


def test_clan_exception():
    with pytest.raises(ClanNotFoundError):
        clans.Clan('clan_that_cannot_possibly_exist_999999')


def test_clan_exp(valid_clan):
    clan_list = get_clan_list(CLAN_NAME)
    clan_exp = get_clan_exp(clan_list)
    assert valid_clan.exp == clan_exp


def test_clan_leader(valid_clan, valid_clan_list):
    valid_clan_leader = None
    for key, value in valid_clan.member.items():
        if value['rank'] == 'Owner':
            valid_clan_leader = key
    assert valid_clan_list[1][0] == valid_clan_leader
