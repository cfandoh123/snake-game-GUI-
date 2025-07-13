# Improved Snake Game

A modern, feature-rich implementation of the classic Snake game built with Python and Pygame.

## 🎮 Features

### Core Gameplay
- **Smooth Controls**: Responsive arrow key controls with proper collision detection
- **Progressive Difficulty**: Speed increases as you collect more food
- **Visual Feedback**: Animated food and gradient snake colors
- **Pause Functionality**: Press 'P' to pause/unpause the game

### User Interface
- **Main Menu**: Navigate between Play Game, High Score, and Quit
- **High Score System**: Persistent high score tracking with JSON storage
- **Game Over Screen**: Shows final score with options to restart or return to menu
- **Visual Polish**: Better graphics, colors, and animations

### Technical Improvements
- **Object-Oriented Design**: Clean, modular code structure
- **Bug Fixes**: Fixed wall collision and self-collision detection
- **Error Handling**: Robust error handling for file operations
- **Type Hints**: Full type annotations for better code maintainability

## 🚀 Installation & Setup

### Prerequisites
- Python 3.6+
- Pygame

### Installation
```bash
# Install pygame
pip install pygame

# Run the improved game
python improved_snake_game.py
```

## 🎯 How to Play

### Controls
- **Arrow Keys**: Move the snake
- **P**: Pause/Unpause the game
- **R**: Restart after game over
- **M**: Return to menu after game over
- **Q**: Quit the game

### Gameplay
1. Navigate through the menu using arrow keys and Enter
2. Control the snake to collect red food squares
3. Avoid hitting walls or your own body
4. The game speeds up as you collect more food
5. Try to beat your high score!

## 🔧 Key Improvements Over Original

### 1. **Bug Fixes**
- **Wall Collision**: Fixed the bug where snake could pass through walls
- **Self-Collision**: Proper detection of snake hitting itself
- **Food Spawning**: Food no longer spawns on the snake's body
- **Stack Overflow**: Eliminated recursive game loop

### 2. **Enhanced User Experience**
- **Menu System**: Professional menu with navigation
- **High Score Tracking**: Persistent score saving
- **Pause Feature**: Ability to pause mid-game
- **Better Visuals**: Gradient snake colors and animated food
- **Larger Display**: Increased from 600x400 to 800x600

### 3. **Code Quality**
- **Class Structure**: Organized into a proper SnakeGame class
- **Type Hints**: Full type annotations for better IDE support
- **Error Handling**: Graceful handling of file operations
- **Documentation**: Comprehensive docstrings
- **Modular Design**: Separated concerns into different methods

### 4. **Game Mechanics**
- **Progressive Speed**: Game gets faster as you progress
- **Better Collision Detection**: More accurate boundary checking
- **Improved Controls**: Prevents 180-degree turns (can't go directly opposite)
- **Visual Feedback**: Clear indication of game state

## 📁 File Structure

```
snake-game-GUI-/
├── game.py                    # Original game
├── improved_snake_game.py     # Improved version
├── README.md                  # Original README
├── README_IMPROVED.md         # This file
└── high_score.json           # High score storage (created automatically)
```

## 🎨 Visual Enhancements

### Snake Appearance
- **Gradient Colors**: Snake body segments have varying shades of green
- **Head Highlighting**: Snake head is darker for easy identification
- **Borders**: Each segment has a black border for definition

### Food Animation
- **Pulsing Effect**: Food size varies slightly for visual appeal
- **Clear Visibility**: Red color with black border

### UI Elements
- **Centered Text**: All text elements are properly centered
- **Color Coding**: Different colors for different UI states
- **Professional Layout**: Clean, modern menu design

## 🔮 Future Enhancements

The improved code structure makes it easy to add new features:

### Potential Additions
- **Sound Effects**: Background music and sound effects
- **Power-ups**: Special food items with temporary effects
- **Multiple Levels**: Different difficulty levels
- **Multiplayer**: Local multiplayer support
- **Achievements**: Unlockable achievements system
- **Customization**: Snake and food skin options

### Technical Improvements
- **Configuration File**: External settings file
- **Save States**: Ability to save and load game progress
- **Statistics**: Detailed game statistics tracking
- **Replay System**: Record and replay games

## 🐛 Known Issues

None currently identified. The improved version addresses all major issues from the original game.

## 🤝 Contributing

Feel free to contribute improvements! The modular design makes it easy to add new features or modify existing ones.

## 📄 License

This project is open source and available under the MIT License.

---

**Enjoy the improved Snake Game!** 🐍 
