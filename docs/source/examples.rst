Examples
=======================================

* Installing::
    - `python -m pip install rs3clans`

Usage
-----

Importing::
    >>> import rs3clans as rs3

Creating object Player passing its name as "nriver"::
    >>> player = rs3.Player(name="nriver")
    >>> # If runemetrics is True when creating object Player
    >>> # set_runemetrics_info() method will run by default
    >>> player.rs3.Player(name="nriver", runemetrics=True)

Creating Clan "clan" passing its name as the clan of "player" with set_exp ::
    >>> clan = rs3.Clan(name=player.clan, set_exp=True)

Setting player's attributes that are obtained with Runemetric's API::
    >>> # Not needed if runemetrics was True when creating Player
    >>> player.set_runemetrics_info()

Getting Player name, real case-sensitive name if the user has his Runemetrics profile not Private, otherwise as passed when creating object::
    >>> player.name
    NRiver

Generic player info::
    >>> player
    Name: NRiver Clan: Atlantis Exists: True

Getting information of specific skills from the player::
    >>> player.skill('agility').level
    99
    >>> # Can pass skill names as well as id
    >>> # (8 = Woodcutting for example)
    >>> player.skill(8).exp
    14054178.6
    >>> player.skill('AtTaCk').rank
    68311

Getting some player info in Dictionary format::
    >>> player.info
    {'isSuffix': True, 'recruiting': True, 'name': 'NRiver', 'clan': 'Atlantis', 'title': 'the Liberator'}

Getting player's clan name::
    >>> player.clan
    Atlantis

Getting player's total Exp, or None if his Runemetrics profile is private::
    >>> player.exp
    1037291112

Getting the total exp of clan::
    >>> clan.exp
    151349638333

Getting info in Dictionary format of the clan's member "Pedim" (case-sensitive)::
    >>> clan.member['Pedim']
    {'rank': 'Owner', 'exp': 739711654}

Getting info in Dictionary format of the clan's member "NRiver" (case insensitive)::
    >>> clan.get_member('nRiVeR')
    {'rank': 'Overseer', 'exp': 1041963324}
    >>> clan.get_member('nriver')
    {'rank': 'Overseer', 'exp': 1041963324}


Getting the rank of member "Pedim" in his clan::
    >>> # Case-sensitive way
    >>> clan.member['Pedim']['rank']
    Owner
    >>> # Case-insensitive way
    >>> clan.get_member('pedim')['rank']
    Owner

Getting the total player count of clan::
    >>> clan.count
    499

Getting the average clan exp per member of clan::
    >>> clan.avg_exp
    303305888.44288576

Handling exceptions/errors:
---------------------------
Dealing with non-existent clans::
    >>> try:
    ...     clan = rs3.Clan("adnygydbydby2bdyb28123")
    ... except rs3.ClanNotFoundError:
    ...     print("A wild exception flew by.")
    A wild exception flew by.

Dealing with non-existent players::
    >>> player = rs3.Player(name="iub2323bf32ubfjsdbf8723bf23f")
    >>> if not player.exists:
    ...     print(f"Player '{player.name}'' does not exist.")
    Player 'iub2323bf32ubfjsdbf8723bf23f' does not exist.

Getting information only if player exists::
    >>> player = rs3.Player(name="nriver")
    >>> if not player.exists:
    ...     print(f"Player {player.name} does not exist.")
    ... else:
    ...     try:
    ...         clan = rs3.Clan(name=player.clan)
    ...     except rs3.ClanNotFoundError:
    ...         # If this exception runs, the player is for sure not in a clan.
    ...         # This is because the player's clan info can be set even if his runemetrics profile is private.
    ...         # This only gets caught if the player exists in the first place.
    ...         print(f"Player '{player.name}' is not in a clan.")
    ...     try:
    ...         player_clan_info = clan.member[player.name]
    ...         print(f"Clan info of '{player.name}': {player_clan_info}")
    ...     except KeyError:
    ...     # If this exception runs, the player IS in a clan, but since his profile is private, his case-sensitive name couldn't be set.
    ...     # So it's still possible to get its clan info, but his name has to be passed case-sensitively
    ...     # (name="NRiver" instead of name="nriver") for example.
    ...        if player.private_profile:
    ...        # A profile COULD be found for the name passed, but it's private, this means his name has to be passed on case-sensitively.
    ...        print(f"Player '{player.name}' has a private profile. Pass its name case-sensitively to get clan info.")