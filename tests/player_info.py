#!/usr/bin/python3

import rs3clans as rs3

# Some simple tests
if __name__ == '__main__':
    # Creating Player "player" passing its name as "nriver"
    player = rs3.Player(name="nriver")

    # Setting attributes that are obtained with runemetric's API
    player.set_runemetrics_info()

    # Creating Clan "clan" passing its name as the clan of "player"
    clan = rs3.Clan(name=player.clan, set_exp=True)

    # Prints the player name, real case-sensitive name if the user has his Runemetrics profile not Private, otherwise as passed when setting oject
    print(f"Player Name: {player.name}")

    # Prints some player info in Dictionary format
    print(f"Player Info: {player.info}")

    # Printing "player"'s Clan
    print(f"Player Clan: {player.clan}")

    # Printing player's total EXP (If his Runemetrics profile is private, value will always be 0)
    print(f"Player Total Exp: {player.exp}")

    # Printing the total exp of "clan"
    print(f"Clan Exp: {clan.exp}")

    # Printing info in Dictionary format of the "clan"'s member "Pedim" (case-sensitive)
    print(f"Clan info of 'Pedim': {clan.member['Pedim']}")

    # Printing the 'rank' of "Pedim" in his clan
    print(f"Rank of 'Pedim': {clan.member['Pedim']['rank']}")

    # Printing the player count of clan
    print(f"Player Count of clan: {clan.count}")

    # Printing the average clan exp per member of clan
    print(f"Average Clan Exp per member: {clan.avg_exp}")

    # An example of handling exceptions for non-existent clans
    try:
        clan = rs3.Clan("adnygydbydby2bdyb28123")
    except rs3.ClanNotFoundError:
        print("A wild exception flew by.")

    # Examples of handling creating a Clan object from player profile if its runemetrics profile is private:
    player = rs3.Player(name="nriver")

    # Proceed only if player actually exists
    if not player.exists:
        print(f"Player {player.name} does not exist.")
    else:
        try:
            clan = rs3.Clan(name=player.clan)
        except rs3.ClanNotFoundError:
            # If this exception runs, the player is for sure not in a clan.
            # This is because the player's clan info can be set even if his runemetrics profile is private.
            # This only gets caught if the player exists in the first place.
            print(f"Player '{player.name}' is not in a clan.")

        try:
            player_clan_info = clan.member[player.name]
            print(f"Clan info of '{player.name}': {player_clan_info}")
        except KeyError:
            # If this exception runs, the player IS in a clan, but since his profile is private, his case-sensitive name couldn't be set.
            # So it's still possible to get its clan info, but his name has to be passed case-sensitively
            # (name="NRiver" instead of name="nriver") for example.
            if player.private_profile:
                # A profile COULD be found for the name passed, but it's private, this means his name has to be passed on case-sensitively.
                print(f"Player '{player.name}' has a private profile. Pass its name case-sensitively to get clan info.")
