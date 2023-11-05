class Player:
   pass

class Team:
    pass

def main():
    player1 = Player("Gunnar Jónsson", "Keflavík", 17, 3)
    print(player1)
    player2 = Player("Anna Sigurðardóttir", "Breiðablik", 14, 5)
    print(player2)
    player3 = Player("Guðmundur Einarsson", "Keflavík", 11, 4)
    print(player3)
    player4 = Player("Sigrún Kjartansdóttir", "Breiðablik", 21, 6)
    print(player4)

    player1.add_game(3)
    player2.add_game(6)

    keflavik = Team("Keflavík")
    keflavik.add_player(player1)
    keflavik.add_player(player3)
    print(keflavik)

    breidablik = Team("Breiðablik")
    breidablik.add_player(player2)
    breidablik.add_player(player4)
    print(breidablik)

main()
