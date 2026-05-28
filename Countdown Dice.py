import random


def get_num_players() -> int:
    while True:
        try:
            n = int(input("Enter the number of players(2-4): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue
        if 2 <= n <= 4:
            return n
        print("Number of players must be between 2 and 4.")


def main() -> None:
    num_players = get_num_players()

    players = []
    scores = []
    for i in range(num_players):
        name = input(f"Enter name of player {i + 1} : ").strip() or f"Player {i + 1}"
        players.append(name)
        scores.append(50)

    round_num = 1
    game_won = False

    while not game_won:
        print(f"\n== ROUND {round_num}")
        round_num += 1

        for i in range(num_players):
            current_player = players[i]
            current_score = scores[i]

            print(f"\n{current_player}'s turn! Current Score: {current_score}")
            input("Press Enter to roll the die...")
            roll = random.randint(1, 6)
            print(f"Rolled: {roll}")

            remaining = current_score - roll

            if remaining == 0:
                scores[i] = 0
                print(f"EXACT HIT! {current_player} wins the game!")
                game_won = True
                break
            elif remaining < 0:
                # Bust: score stays the same
                print(f"BUST! You rolled too high. Score stays at {current_score}.")
            else:
                scores[i] = remaining
                print(f"📉 New Score: {scores[i]}")

        # Optional end-of-round display (kept minimal)
        # if not game_won:
        #     print("\nScores:")
        #     for p, s in zip(players, scores):
        #         print(f"- {p}: {s}")


if __name__ == "__main__":
    main()

