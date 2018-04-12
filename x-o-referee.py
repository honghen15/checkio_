def checkio(game_result):
    #print(game_result[0])
    ans = '.'
    if not game_result[0][0] == '.' and game_result[0][0] == game_result[0][1] == game_result[0][2]:
        ans = game_result[0][0]
    elif not game_result[1][0] == '.' and game_result[1][0] == game_result[1][1] == game_result[1][2]:
        ans = game_result[1][0]
    elif not game_result[2][0] == '.' and game_result[2][0] == game_result[2][1] == game_result[2][2]:
        ans = game_result[2][0]
    elif not game_result[0][0] == '.' and game_result[0][0] == game_result[1][0] == game_result[2][0]:
        ans = game_result[0][0]
    elif not game_result[0][1] == '.' and game_result[0][1] == game_result[1][1] == game_result[2][1]:
        ans = game_result[0][1]
    elif not game_result[0][2] == '.' and game_result[0][2] == game_result[1][2] == game_result[2][2]:
        ans = game_result[0][2]
    elif not game_result[0][0] == '.' and game_result[0][0] == game_result[1][1] == game_result[2][2]:
        ans = game_result[0][0]
    elif not game_result[2][0] == '.' and game_result[2][0] == game_result[1][1] == game_result[0][2]:
        ans = game_result[2][0]


    return 'D' if ans == '.' else ans
    #return "D" or "X" or "O"

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    print( checkio([
        "X.O",
        "XX.",
        "XOO"]))# == "X", "Xs wins"
    print( checkio([
        "OO.",
        "XOX",
        "XOX"]))# == "O", "Os wins"
    print( checkio([
        "OOX",
        "XXO",
        "OXX"]))# == "D", "Draw"
    print( checkio([
        "O.X",
        "XX.",
        "XOO"]))# == "X", "Xs wins again"
    print(checkio(["...","XXX","OO."]))
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

