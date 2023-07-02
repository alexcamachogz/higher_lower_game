# Higher Lower Game

This is a simple Python script for playing the "Higher Lower" game, where you compare the number of followers between two different profiles and guess which one has more followers. The game fetches data from a list of profiles and displays two options for comparison.

## How to Play

1. The game will present two profiles (A and B) with their names, descriptions, and countries.
2. Your task is to guess which profile has more followers.
3. Type 'A' if you think profile A has more followers, or 'B' if you think profile B has more followers.
4. After making a choice, the game will tell you if you guessed correctly and display the current score.
5. The game will continue with new profiles for comparison until you make an incorrect guess.
6. At that point, the game will display your final score.

## How to Run the Game

1. Clone or download the repository to your local machine.
2. Make sure you have Python installed.
3. Run the game by executing the script:
   ```
     python main.py
   ```

## Code Overview

The code is written in Python and consists of the following main functions:
* **clean_display()**: Clears the screen and displays the game logo.
* **random_option()**: Generates a random index to select a profile from the data list.
* **print_option(person)**: Takes a profile dictionary as input and returns a formatted string with the person's name, description, and country.
* **choose_option()**: Requests and validates the user's answer (either 'A' or 'B').
* **compare_followers(a, b)**: Compares the number of followers between two profiles and returns 'a' if the first profile has more followers or 'b' if the second profile has more followers.
* **higher_lower_game(option_a = "")**: The main game loop. It takes an optional option_a parameter that represents the first profile for comparison. If no option_a is provided, it selects a random profile. The function displays the two profiles for comparison and iteratively calls itself with the next profile until the user makes an incorrect guess.

## Note
The data for the game is imported from a separate file called game_data.py. This file contains a list of profiles in the form of dictionaries with information about each person's name, description, country, and follower count. You can customize this data or replace it with your own.

Have fun playing the Higher Lower game!

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
