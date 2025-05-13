# programme fait par Marc-Aurèle Béland
# groupe 406
# TP6 - roche, papier, ciseaux

import arcade
import random
from game_state import GameState

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "roche, papier , ciseaux"


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        arcade.set_background_color(arcade.color.TURQUOISE)
        self.rock = None
        self.paper = None
        self.scissors = None
        self.button_list = None
        self.player_position = SCREEN_WIDTH / 3
        self.bot_position = SCREEN_WIDTH / 3 * 2+70
        self.player_attack_chosen = False
        self.texte = ""
        self.winner = ""
        self.score_player = 0
        self.score_cpu = 0
        self.cpu = 0
        self.cpu_choice = None

        self.state = GameState.NOT_STARTED
        self.pick = None
        self.cpu_choice_icon = None
        self.cpu_choice_icon_list = None



    def setup(self):
        self.button_list = arcade.SpriteList()
        self.bot_list = arcade.SpriteList()
        self.rock = arcade.Sprite("assets/srock.png", 0.7, self.player_position - 80, SCREEN_HEIGHT / 2 - 150)
        self.paper = arcade.Sprite("assets/spaper.png",0.7, self.player_position, SCREEN_HEIGHT / 2 - 150)
        self.scissors = arcade.Sprite("assets/scissors.png",0.7, self.player_position + 80, SCREEN_HEIGHT / 2 - 150)
        self.bot = arcade.Sprite("assets/compy.png", 1, self.bot_position, SCREEN_HEIGHT / 2 - 50)
        self.player_position = arcade.Sprite("assets/faceBeard.png", 0.5, self.player_position)
        self.button_list.append(self.rock)
        self.button_list.append(self.paper)
        self.button_list.append(self.scissors)
        self.bot_list.append(self.bot)
        self.cpu_choice_icon = arcade.Sprite("assets/srock.png", 0.7, self.bot_position, SCREEN_HEIGHT / 2 - 150)
        self.cpu_choice_icon_list = arcade.SpriteList()
        self.cpu_choice_icon_list.append(self.cpu_choice_icon)
        self.cpu_choice = None

    def on_draw(self):
        self.clear()
        if self.state == GameState.ROUND_ACTIVE:
            arcade.draw_text('Roche, papier, ciseau', 201, 500,arcade.color.RED,40)
            arcade.draw_text('Roche, papier, ciseau', 200, 498, arcade.color.WHITE, 40)
            arcade.draw_text("Appuyer sur une image pour faire une attaque!",25, 470,arcade.color.WHITE,30)
            arcade.draw_text("Le pointage du joueur est", 150, 40,arcade.color.WHITE,12)
            arcade.draw_text("Le pointage de l'ordinateur est",500, 40,arcade.color.WHITE,12)
            self.button_list.draw()
            self.bot_list.draw()
        elif self.state == GameState.NOT_STARTED:
            arcade.draw_text('Roche, papier, ciseau', 200, 500,arcade.color.RED,40)
            arcade.draw_text("Appuyer sur une touche pour commencer", 150, 400,arcade.color.RED, 25)
        elif self.state == GameState.ROUND_DONE:
            arcade.draw_text('Roche, papier, ciseau', 201, 500, arcade.color.RED, 40)
            arcade.draw_text('Roche, papier, ciseau', 200, 498, arcade.color.WHITE, 40)
            arcade.draw_text("Appuyer sur espace pour continuer", 25, 470, arcade.color.WHITE, 30)
            arcade.draw_text("Le pointage du joueur est", 150, 40, arcade.color.WHITE, 12)
            arcade.draw_text("Le pointage de l'ordinateur est", 500, 40, arcade.color.WHITE, 12)
            self.button_list.draw()
            self.bot_list.draw()
            self.cpu_choice_icon_list.draw()





    def on_update(self, delta_time):
      #  self.rock = arcade.Sprite("assets/srock-attack.png", 0.5, self.player_position - 80, SCREEN_HEIGHT / 2 - 50)
        if self.pick != None and self.cpu_choice == None:
            self.cpu_choice = random.choice(("ROCK","PAPER","SCISSORS"))
            self.cpu_choice_icon.texture = arcade.load_texture(get_image_path(self.cpu_choice))
            self.state = GameState.ROUND_DONE




    def on_key_press(self, key, key_modifiers):
        if self.state == GameState.NOT_STARTED:
            self.state = GameState.ROUND_ACTIVE

    def on_mouse_press(self, x, y, button, key_modifiers):
        if self.state == GameState.ROUND_ACTIVE:
            if self.rock.collides_with_point((x, y)):
                self.pick = "ROCK"

        if self.state == GameState.ROUND_ACTIVE:
            if self.paper.collides_with_point((x, y)):
                self.pick = "PAPER"

        if self.state == GameState.ROUND_ACTIVE:
            if self.scissors.collides_with_point((x, y)):
                self.pick = "SCISSORS"

def get_image_path(pick):
    if pick == "ROCK":
        return "assets/srock.png"
    elif pick == "PAPER":
        return "assets/spaper.png"
    elif pick == "SCISSORS":
        return "assets/scissors.png"


def main():
    """ Main method """
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()
    arcade.start_render()


if __name__ == "__main__":
    main()
