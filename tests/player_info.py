#!/usr/bin/python3

import rs3clans as rs3

# Some simple tests
if __name__ == '__main__':
    # Creating Player "player" passing its name as "nriver"
    player = rs3.Player("nriver")

    # Creating Clan "clan" passing its name as the clan of "player"
    clan = rs3.Clan(player.clan, set_exp=True)

    # Prints the player name, real case-sensitive name if the user has his Runemetrics profile not Private, otherwise as passed when setting oject
    print("Player Name:", player.name)

    # Prints some player info in Dictionary format
    print("Player Info:", player.info)

    # Printing "player"'s Clan
    print("Player Clan:", player.clan)

    # Printing player's total EXP (If his Runemetrics profile is private, value will always be 0)
    print("Player Total Exp:", player.exp)

    # Printing the total exp of "clan"
    print("Clan Exp:", clan.exp)

    # Printing info in Dictionary format of the "clan"'s member "Pedim" (case-sensitive)
    print("Clan info of 'Pedim':", clan.member['Pedim'])

    # Printing the 'rank' of "Pedim" in his clan
    print("Rank of 'Pedim':", clan.member['Pedim']['rank'])

    # Printing the player count of clan
    print("Player Count of clan:", clan.count)

    # Printing the average clan exp per member of clan
    print("Average Clan Exp per member:", clan.avg_exp)

    # An example of handling exceptions for non-existent clans
    try:
        clan = rs3.Clan("adnygydbydby2bdyb28123")
    except rs3.ClanNotFoundError:
        print("A wild exception flew by.")
