import sys
from time import sleep
import pygame
import pygame.mixer
import random

from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from bullet import Bullet
from alien import Alien

class Star(pygame.sprite.Sprite):
    """Represents a single star in the background."""

    def __init__(self, game):
        """Initialize the star and set its position."""
        super().__init__()
        self.screen = game.screen
        self.color = (255, 255, 255)
        self.rect = pygame.Rect(0, 0, 2, 2)
        self.rect.x = random.randint(0, game.settings.screen_width)
        self.rect.y = random.randint(0, game.settings.screen_height)

    def draw_star(self):
        """Draw the star on the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game and create game resources."""
        pygame.init()
        pygame.mixer.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_width()
        self.settings.screen_height = self.screen.get_height()
        pygame.display.set_caption("Alien Invasion")

        # Create an instance to store game statistics
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)

        # Start the game in an inactive state
        self.game_active = False
        self.difficulty_selected = False  # State to check if difficulty has been selected

        # Create difficulty buttons (perfectly centered)
        button_width, button_height = 200, 50
        spacing = 20  # Spacing between buttons

        # Calculate button positions
        total_height = (3 * button_height) + (2 * spacing)  # Total height of buttons + spacing
        start_y = (self.settings.screen_height - total_height) // 2  # Starting Y position

        self.easy_button = Button(self, "Easy", (self.settings.screen_width // 2, start_y))
        self.medium_button = Button(self, "Medium", (self.settings.screen_width // 2, start_y + button_height + spacing))
        self.hard_button = Button(self, "Hard", (self.settings.screen_width // 2, start_y + 2 * (button_height + spacing)))

        # Play button (initially hidden, centered)
        self.play_button = Button(self, "Play", (self.settings.screen_width // 2, self.settings.screen_height // 2))

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self.stars = pygame.sprite.Group()
        self._create_star_field()
        self._create_fleet()

    def run_game(self):
        """Start the main loop for the game."""
        music_path = r"C:\Users\Luiz Gustavo\Desktop\alien_invasion\sounds\Hans Zimmer - Interstellar (Space Sounds).mp3"
    
        pygame.mixer.music.load(music_path)  
        pygame.mixer.music.set_volume(0.5)  # Ajuste o volume (0.0 a 1.0)
        pygame.mixer.music.play(-1)  # "-1" faz a música tocar infinitamente
        while True:
            self._check_events()

            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if not self.difficulty_selected:
                    self._check_difficulty_buttons(mouse_pos)
                elif self.difficulty_selected and not self.game_active:
                    self._check_play_button(mouse_pos)

    def _check_difficulty_buttons(self, mouse_pos):
        """Set the difficulty based on the clicked button."""
        if self.easy_button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings(difficulty='easy')
            self.difficulty_selected = True
        elif self.medium_button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings(difficulty='medium')
            self.difficulty_selected = True
        elif self.hard_button.rect.collidepoint(mouse_pos):
            self.settings.initialize_dynamic_settings(difficulty='hard')
            self.difficulty_selected = True

    def _check_play_button(self, mouse_pos):
        """Start the game when the Play button is clicked."""
        if self.play_button.rect.collidepoint(mouse_pos):
            self._start_game()

            # Load the high score when the game starts
            self.stats.load_high_score()

            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()

    def _start_game(self):
        """Start the game with the selected settings."""
        self.stats.reset_stats()
        self.game_active = True

        # Reset the points per alien to the initial value (50)
        self.settings.alien_points = 50

        # Clear any remaining bullets and aliens
        self.bullets.empty()
        self.aliens.empty()

        # Create a new fleet and center the ship
        self._create_fleet()
        self.ship.center_ship()

        pygame.mouse.set_visible(False)

    def _check_keydown_events(self, event):
        """Respond to key presses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _create_star_field(self):
        """Create a field of stars in the background."""
        for _ in range(280):
            star = Star(self)
            self.stars.add(star)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width
            current_x = alien_width
            current_y += 2 * alien_height

    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the fleet."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Check if the fleet reaches the screen edges."""
        for alien in self.aliens.sprites():
            if alien.rect.right >= self.settings.screen_width or alien.rect.left <= 0:
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Move the fleet down and change its direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullet group."""
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """Update bullet positions and handle collisions."""
        self.bullets.update()
        self._remove_old_bullets()
        self._check_bullet_alien_collisions()

    def _remove_old_bullets(self):
        """Remove bullets that have gone off the screen."""
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _check_bullet_alien_collisions(self):
        """Handle collisions between bullets and aliens."""
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            # Increment the score for each alien destroyed
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()

        if not self.aliens:
            # Destroy existing bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()

            # Increase the game speed
            self.settings.increase_speed()

            # Increase the points per alien by 5
            self.settings.alien_points += 5
            print(f"Points per alien increased to: {self.settings.alien_points}")

            # Increase the level
            self.stats.level += 1
            self.sb.prep_level()

            # Update the scoreboard
            self.sb.prep_score()

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left and update the scoreboard
            self.stats.ships_left -= 1
            self.sb.prep_ships()

            # Clear any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()

            # Pause briefly to let the player recover
            sleep(0.5)
        else:
            # Save the high score when the game ends
            self.stats.save_high_score()

            self.game_active = False
            self.difficulty_selected = False  # Reset difficulty selection

            # Reset the points per alien to the initial value (50)
            self.settings.alien_points = 50

            pygame.mouse.set_visible(True)  # Show the mouse cursor

    def _check_aliens_bottom(self):
        """Check if any aliens have reached the bottom of the screen."""
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                # Treat this as if the ship was hit
                self._ship_hit()
                break

    def _update_aliens(self):
        """Update the position of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        # Detect collisions between aliens and the ship
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # Check for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _update_screen(self):
        """Update images on the screen and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        for star in self.stars.sprites():
            star.draw_star()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)

        # Draw the score information
        self.sb.show_score()

        # Draw the difficulty buttons if difficulty has not been selected
        if not self.difficulty_selected:
            self.easy_button.draw_button()
            self.medium_button.draw_button()
            self.hard_button.draw_button()
        # Draw the Play button if difficulty has been selected but the game has not started
        elif self.difficulty_selected and not self.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()