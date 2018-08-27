Usage examples
=======================================

* Usage Examples:

Importing::
    >>> import rs3clans as rs3

Creating object Player passing its name as "nriver"::
    >>> player = rs3.Player(name="nriver")

Creating Clan "clan" passing its name as the clan of "player" with set_exp ::
    >>> clan = rs3.Clan(name=player.clan, set_exp=True)

Printing the player name, real case-sensitive name if the user has his Runemetrics profile not Private, otherwise as passed when creating object::
    >>> print(f"Player Name: {player.name}")
    Player Name: NRiver

Printing some player info in Dictionary format::
    >>> print(f"Player Info: {player.info}")
    Player Info: {'isSuffix': True, 'recruiting': True, 'name': 'NRiver', 'clan': 'Atlantis', 'title': 'the Liberator'}

Printing player's clan name::
    >>> print(f"Player Clan: {player.clan}")
    Player Clan: Atlantis

Printing player's total Exp, or None if his Runemetrics profile is private::
    >>> print(f"Player Total Exp: {player.exp}")
    Player Total Exp: 1037291112

Printing the total exp of clan::
    >>> print(f"Clan Exp: {clan.exp}")
    Clan Exp: 151349638333

Printing info in Dictionary format of the clan's member "Pedim" (requires case-sensitive name)::
    >>> print(f"Clan info of 'Pedim': {clan.member['Pedim']}")
    Clan info of 'Pedim': {'rank': 'Owner', 'exp': 739711654}

Printing the rank of member "Pedim" in his clan::
    >>> print(f"Rank of 'Pedim': {clan.member['Pedim']['rank']}")
    Rank of 'Pedim': Owner

Printing the total player count of clan::
    >>> print(f"Player Count of clan: {clan.count}")
    Player Count of clan: 499

Printing the average clan exp per member of clan::
    >>> print(f"Average Clan Exp per member: {clan.avg_exp}")
    Average Clan Exp per member: 303305888.44288576

* Handling exceptions/errors:

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