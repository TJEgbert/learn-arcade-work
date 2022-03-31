import arcade

# Variables
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 9")

        self.wall_list = None
        self.player_sprite_list = None
        self.collection_spite_list = None

    def setup(self):

        arcade.set_background_color(arcade.color.BLUE)

        self.wall_list = arcade.sprite_list
        self.player_sprite_list = arcade.sprite_list
        self.collection_spite_list = arcade.sprite_list

    def on_draw(self):

        arcade.start_render()


def main():
    window = MyGame
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()