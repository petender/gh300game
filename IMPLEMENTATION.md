# Shooting Reflex Game - Implementation Details

## Overview
This Python application tests shooting reflexes by measuring reaction time between target appearance and player response.

## Game Flow

### 1. Player Name Input
- User enters their name using keyboard
- Press ENTER to continue
- Press BACKSPACE to delete characters

### 2. Game Screen Layout
- **Screen Size:** 800x600 pixels
- **Shooter Position:** Bottom middle (blue triangle pointing up)
- **Target Position:** Random location on screen (red/white bullseye)

### 3. Game Mechanics
- Random delay (1-3 seconds) before target appears
- Player presses SPACE bar when they see the target
- Reaction time is calculated from target appearance to SPACE press

### 4. Win/Loss Logic
- **WIN:** Reaction time < 0.3 seconds → Display "YOU WIN!" (green text)
- **LOSE:** Reaction time ≥ 0.3 seconds → Display "YOU ARE TOO SLOW" (red text)

### 5. Results Display
- Shows the exact reaction time in seconds (e.g., "Time: 0.287s")
- Option to play again (press SPACE) or quit (press ESC)

## Controls
- **SPACE:** Shoot when target appears / Start new round
- **ESC:** Quit game
- **ENTER:** Confirm name input
- **BACKSPACE:** Delete character in name input

## Technical Implementation

### Game States
1. **ready:** Initial state showing welcome message
2. **waiting:** Non-blocking delay before target appears
3. **target_shown:** Target is visible, waiting for player response
4. **result:** Shows win/lose message and reaction time

### Key Features
- Non-blocking timer implementation for responsive quit events
- Clean event handling with pygame
- Centered text rendering for better UI
- 60 FPS game loop for smooth performance

## Color Scheme
- **Background:** White
- **Text:** Black (instructions), Green (win), Red (lose)
- **Shooter:** Blue triangle
- **Target:** Red circles with white middle (bullseye pattern)

## Dependencies
- pygame >= 2.5.0
- Python 3.7+
