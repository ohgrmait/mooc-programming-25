# Write your solution here

def who_won(game_board: list) -> int:
    player1_piece = 0
    player2_piece = 0
    for row in game_board:
        for piece in row:
            if piece == 1:
                player1_piece += 1
            elif piece == 2:
                player2_piece += 1
    if player1_piece > player2_piece:
        return 1
    elif player2_piece > player1_piece:
        return 2
    else:
        return 0

if __name__ == "__main__":
    print(who_won([[1]]))
