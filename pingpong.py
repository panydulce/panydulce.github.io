import random

def serve_ball():
    return random.choice(["left", "right"])

def play_ping_pong():
    print("Welcome to Text-based Ping Pong!")
    print("Instructions: Type 'left' or 'right' to hit the ball.")
    print("Enter 'quit' to end the game.\n")

    score_player = 0
    score_bot = 0

    while True:
        print(f"Score: Player {score_player} - Bot {score_bot}")
        player_input = input("Enter your move (left/right/quit): ").lower()

        if player_input == 'quit':
            print("Thanks for playing!")
            break

        if player_input not in ['left', 'right']:
            print("Invalid move. Please type 'left' or 'right'.")
            continue

        bot_move = serve_ball()

        if player_input == bot_move:
            print(f"You hit the ball {player_input}. The bot hit it {bot_move}. It's a point for you!")
            score_player += 1
        else:
            print(f"You hit the ball {player_input}. The bot hit it {bot_move}. The bot scored a point!")
            score_bot += 1

        if score_player >= 5 or score_bot >= 5:
            if score_player > score_bot:
                print("Congratulations! You win!")
            else:
                print("The bot wins! Better luck next time!")

            break

if __name__ == "__main__":
    play_ping_pong()
