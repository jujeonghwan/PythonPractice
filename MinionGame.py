def minion_game(string):
    string_length = len(string)
    player1 = 0
    player2 = 0

    for i in range(string_length):
        if string[i] in "AEIOU":
            player1 += string_length - i
        else:
            player2 += string_length - i

    if player1 > player2:
        print ("Kevin", player1)
    elif player1 < player2:
        print ("Stuart", player2)
    else:
        print ("Draw")


s = "BANANA"
minion_game(s)