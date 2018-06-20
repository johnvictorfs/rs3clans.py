#!/usr/bin/env python
import rs3clans as rs


def getUserClanExp():
    username = input("Username: ")
    clan_name = input("Clan name: ")

    # Gets user's clan exp from rs3clans.get_user_clan_exp
    clan_exp = rs.get_user_clan_exp(username, clan_name)

    print("Clan exp of {}: {:,}".format(username, clan_exp))
    return clan_exp


import operator
def rankingOfClans():
    rank_dict = dict()
    rank = 1
    while True:
        clan_name = input("Clan name (empty to stop): ")
        if clan_name is '':
            break

        # Stores clan exp in a dictionary with their name being its key
        rank_dict[clan_name] = rs.get_clan_exp(clan_name)

    # Sorts dictionary by clan exp
    sorted_rank_list = sorted(rank_dict.items(), key=operator.itemgetter(1), reverse=True)

    # Prints formatted dictionary from higher to lower exp
    for clan in sorted_rank_list[::1]:
        print("Rank: {}".format(rank))
        for clan_name in clan[0::2]:
            print ("Clan Name: {}".format(clan_name))
        for clan_exp in clan[1::1]:
            print("Clan Exp: {:,}\n".format(clan_exp))
        rank += 1
    return sorted_rank_list
                          

def main():
    print("""
--------------------------------------------
|   What function do you want to test?     |
|   1- getUserClanExp                      |
|   2- rankingOfClans                      |
--------------------------------------------
    """)
    answer = input(">> ")
    if answer is '1':
        getUserClanExp()
    elif answer is '2':
        rankingOfClans()
    else:
        print("That ain't no answer.")
        main()

if __name__ == '__main__':
    main()

