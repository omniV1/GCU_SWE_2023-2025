# Owen Lindsey
# CST-180
# 9/24/2025
# war_card_game.py

"""
War Card Game Simulation
This program simulates a modified war card game between two players.
Each player has 26 cards (values 1-13, each appearing twice).
The game plays 10 matches and tracks statistics.
"""

import random

def main():
    # DEFINE deck_of_cards as [1 -> 13]
    # Create a list containing values 1 through 13 (representing card ranks)
    deck_of_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # DEFINE player_1_deck as deck_of_cards + deck_of_cards
    # Create player 1's deck by duplicating the deck_of_cards (26 cards total)
    player_1_deck = deck_of_cards + deck_of_cards
    # DEFINE player_2_deck as deck_of_cards + deck_of_cards  
    # Create player 2's deck by duplicating the deck_of_cards (26 cards total)
    player_2_deck = deck_of_cards + deck_of_cards
    # DEFINE player_1_round_wins as 0
    # Initialize counter for player 1's round wins in current game
    player_1_round_wins = 0
    # DEFINE player_2_round_wins as 0
    # Initialize counter for player 2's round wins in current game
    player_2_round_wins = 0
    # DEFINE player_1_match_wins as 0
    # Initialize counter for player 1's total match wins across all 10 games
    player_1_match_wins = 0
    # DEFINE player_2_match_wins as 0
    # Initialize counter for player 2's total match wins across all 10 games
    player_2_match_wins = 0
    # DEFINE total_ties as 0
    # Initialize counter for total ties across all games
    total_ties = 0
    # DEFINE player_1_win_percentage as 0.0
    # Initialize player 1's win percentage
    player_1_win_percentage = 0.0
    # DEFINE player_2_win_percentage as 0.0
    # Initialize player 2's win percentage
    player_2_win_percentage = 0.0
    # FOR match IN range(1 -> 10):
    # Loop through 10 matches (games)
    for match in range(1, 11):
        print(f"\n=== Game {match} ===")
        
        # RANDOM SHUFFLE player_1_deck
        # Shuffle player 1's deck randomly for each game
        random.shuffle(player_1_deck)
        # RANDOM SHUFFLE player_2_deck
        # Shuffle player 2's deck randomly for each game
        random.shuffle(player_2_deck)
        
        # DEFINE player_1_round_wins as 0  # Reset for each game
        # Reset player 1's round wins for this game
        player_1_round_wins = 0
        # DEFINE player_2_round_wins as 0  # Reset for each game
        # Reset player 2's round wins for this game
        player_2_round_wins = 0
        # FOR round IN range(1 -> 26):
        # Loop through 26 rounds (one for each card in each player's deck)
        for round_num in range(1, 27):
            # DEFINE player_1_card EQUALS player_1_deck[round - 1]  # Draw card for this round
            # Get player 1's card for this round (index is round - 1 because arrays are 0-indexed)
            player_1_card = player_1_deck[round_num - 1]

            # DEFINE player_2_card EQUALS player_2_deck[round - 1]  # Draw card for this round
            # Get player 2's card for this round (index is round - 1 because arrays are 0-indexed)
            player_2_card = player_2_deck[round_num - 1]
            # IF player_1_card GREATER THAN player_2_card:
            # Compare the two cards - if player 1's card is higher
            if player_1_card > player_2_card:  # Replace with actual comparison
                # COMPUTE player_1_round_wins as player_1_round_wins + 1
                # Increment player 1's round wins
                player_1_round_wins += 1
                # PRINT("Player 1 wins round count:", player_1_round_wins)
                # Print the current round win count for player 1
                print(f"Player 1 wins round count: {player_1_round_wins}")
            # ELIF player_1_card LESS THAN player_2_card:
            # If player 2's card is higher
            elif player_1_card < player_2_card:  # Replace with actual comparison
                # COMPUTE player_2_round_wins as player_2_round_wins + 1
                # Increment player 2's round wins
                player_2_round_wins += 1
                # PRINT("Player 2 wins round count:", player_2_round_wins)
                # Print the current round win count for player 2
                print(f"Player 2 wins round count: {player_2_round_wins}")
            # ELSE:
            # If the cards are equal (tie)
            else:
                # COMPUTE total_ties as total_ties + 1
                # Increment the total ties counter
                total_ties += 1
                # PRINT("Tie - no one wins this round")
                # Print that this round was a tie
                print(f"Tie - no one wins this round")
        # After 26 rounds, determine game winner
        # IF player_1_round_wins GREATER THAN player_2_round_wins:
        # Check if player 1 won more rounds in this game
        if player_1_round_wins > player_2_round_wins:  # Replace with actual comparison
            # COMPUTE player_1_match_wins as player_1_match_wins + 1
            # Increment player 1's total match wins
            player_1_match_wins += 1
            # PRINT("Player 1 wins game!")
            # Print that player 1 won this game
            print(f"Player 1 wins game!")
        # ELIF player_2_round_wins GREATER THAN player_1_round_wins:
        # Check if player 2 won more rounds in this game
        elif player_2_round_wins > player_1_round_wins:  # Replace with actual comparison
            # COMPUTE player_2_match_wins as player_2_match_wins + 1
            # Increment player 2's total match wins
            player_2_match_wins += 1
            # PRINT("Player 2 wins game!")
            # Print that player 2 won this game
            print(f"Player 2 wins game!")
        # ELSE:
        # If both players won the same number of rounds (game tie)
        else:
            # COMPUTE total_ties as total_ties + 1
            # Increment the total ties counter
            total_ties += 1
            # PRINT("Game is a tie!")
            # Print that this game was a tie
            print(f"Game is a tie!")
    # COMPUTE player_1_win_percentage as (player_1_match_wins / 10) * 100
    # Calculate player 1's win percentage (matches won out of 10 total matches)
    player_1_win_percentage = (player_1_match_wins / 10) * 100
    # COMPUTE player_2_win_percentage as (player_2_match_wins / 10) * 100
    # Calculate player 2's win percentage (matches won out of 10 total matches)
    player_2_win_percentage = (player_2_match_wins / 10) * 100
    # PRINT("Final Results:")
    # Print header for final results
    
    # PRINT("Player 1 total wins:", player_1_match_wins)
    # Print player 1's total match wins
    print(f"Player 1 total wins: {player_1_match_wins}")
    # PRINT("Player 2 total wins:", player_2_match_wins)
    # Print player 2's total match wins
    print(f"Player 2 total wins: {player_2_match_wins}")
    # PRINT("Total ties:", total_ties)
    # Print total number of ties
    print(f"Total ties: {total_ties}")
    # PRINT("Player 1 win percentage:", player_1_win_percentage, "%")
    # Print player 1's win percentage
    print(f"Player 1 win percentage: {player_1_win_percentage}%")
    # PRINT("Player 2 win percentage:", player_2_win_percentage, "%")
    # Print player 2's win percentage
    print(f"Player 2 win percentage: {player_2_win_percentage}%")
# Call the main function to run the program
if __name__ == "__main__":
    main()
