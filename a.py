number_of_game_played = input()
result_of_each_game = input()
#print(type(number_of_game_played))
#rint(type(result_of_each_game))
A_win = 0
D_win = 0
for i in result_of_each_game:
    if i == "A":
        A_win +=1
    else:
        D_win += 1
if A_win > D_win:
    print("Anton")
elif  A_win == D_win:
    print("Friendship")
else:
    print("Danik")

