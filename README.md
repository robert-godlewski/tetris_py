# Description
This version of tetris was made with PyGame.

# To run in terminal
> % `bash tetris.sh`

# Todos
- [ ] Add in necessary classes
- [ ] Add in 32 x 32 block grid
- [ ] Fix Game Logic
- [ ] Add in other Graphics
- [ ] Add in Audio
- [ ] Game Testing and bug fixes
- [ ] Web Page to deploy

## Game Classes Needed
- [ ] Add in Game Grid Class: 2D array with 10 columns and 20 rows - In the process
- [ ] Add in Tetromino Shape Classes
  - [ ] Add in I shape and possible rotations
  - [ ] Add in O shape and possible rotations
  - [ ] Add in T shape and possible rotations
  - [ ] Add in S shape and possible rotations
  - [ ] Add in Z shape and possible rotations
  - [ ] Add in J shape and possible rotations
  - [ ] Add in L shape and possible rotations
- [ ] Add in a Scoreboard Class - In the process

## Game Logic Needed
- [ ] Piece Movement
  - [ ] Pieces should drop automatically due to gravity and faster when pressed down
  - [ ] Can move the pieces left and right
- [ ] Rotation: Add in rotation mechanism for the tetrominoes recalculating the block positions based on a pivot point and checking for collisions.
- [ ] Collision Detection
- [ ] Locking Pieces: When the current Tetromino reaches the bottom or lands on another block the game locks it in place and updates the game grid with occupied cells
- [ ] Row Clearing: Detect and clear full rows, shift the blocks aboce down and update the score
- [ ] Game Over Condition: Determine if the game ends when the new tetromino cannot move at all due to existing blocks

## Graphic Assets Needed
- [x] 32 x 32 test block
- [ ] 32 x 32 block grid
- [ ] 32 x 32 Blocks for each tetromino shape
- [ ] Scoreboard
- [ ] Game Over Screen
- [ ] Pause/ unpause button
- [ ] etc

## Audio Assets Needed
- [ ] Theme music
- [ ] Game Over
- [ ] Row Clearing
- [ ] Piece movement
- [ ] Piece rotation
- [ ] etc

# Features
These are all things to consider to be part of the game.  With most games it's good to have 5 to 15 features.  Start of Development on May 22, 2025

## Current Features
This is so far the list of features within this project we currently have:
* none

## Future Features
* Web-based
* Mobile friendly
* Console - later on especially Steam Deck
* Able to use a gamepad
* Multiplayer?

### OS Compatibility
Must implement:
- [ ] MacOS: To locally play on my computer
- [ ] Windows: To be accessible with to others
- [ ] Linux: To be accessible with devices like Steam Deck
- [ ] Web-based: To be able to play on the website

Skipping for now because we might implement this game in a puzzle collection game instead
- [ ] iOS
- [ ] Android
- [ ] Nintendo System
- [ ] Xbox System
- [ ] PlayStation System

### Controller Scheme
- [ ] Mouse and Keyboard
- [ ] Touch
- [ ] Gamepad
  - [ ] Nintendo Switch Pro
  - [ ] Xbox Wireless Controller
  - [ ] PlayStation DualSense (PS5)

## Game Art
We will ultimately use GIMP to develop sprites and graphics for the game.

Needs:
- [ ] Block sprites
- [ ] Background
- [ ] Scoreboard
- [ ] Title Menu

## Audio Files
We will ultimately use Logic Pro X to develop the sounds for this game.

Needs:
- [ ] Music
- [ ] Block Sound Effects
- [ ] Level Transition Sound Effects
- [ ] Selecting items in the menu

## Platforms
Will need to add this to platforms to sell later on.  Most likely will just have this published on a website for free (or little money).

List:
* Steam (Most Popular)
* Epic
* GOG
* Itch.io
* Apple App Store - Puzzle Collection
* Google Play Store - Puzzle Collection
* Nintendo Store - Puzzle Collection
* Xbox Live - Puzzle Collection
* PlayStation Network - Puzzle Collection

# References
* [PyGame](https://www.pygame.org/docs/)
* [Tech with Tim Tutorial](https://github.com/techwithtim/Python-Platformer.git)
