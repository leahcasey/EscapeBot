# EscapeBot
The Python Chatbot Escape Room Game is an interactive, trivia-based escape game where players must answer a series of questions correctly to progress and ultimately "escape." The game dynamically loads questions from python_game_file.txt into a nested dictionary format, which is then passed to an instance of EscapeBot for gameplay.

Gameplay Overview
At the start, the player is given the option to begin or exit. If they choose to play, the EscapeBot presents a series of multiple-choice questions along with corresponding stimuli. The player must select the correct answer to move forward.
Correct answers allow progression to the next question.
Incorrect answers result in the loss of a life:
If the player has lives remaining, they are given another chance to answer the same question.
If the player runs out of lives, the game ends with a final message.
The game continues until the player answers all questions correctly or loses all lives.

Features

Changing Question Sets:
Once a player successfully completes the game, they are given the option to play again with a completely new set of questions, stimuli, and answers.
This feature showcases inheritance, method overriding, and object interactions, as the game dynamically switches to a new dataset using object-oriented principles.

Bonus Life Mechanic:
If a player reaches only 1 remaining life and then answers the next question correctly, they gain an extra life as a reward.
This feature demonstrates concepts of OOP principles, methods, and variable scope (class, instance, and private variables) by modifying the game’s life system dynamically.

Technical Highlights
Utilizes file handling to read and structure questions dynamically.
Implements object-oriented programming (OOP) concepts for clean, modular code.
Features user input handling and randomized answer presentation for an engaging gameplay experience.
This project combines file management, class-based architecture, and interactive gameplay mechanics to create a challenging and dynamic escape room experience.
