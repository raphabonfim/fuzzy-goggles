import os
import sys
import random
import argparse

# Optionally run with dummy video driver when in headless mode
parser = argparse.ArgumentParser(description="Placeholder beat'em up prototype")
parser.add_argument("--headless", action="store_true", help="Run with dummy video driver for automated tests")
args = parser.parse_args()

if args.headless:
    os.environ["SDL_VIDEODRIVER"] = "dummy"

import pygame

# Screen dimensions
WIDTH, HEIGHT = 800, 450

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (66, 135, 245)
RED = (200, 40, 40)
ORANGE = (245, 130, 48)
PURPLE = (145, 61, 136)

class Entity:
    def __init__(self, x, y, w, h, color, speed, hp):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.speed = speed
        self.max_hp = hp
        self.hp = hp

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        # simple HP bar
        if self.max_hp > 1:
            ratio = self.hp / self.max_hp
            bar_width = int(self.rect.width * ratio)
            bar_rect = pygame.Rect(self.rect.x, self.rect.y - 6, bar_width, 4)
            pygame.draw.rect(surface, WHITE, bar_rect)

class Player(Entity):
    def __init__(self):
        super().__init__(WIDTH // 2, HEIGHT - 60, 40, 50, BLUE, 5, 20)
        self.attack_cooldown = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.clamp_ip(pygame.Rect(0, 0, WIDTH, HEIGHT))

    def attack(self, attack_type):
        if self.attack_cooldown > 0:
            return None
        self.attack_cooldown = 20
        # attack rect depending on type
        if attack_type == "light":
            w, h, dmg = 40, 20, 2
        elif attack_type == "heavy":
            w, h, dmg = 60, 30, 5
        else:  # grab
            w, h, dmg = 50, 50, 8
        attack_rect = pygame.Rect(self.rect.centerx - w // 2, self.rect.y - h, w, h)
        return attack_rect, dmg

    def update(self):
        if self.attack_cooldown > 0:
            self.attack_cooldown -= 1

class Enemy(Entity):
    def __init__(self, x, y, color, speed, hp):
        super().__init__(x, y, 40, 50, color, speed, hp)

    def update(self, player):
        if player.rect.x < self.rect.x:
            self.rect.x -= self.speed
        elif player.rect.x > self.rect.x:
            self.rect.x += self.speed
        if player.rect.y < self.rect.y:
            self.rect.y -= self.speed
        elif player.rect.y > self.rect.y:
            self.rect.y += self.speed

        if self.rect.colliderect(player.rect):
            player.hp -= 1

class Game:
    def __init__(self, headless=False):
        self.headless = headless
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Best Served Cold Prototype")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 28)
        self.loop = 1
        self.state = "hunt"
        self.player = Player()
        self.enemies = []
        self.message_timer = 0
        self.spawn_hunt()

    def spawn_hunt(self):
        self.enemies = []
        for _ in range(3 + self.loop):
            x = random.randint(50, WIDTH - 90)
            y = random.randint(50, HEIGHT - 100)
            speed = 2 + self.loop * 0.5
            hp = 5 + self.loop
            self.enemies.append(Enemy(x, y, RED, speed, hp))

    def spawn_miniboss(self):
        self.enemies = []
        speed = 2 + self.loop * 0.4
        hp = 15 + self.loop * 2
        self.enemies.append(Enemy(WIDTH // 2, HEIGHT // 3, ORANGE, speed, hp))

    def spawn_boss(self):
        self.enemies = []
        speed = 2 + self.loop * 0.5
        hp = 25 + self.loop * 3
        self.enemies.append(Enemy(WIDTH // 2, HEIGHT // 4, PURPLE, speed, hp))

    def update(self):
        self.player.handle_input()
        self.player.update()
        for enemy in list(self.enemies):
            enemy.update(self.player)
            if enemy.hp <= 0:
                self.enemies.remove(enemy)
        if self.player.hp <= 0:
            self.running = False

        # state transitions
        if not self.enemies:
            if self.state == "hunt":
                self.state = "confront"
                self.spawn_miniboss()
            elif self.state == "confront":
                self.state = "showdown"
                self.spawn_boss()
            elif self.state == "showdown":
                self.state = "twist"
                self.message_timer = 120  # two seconds
        elif self.state == "twist" and self.message_timer <= 0:
            self.loop += 1
            self.state = "hunt"
            self.player.hp = self.player.max_hp
            self.spawn_hunt()

        if self.state == "twist" and self.message_timer > 0:
            self.message_timer -= 1

    def draw(self):
        self.screen.fill(BLACK)
        self.player.draw(self.screen)
        for enemy in self.enemies:
            enemy.draw(self.screen)
        loop_text = self.font.render(f"Loop {self.loop} - {self.state}", True, WHITE)
        hp_text = self.font.render(f"HP: {self.player.hp}", True, WHITE)
        self.screen.blit(loop_text, (10, 10))
        self.screen.blit(hp_text, (10, 30))
        if self.state == "twist":
            msg = self.font.render("Roles flip!", True, WHITE)
            rect = msg.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            self.screen.blit(msg, rect)
        pygame.display.flip()

    def handle_attacks(self):
        keys = pygame.key.get_pressed()
        attack = None
        if keys[pygame.K_j]:
            attack = self.player.attack("light")
        elif keys[pygame.K_k]:
            attack = self.player.attack("heavy")
        elif keys[pygame.K_l]:
            attack = self.player.attack("grab")
        if attack:
            rect, dmg = attack
            for enemy in self.enemies:
                if rect.colliderect(enemy.rect):
                    enemy.hp -= dmg

    def run(self):
        self.running = True
        frame_limit = 300 if self.headless else None
        frames = 0
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.handle_attacks()
            self.update()
            self.draw()
            self.clock.tick(60)
            frames += 1
            if frame_limit and frames > frame_limit:
                self.running = False
        pygame.quit()

if __name__ == "__main__":
    game = Game(headless=args.headless)
    game.run()
