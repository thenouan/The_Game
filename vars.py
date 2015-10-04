__author__ = 'Markus Peterson'

class Variables:
    # SCREEN
    # screen_width = 1080
    # screen_height = 720
    screen_width = 1000
    screen_height = 900


    # MAP
    world_map_width = 50
    world_map_height = 50
    world_map_block_size = 8
    world_map_octaves = 2
    world_map_gen_threshold = 3

    # MINIMAP
    minimap_width = 150
    minimap_height = 150
    minimap_block_size = 2

    # COLORS
    world_map_colors = {
         0: ( 10,  10,  10),
         1: ( 70,  70,  70),
         2: ( 80,  80,  80),
         3: ( 45,   0,   0),
         4: (100,   0, 100),
        11: (100, 100,  10),
        12: ( 10, 100, 100),
        13: (  0,  45,   0),
    }

    minimap_colors = {
         0: ( 25,  25,  25),
         1: ( 65,  65,  65),
         2: ( 75,  75,  75),
         3: ( 45,   0,   0),
         4: (100,   0, 100),
        11: ( 50, 100,   0),
        12: ( 10, 100, 100),
        13: (  0,  45,   0),
    }
