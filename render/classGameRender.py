import arcade
from engine import classEngine

class GameRender:

    def __init__(self):
        # Engine
        self.engine = None

        # Map sprite list
        self.map_sprites = None
        # Player Enemy and Upgrade sprite list
        self.ent_sprites = None

        # Map textures
        self.texture_wall = None
        self.texture_floor1 = None
        self.texture_floor2 = None
        self.texture_spike = None
        self.texture_hole = None

        # Ent textures
        self.texture_player_right = None
        self.texture_player_left = None
        self.texture_coin = None
        self.texture_upgrade_speed = None
        self.texture_upgrade_maxhealth = None
        self.texture_healthpack = None
        self.texture_enemy = None
        self.texture_sword = None

        # Texture Dicts
        self.bg_textures = None
        self.fg_textures = None

        # Generation

    def setup(self):
        self.engine = classEngine.Engine()
        self.engine.setup()

        self.texture_player_right = arcade.load_texture("res/images/knight_f_idle_anim_f1.png")
        self.texture_player_left = arcade.load_texture("res/images/knight_f_idle_anim_f1.png", mirrored=True)
        self.texture_coin = arcade.load_texture("res/images/coin_anim_f0.png")
        self.texture_upgrade_speed = arcade.load_texture("res/images/flask_big_blue.png")
        self.texture_upgrade_maxhealth = arcade.load_texture("res/images/flask_big_red.png")
        self.texture_healthpack = arcade.load_texture("res/images/ui_heart_full.png")
        self.texture_enemy = arcade.load_texture("res/images/imp_idle_anim_f1.png")
        self.texture_sword = arcade.load_texture("res/images/weapon_regular_sword.png", width=10, height=21)

        self.texture_hole = arcade.load_texture("res/images/hole.png", width=45, height=45)
        self.texture_spike = arcade.load_texture("res/images/floor_spikes_anim_f3.png", width=45, height=45)
        self.texture_wall = arcade.load_texture("res/images/wall_mid.png", width=45, height=45)
        self.texture_floor1 = arcade.load_texture("res/images/floor_1.png", width=45, height=45)
        self.texture_floor2 = arcade.load_texture("res/images/floor_3.png", width=45, height=45)

        self.bg_textures = [
            self.texture_wall,
            self.texture_floor1,
            self.texture_floor2,
            self.texture_hole,
            self.texture_spike
        ]

        self.fg_textures = [
            None,
            self.texture_coin,
            self.texture_healthpack,
            self.texture_upgrade_maxhealth,
            self.texture_upgrade_speed,
            None
        ]

    def draw(self):
        self.draw_bg()
        self.draw_fg()
        self.draw_player()
        self.draw_enemies()
        if self.engine.player.draw_sword:
            self.draw_sword()
        arcade.draw_text("DEBUG:GAME", 0, 0, arcade.color.WHITE)

    def update(self):
        self.engine.update()

    def keypress(self, key):
        self.engine.keypress(key)

    def draw_bg(self):
        for row in range(16):
            for col in range(16):
                arcade.draw_texture_rectangle(
                    row*45+22.5,
                    col*45+22.5,
                    45,
                    45,
                    self.bg_textures[self.engine.tile_data.floor_grid[15-row][15-col]]
                )

    def draw_fg(self):
        for row in range(16):
            for col in range(16):
                if self.engine.tile_data.surface_grid[row][col] not in [0,5]:
                    arcade.draw_texture_rectangle(
                        row*45+22.5,
                        col*45+22.5,
                        30,
                        30,
                        self.fg_textures[self.engine.tile_data.surface_grid[row][col]]
                    )

    def draw_player(self):
        if self.engine.player.face_right:
            texture = self.texture_player_right
        else:
            texture = self.texture_player_left
        arcade.draw_texture_rectangle(
            self.engine.player.row * 45 + 22.5,
            self.engine.player.col * 45 + 22.5,
            45,
            45,
            texture
        )

    def draw_enemies(self):
        for enemy in self.engine.enemy_list:
            arcade.draw_texture_rectangle(
                enemy.row * 45 + 22.5,
                enemy.col * 45 + 22.5,
                45,
                45,
                self.texture_enemy
            )

    def draw_sword(self):
        arcade.draw_texture_rectangle(
            (self.engine.player.row - 1 + (2 * self.engine.player.face_right)) * 45 + 22.5,
            self.engine.player.col * 45 + 22.5,
            10,
            21,
            self.texture_sword,
            (90 + (180 * self.engine.player.face_right))
        )

