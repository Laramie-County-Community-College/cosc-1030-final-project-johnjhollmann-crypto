[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=21595539)
# Final Project Information - Model a statistical simulation

We will be writing a program that helps us gain some insight into a situation that can occur in Basketball.  When down 3 with 30 seconds left--it is better to take a hard 3 or an easy two and attempt to get another possession?  We will attempt to answer this by building a type of program called a simulation.  We will take what we have learned about our 'tools' and the idea of abstraction and work toward building some statistics that might drive a decision!

We will be talking about how to build the code as we go, but it is important to know that each student will need to actually implement the code themselves in their Replit.

## Project Deliverables:

Along with your program, provide some description of what your program does and how it's logic works.  A flow chart is a great idea for this deliverable.  You can use any tool you'd like for a flowchart if you choose to go that route.  Hand drawn (and scanned or photographed) images are acceptable.

## Additional Information

### Key Ideas:

*Decision-Making in Basketball:* The transcript discusses the strategic decision of whether to take a 3-pointer or foul an opponent in the final seconds of a basketball game.

Monte Carlo Simulation: A Monte Carlo simulation is a tool to analyze probabilities and make informed decisions. This simulation involves running multiple trials of a scenario to estimate the likelihood of different outcomes.  We will model the end of a basketball game to build one!

Parameters and Assumptions: The simulation relies on various parameters, such as shooting percentages, free-throw percentages, and time remaining. These parameters can be adjusted to explore different scenarios.
Simulation Logic: The simulation models the actions of both teams, including shot attempts, free throws, rebounds, and time management.

Outcome Analysis: By running numerous simulations, the program can determine which strategy (taking a 3-pointer or fouling) is more likely to lead to a win based on the given parameters.
Your Assignment

Based on the provided problem statement, design and create a Python program that simulates the end-game scenario of a basketball game, specifically focusing on the decision of whether to take a 3-pointer or attempt to foul an opponent with poor free-throw shooting.

## Requirements:

Monte Carlo Simulation: Implement a Monte Carlo simulation to run multiple trials of the scenario.

Parameters: Use variables to store (and easily manipulate) the various parameters, such as:

Your 3-point percentage
Your 2-point percentage
Opponent's free-throw percentage
Time remaining in the game
Probability of offensive rebound
Probability of winning in overtime

Scenario Logic: Accurately represent the game logic, including:

Taking a 3-pointer and the potential outcomes (making it, missing it, winning in overtime)
Attempting to foul and the subsequent free-throws and potential offensive rebounds
Time management based on the score difference and time remaining

Output: Display the results of the simulation, including:

The percentage of wins for each strategy (taking a 3-pointer or fouling)
The average number of points scored in each scenario
