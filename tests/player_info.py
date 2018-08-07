#!/usr/bin/python3

import rs3clans as rs3

# Some simple tests
if __name__ == '__main__':

    player = rs3.Player("nriver")  # Creating Player "player" passing its name as "nriver"
    clan = rs3.Clan(player.clan, set_exp=True)  # Creating Clan "clan" passing its name as the clan of "player"
    print("Player Name:", player.name)  # Prints the player name, as passed into object Player
    print("Player Info:", player.info)  # Prints some player info in Dictionary format
    print("Player Clan:", player.clan)  # Printing "player"'s Clan
    print("Clan Exp:", clan.exp)  # Printing the total exp of "clan"
    print("Clan info of 'Pedim':", clan.member['Pedim'])  # Printing info in Dictionary format of the "clan"'s member "Pedim" (case-sensitive)
    print("Rank of 'Pedim':", clan.member['Pedim']['rank'])  # Printing the 'rank' of "Pedim" in his clan
    print("Player Count of clan:", clan.count)  # Printing the player count of clan
    print("Average Clan Exp per member:", clan.avg_exp)  # Printing the average clan exp per member of clan

    try:
        clan = Clan("adnygydbydby2bdyb28123")
    except rs3.ClanNotFoundError:
        print("A wild exception flew by.")