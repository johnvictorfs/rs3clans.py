import pytest

from rs3clans import clans


class TestClans:
    """Tests for a Clan that gets its data from a mocked clan info csv"""
    clan_csv = '''Clanmate, Clan Rank, Total XP, Kills
NRiver,Owner, 50, 4
Player1,Overseer, 50, 3
Player2,General, 200, 0
Player3,Captain, 500, 2
Player Spaces,Captain, 750, 4
Nb\xa0Spaces,Recruit, 200, 6'''

    clan = clans.Clan('name', update_stats=False, set_exp=True)
    clan_list = clan.parse_clan_list(clan_csv)
    clan.update(clan_list)

    def test_parse_clan_list(self):
        with pytest.raises(IndexError):
            self.clan.parse_clan_list('')

        assert self.clan_list[0][0] == 'Clanmate'
        assert self.clan_list[1][0] == 'NRiver'
        assert self.clan_list[1][1] == 'Owner'

    def test_clan_exp(self):
        assert self.clan.exp == (50 + 50 + 200 + 500 + 750 + 200)

    def test_clan_types(self):
        assert isinstance(self.clan.name, str)
        assert isinstance(self.clan.exp, int)
        assert isinstance(self.clan.member, dict)
        assert isinstance(self.clan.avg_exp, float) or isinstance(self.clan.avg_exp, int)
        assert isinstance(self.clan.count, int)
        assert isinstance(self.clan.get_member('NRiver'), clans.ClanMember)

    def test_clan_leader(self):
        leader = self.clan.leader

        assert leader.name == 'NRiver'
        assert leader.rank == 'Owner'
        assert leader.exp == 50

    def test_get_member(self):
        """
        Testing getting a normal Member from a Clan, a Member with spaces in its name, and a Member with non-breaking
        spaces in its name (what is returned by Jagex's API normally)
        """
        assert self.clan.get_member('asdasdasdasdasd') is None

        member = self.clan.get_member('nriver')
        assert member == self.clan.member["NRiver"]
        assert member.name == 'NRiver'
        assert member.rank == 'Owner'
        assert member.exp == 50

        nb_spaces = self.clan.get_member('nb spaces')
        assert nb_spaces == self.clan.member["Nb Spaces"]
        assert nb_spaces.name == 'Nb Spaces'
        assert nb_spaces.rank == 'Recruit'
        assert nb_spaces.exp == 200

        with_spaces = self.clan.get_member('player spaces')
        assert with_spaces == self.clan.member["Player Spaces"]
        assert with_spaces.name == 'Player Spaces'
        assert with_spaces.rank == 'Captain'
        assert with_spaces.exp == 750
