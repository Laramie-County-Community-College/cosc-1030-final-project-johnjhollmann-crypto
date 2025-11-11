import random

# Constants for time taken in the simulation (approximate values)
TIME_PER_3PT_POSSESSION = 5       # Time for an offensive set and shot
TIME_PER_2PT_POSSESSION = 5       # Time for a quick two-point attempt
TIME_PER_REBOUND_AND_SHOT = 4     # Time to grab a rebound and get another shot off
TIME_PER_FOUL_POSSESSION = 0.5    # Time it takes to commit an intentional foul
TIME_PER_FREETROW = 0.8           # Time per free throw attempt
TIME_PER_OPP_POSSESSION = 10      # Time for opponent to get ball back and score


def simulate_game_ending(score_diff, time_left, strategy, params):
    """Simulates the entire game ending from the initial state."""
    current_score_diff = score_diff
    current_time = time_left
    
    has_ball = True

    if strategy == "3_pointer":
        # Simulate the single, final possession with a 3-point attempt
        if has_ball and current_time >= TIME_PER_3PT_POSSESSION:
            current_time -= TIME_PER_3PT_POSSESSION
            if random.random() < params['my_3pt_pct']:
                current_score_diff += 3
                
                # After a successful 3-pointer, opponent gets the ball back
                if current_time >= TIME_PER_OPP_POSSESSION:
                    current_time -= TIME_PER_OPP_POSSESSION
                    if random.random() < params['opp_poss_score_pct']:
                        current_score_diff -= 2 # Assume opponent scores a 2-pointer
                else: # Not enough time for opponent possession, game is over
                    pass
            else:
                if current_time >= TIME_PER_REBOUND_AND_SHOT and random.random() < params['off_rebound_pct']:
                    current_time -= TIME_PER_REBOUND_AND_SHOT
                    if random.random() < params['my_2pt_pct_rebound']:
                        current_score_diff += 2
        
    elif strategy == "foul_opponent":
        # First, simulate the losing team's quick 2-point attempt
        if has_ball and current_time >= TIME_PER_2PT_POSSESSION:
            current_time -= TIME_PER_2PT_POSSESSION
            if random.random() < params['my_2pt_pct_rebound']:
                current_score_diff += 2
            
            # Now, simulate the fouling sequence if still behind
            if current_score_diff < 0:
                while current_time > 0 and current_score_diff < 0:
                    # Foul the opponent
                    current_time -= TIME_PER_FOUL_POSSESSION

                    # Opponent shoots first free throw
                    if random.random() < params['opp_ft_pct']:
                        current_score_diff -= 1
                    current_time -= TIME_PER_FREETROW

                    # Opponent shoots second free throw
                    if random.random() < params['opp_ft_pct']:
                        current_score_diff -= 1
                    else:
                        # Missed second free throw, check for defensive rebound
                        if random.random() < (1 - params['ft_rebound_pct']):
                            has_ball = True
                            current_time -= TIME_PER_REBOUND_AND_SHOT
                        else:
                            # Opponent offensive rebound, game likely over
                            has_ball = False
                            current_time = 0

                    # My team now has the ball with a chance to score
                    if has_ball and current_time > 0:
                        if random.random() < params['my_2pt_pct_rebound']:
                            current_score_diff += 2
                        current_time -= TIME_PER_2PT_POSSESSION
                    
                    has_ball = False

    return current_score_diff

def monte_carlo_basketball_simulation_time(
    num_simulations,
    params,
    initial_score_diff,
    initial_time_remaining
):
    """
    Simulates basketball end-game scenarios with time management using a Monte Carlo approach.
    """
    wins_3pt = 0
    wins_foul = 0
    total_points_3pt = 0
    total_points_foul = 0

    for _ in range(num_simulations):
        # Scenario 1: Attempt a 3-pointer
        final_score_3pt = simulate_game_ending(
            initial_score_diff, initial_time_remaining, "3_pointer", params
        )
        
        if final_score_3pt > 0:
            wins_3pt += 1
        elif final_score_3pt == 0:
            if random.random() < params['ot_win_pct']:
                wins_3pt += 1
        
        total_points_3pt += final_score_3pt

        # Scenario 2: Foul the opponent
        final_score_foul = simulate_game_ending(
            initial_score_diff, initial_time_remaining, "foul_opponent", params
        )
        
        if final_score_foul > 0:
            wins_foul += 1
        elif final_score_foul == 0:
            if random.random() < params['ot_win_pct']:
                wins_foul += 1
        
        total_points_foul += final_score_foul
        
    return {
        "3_pointer": {
            "win_percentage": (wins_3pt / num_simulations) * 100,
            "average_score": total_points_3pt / num_simulations
        },
        "foul_opponent": {
            "win_percentage": (wins_foul / num_simulations) * 100,
            "average_score": total_points_foul / num_simulations
        }
    }

if __name__ == "__main__":
    # --- Parameters ---
    NUM_SIMULATIONS = 100000
    
    # Team stats parameters
    simulation_params = {
        'my_3pt_pct': 0.35,
        'my_2pt_pct_rebound': 0.50,
        'opp_ft_pct': 0.65,
        'off_rebound_pct': 0.25,
        'ft_rebound_pct': 0.20,
        'ot_win_pct': 0.50,
        'opp_poss_score_pct': 0.50, # New parameter: opponent scoring percentage after a made 3
    }

    # Game situation
    SCORE_DIFFERENCE = -3
    TIME_REMAINING = 30

    # --- Run Simulation ---
    results = monte_carlo_basketball_simulation_time(
        num_simulations=NUM_SIMULATIONS,
        params=simulation_params,
        initial_score_diff=SCORE_DIFFERENCE,
        initial_time_remaining=TIME_REMAINING
    )

    # --- Display Output ---
    print(f"Simulation of {NUM_SIMULATIONS} end-game scenarios with {TIME_REMAINING} seconds left:")
    print("Team down by 3 starts with the ball.")
    print("-" * 40)
    print("Strategy: Attempt 3-Pointer on the first possession")
    print(f"  Win Percentage: {results['3_pointer']['win_percentage']:.2f}%")
    print(f"  Average Score Difference: {results['3_pointer']['average_score']:.2f}")
    print("\nStrategy: Attempt Quick 2-Pointer, then Foul")
    print(f"  Win Percentage: {results['foul_opponent']['win_percentage']:.2f}%")
    print(f"  Average Score Difference: {results['foul_opponent']['average_score']:.2f}")
    print("-" * 40)
    
    if results['3_pointer']['win_percentage'] > results['foul_opponent']['win_percentage']:
        print("Conclusion: In this scenario, attempting a 3-pointer on the first possession yields a higher win percentage.")
    else:
        print("Conclusion: In this scenario, the strategy of attempting a quick 2-pointer followed by fouling yields a higher win percentage.")
