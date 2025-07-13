import pygame
import random
import json
import os
from typing import List, Tuple, Optional

class SnakeGame:
    def __init__(self):
        pygame.init()
        
        # Colors
        self.WHITE = (255, 255, 255)
        self.YELLOW = (255, 255, 102)
        self.BLACK = (0, 0, 0)
        self.RED = (213, 50, 80)
        self.GREEN = (0, 255, 0)
        self.BLUE = (50, 153, 213)
        self.DARK_GREEN = (0, 200, 0)
        self.GRAY = (128, 128, 128)
        
        # Game settings
        self.DIS_WIDTH = 800
        self.DIS_HEIGHT = 600
        self.SNAKE_BLOCK = 20
        self.INITIAL_SPEED = 10
        self.SPEED_INCREMENT = 0.5
        
        # Initialize display
        self.dis = pygame.display.set_mode((self.DIS_WIDTH, self.DIS_HEIGHT))
        pygame.display.set_caption('Calvin\'s Snake Game')
        
        # Fonts
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
        self.title_font = pygame.font.SysFont("bahnschrift", 50)
        
        # Game state
        self.clock = pygame.time.Clock()
        self.high_score = self.load_high_score()
        
        # Sound effects (if available)
        self.sounds = {}
        self.load_sounds()
    
    def load_sounds(self):
        """Load sound effects if available"""
        try:
            # You can add sound files to make this work
            pass
        except:
            pass
    
    def load_high_score(self) -> int:
        """Load high score from file"""
        try:
            if os.path.exists('high_score.json'):
                with open('high_score.json', 'r') as f:
                    data = json.load(f)
                    return data.get('high_score', 0)
        except:
            pass
        return 0
    
    def save_high_score(self, score: int):
        """Save high score to file"""
        try:
            with open('high_score.json', 'w') as f:
                json.dump({'high_score': score}, f)
        except:
            pass
    
    def draw_score(self, score: int, high_score: int):
        """Draw current score and high score"""
        score_text = self.score_font.render(f"Score: {score}", True, self.YELLOW)
        high_score_text = self.score_font.render(f"High Score: {high_score}", True, self.YELLOW)
        self.dis.blit(score_text, [10, 10])
        self.dis.blit(high_score_text, [10, 50])
    
    def draw_snake(self, snake_list: List[List[int]]):
        """Draw the snake with gradient colors"""
        for i, segment in enumerate(snake_list):
            # Create gradient effect - head is darker
            if i == len(snake_list) - 1:  # Head
                color = self.DARK_GREEN
            else:
                # Body segments get progressively lighter
                intensity = max(100, 255 - (len(snake_list) - i) * 10)
                color = (0, intensity, 0)
            
            pygame.draw.rect(self.dis, color, [segment[0], segment[1], self.SNAKE_BLOCK, self.SNAKE_BLOCK])
            # Add border
            pygame.draw.rect(self.dis, self.BLACK, [segment[0], segment[1], self.SNAKE_BLOCK, self.SNAKE_BLOCK], 1)
    
    def draw_food(self, food_pos: Tuple[int, int]):
        """Draw food with animation effect"""
        x, y = food_pos
        # Draw food with a pulsing effect
        size = self.SNAKE_BLOCK + int(2 * abs(pygame.time.get_ticks() % 1000 - 500) / 500)
        pygame.draw.rect(self.dis, self.RED, [x, y, size, size])
        pygame.draw.rect(self.dis, self.BLACK, [x, y, size, size], 1)
    
    def generate_food(self, snake_list: List[List[int]]) -> Tuple[int, int]:
        """Generate food position that doesn't overlap with snake"""
        while True:
            foodx = round(random.randrange(0, self.DIS_WIDTH - self.SNAKE_BLOCK) / self.SNAKE_BLOCK) * self.SNAKE_BLOCK
            foody = round(random.randrange(0, self.DIS_HEIGHT - self.SNAKE_BLOCK) / self.SNAKE_BLOCK) * self.SNAKE_BLOCK
            
            # Check if food position doesn't overlap with snake
            if [foodx, foody] not in snake_list:
                return (foodx, foody)
    
    def check_collision(self, x: int, y: int, snake_list: List[List[int]]) -> bool:
        """Check for wall or self collision"""
        # Wall collision
        if x >= self.DIS_WIDTH or x < 0 or y >= self.DIS_HEIGHT or y < 0:
            return True
        
        # Self collision (check against all body segments)
        if [x, y] in snake_list[:-1]:
            return True
        
        return False
    
    def show_menu(self) -> str:
        """Show main menu and return user choice"""
        menu = True
        selected = 0
        options = ["Play Game", "High Score", "Quit"]
        
        while menu:
            self.dis.fill(self.BLUE)
            
            # Draw title
            title = self.title_font.render("SNAKE GAME", True, self.YELLOW)
            title_rect = title.get_rect(center=(self.DIS_WIDTH/2, 100))
            self.dis.blit(title, title_rect)
            
            # Draw menu options
            for i, option in enumerate(options):
                color = self.YELLOW if i == selected else self.WHITE
                text = self.font_style.render(option, True, color)
                text_rect = text.get_rect(center=(self.DIS_WIDTH/2, 250 + i * 50))
                self.dis.blit(text, text_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        selected = (selected - 1) % len(options)
                    elif event.key == pygame.K_DOWN:
                        selected = (selected + 1) % len(options)
                    elif event.key == pygame.K_RETURN:
                        return options[selected].lower().replace(" ", "_")
        
        return "quit"
    
    def show_high_score(self):
        """Show high score screen"""
        showing = True
        while showing:
            self.dis.fill(self.BLUE)
            
            title = self.title_font.render("HIGH SCORE", True, self.YELLOW)
            title_rect = title.get_rect(center=(self.DIS_WIDTH/2, 200))
            self.dis.blit(title, title_rect)
            
            score_text = self.score_font.render(f"{self.high_score}", True, self.WHITE)
            score_rect = score_text.get_rect(center=(self.DIS_WIDTH/2, 300))
            self.dis.blit(score_text, score_rect)
            
            back_text = self.font_style.render("Press any key to go back", True, self.YELLOW)
            back_rect = back_text.get_rect(center=(self.DIS_WIDTH/2, 400))
            self.dis.blit(back_text, back_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    return "menu"
        
        return "menu"
    
    def show_game_over(self, score: int) -> str:
        """Show game over screen"""
        game_over = True
        new_high_score = score > self.high_score
        
        if new_high_score:
            self.high_score = score
            self.save_high_score(score)
        
        while game_over:
            self.dis.fill(self.BLUE)
            
            # Game over message
            if new_high_score:
                title = self.title_font.render("NEW HIGH SCORE!", True, self.YELLOW)
            else:
                title = self.title_font.render("GAME OVER", True, self.RED)
            
            title_rect = title.get_rect(center=(self.DIS_WIDTH/2, 150))
            self.dis.blit(title, title_rect)
            
            # Score display
            score_text = self.score_font.render(f"Score: {score}", True, self.WHITE)
            score_rect = score_text.get_rect(center=(self.DIS_WIDTH/2, 250))
            self.dis.blit(score_text, score_rect)
            
            # Instructions
            restart_text = self.font_style.render("Press 'R' to Play Again", True, self.YELLOW)
            menu_text = self.font_style.render("Press 'M' for Menu", True, self.YELLOW)
            quit_text = self.font_style.render("Press 'Q' to Quit", True, self.YELLOW)
            
            restart_rect = restart_text.get_rect(center=(self.DIS_WIDTH/2, 350))
            menu_rect = menu_text.get_rect(center=(self.DIS_WIDTH/2, 400))
            quit_rect = quit_text.get_rect(center=(self.DIS_WIDTH/2, 450))
            
            self.dis.blit(restart_text, restart_rect)
            self.dis.blit(menu_text, menu_rect)
            self.dis.blit(quit_text, quit_rect)
            
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        return "play"
                    elif event.key == pygame.K_m:
                        return "menu"
                    elif event.key == pygame.K_q:
                        return "quit"
        
        return "quit"
    
    def game_loop(self) -> str:
        """Main game loop"""
        # Initialize game state
        x1 = self.DIS_WIDTH // 2
        y1 = self.DIS_HEIGHT // 2
        
        x1_change = 0
        y1_change = 0
        
        snake_list = []
        length_of_snake = 1
        speed = self.INITIAL_SPEED
        
        # Generate initial food
        food_pos = self.generate_food(snake_list)
        
        # Game state
        game_over = False
        paused = False
        
        while not game_over:
            # Handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return "quit"
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = not paused
                    elif not paused:
                        if event.key == pygame.K_LEFT and x1_change <= 0:
                            x1_change = -self.SNAKE_BLOCK
                            y1_change = 0
                        elif event.key == pygame.K_RIGHT and x1_change >= 0:
                            x1_change = self.SNAKE_BLOCK
                            y1_change = 0
                        elif event.key == pygame.K_UP and y1_change <= 0:
                            y1_change = -self.SNAKE_BLOCK
                            x1_change = 0
                        elif event.key == pygame.K_DOWN and y1_change >= 0:
                            y1_change = self.SNAKE_BLOCK
                            x1_change = 0
            
            if paused:
                # Show pause message
                pause_text = self.font_style.render("PAUSED - Press P to continue", True, self.YELLOW)
                pause_rect = pause_text.get_rect(center=(self.DIS_WIDTH/2, self.DIS_HEIGHT/2))
                self.dis.blit(pause_text, pause_rect)
                pygame.display.update()
                continue
            
            # Update snake position
            x1 += x1_change
            y1 += y1_change
            
            # Check for collisions
            if self.check_collision(x1, y1, snake_list):
                return self.show_game_over(length_of_snake - 1)
            
            # Update display
            self.dis.fill(self.BLUE)
            
            # Draw food
            self.draw_food(food_pos)
            
            # Update snake
            snake_head = [x1, y1]
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]
            
            # Draw snake
            self.draw_snake(snake_list)
            
            # Draw score
            self.draw_score(length_of_snake - 1, self.high_score)
            
            # Check for food collision
            if x1 == food_pos[0] and y1 == food_pos[1]:
                food_pos = self.generate_food(snake_list)
                length_of_snake += 1
                # Increase speed
                speed += self.SPEED_INCREMENT
            
            pygame.display.update()
            self.clock.tick(speed)
        
        return "quit"
    
    def run(self):
        """Main game runner"""
        current_state = "menu"
        
        while current_state != "quit":
            if current_state == "menu":
                current_state = self.show_menu()
            elif current_state == "play_game":
                current_state = self.game_loop()
            elif current_state == "high_score":
                current_state = self.show_high_score()
            else:
                current_state = "quit"
        
        pygame.quit()

if __name__ == "__main__":
    game = SnakeGame()
    game.run() 