#!/usr/bin/env python3
"""
Generate Placeholder Assets for Harvest & Hero
Creates simple but functional placeholder graphics for testing.
Replace with professional free assets from FREE_ASSET_SOURCES.md later!
"""

from PIL import Image, ImageDraw

def create_player_spritesheet():
    """Create a simple 64x64 player sprite sheet with 16 frames"""
    # Create 64x64 image
    img = Image.new('RGBA', (64, 64), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Colors
    blue = (65, 105, 225, 255)  # Player body
    skin = (255, 220, 177, 255)  # Face
    dark = (0, 0, 100, 255)      # Outline/eyes

    # Helper function to draw a simple character
    def draw_char(x, y, facing='down', frame=0):
        """Draw a simple stick figure character"""
        # Body (12x14 pixels, centered in 16x16)
        body_x = x + 2
        body_y = y + 2

        # Head (skin color circle)
        draw.ellipse([body_x+3, body_y, body_x+9, body_y+6], fill=skin, outline=dark)

        # Eyes (facing direction indicators)
        if facing == 'down':
            draw.point((body_x+4, body_y+3), fill=dark)
            draw.point((body_x+7, body_y+3), fill=dark)
        elif facing == 'up':
            # Back of head, no eyes
            pass
        elif facing == 'left':
            draw.point((body_x+4, body_y+3), fill=dark)
        elif facing == 'right':
            draw.point((body_x+7, body_y+3), fill=dark)

        # Body (blue rectangle)
        draw.rectangle([body_x+2, body_y+6, body_x+9, body_y+11], fill=blue, outline=dark)

        # Legs (offset based on walk frame)
        leg_offset = 0
        if frame == 1:
            leg_offset = -1
        elif frame == 3:
            leg_offset = 1

        draw.rectangle([body_x+3, body_y+11, body_x+5, body_y+14], fill=blue, outline=dark)
        draw.rectangle([body_x+6+leg_offset, body_y+11, body_x+8+leg_offset, body_y+14], fill=blue, outline=dark)

    # Row 0: Down animations
    draw_char(0, 0, 'down', 0)    # Idle
    draw_char(16, 0, 'down', 1)   # Walk 1
    draw_char(32, 0, 'down', 2)   # Walk 2
    draw_char(48, 0, 'down', 3)   # Walk 3

    # Row 1: Up animations
    draw_char(0, 16, 'up', 0)     # Idle
    draw_char(16, 16, 'up', 1)    # Walk 1
    draw_char(32, 16, 'up', 2)    # Walk 2
    draw_char(48, 16, 'up', 3)    # Walk 3

    # Row 2: Left animations
    draw_char(0, 32, 'left', 0)   # Idle
    draw_char(16, 32, 'left', 1)  # Walk 1
    draw_char(32, 32, 'left', 2)  # Walk 2
    draw_char(48, 32, 'left', 3)  # Walk 3

    # Row 3: Right animations
    draw_char(0, 48, 'right', 0)  # Idle
    draw_char(16, 48, 'right', 1) # Walk 1
    draw_char(32, 48, 'right', 2) # Walk 2
    draw_char(48, 48, 'right', 3) # Walk 3

    return img

def create_tileset():
    """Create a simple 256x256 tileset with basic terrain"""
    img = Image.new('RGBA', (256, 256), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Define colors for different terrain types
    colors = {
        'grass': (50, 200, 50, 255),
        'grass_dark': (40, 160, 40, 255),
        'dirt': (139, 90, 43, 255),
        'dirt_light': (180, 120, 70, 255),
        'water': (65, 105, 225, 255),
        'water_light': (100, 149, 237, 255),
        'wall': (100, 100, 100, 255),
        'wall_dark': (70, 70, 70, 255),
        'tree_leaves': (34, 139, 34, 255),
        'tree_trunk': (101, 67, 33, 255),
        'rock': (128, 128, 128, 255),
    }

    def draw_tile(tile_x, tile_y, tile_type):
        """Draw a 16x16 tile at grid position"""
        x = tile_x * 16
        y = tile_y * 16

        if tile_type == 'grass':
            # Grass with slight variation
            draw.rectangle([x, y, x+15, y+15], fill=colors['grass'])
            draw.point((x+3, y+5), fill=colors['grass_dark'])
            draw.point((x+10, y+8), fill=colors['grass_dark'])

        elif tile_type == 'dirt':
            draw.rectangle([x, y, x+15, y+15], fill=colors['dirt'])
            draw.point((x+4, y+6), fill=colors['dirt_light'])

        elif tile_type == 'water':
            draw.rectangle([x, y, x+15, y+15], fill=colors['water'])
            draw.line([x+2, y+5, x+8, y+5], fill=colors['water_light'])

        elif tile_type == 'wall':
            draw.rectangle([x, y, x+15, y+15], fill=colors['wall'])
            draw.rectangle([x, y, x+15, y+3], fill=colors['wall_dark'])

        elif tile_type == 'tree_top_left':
            draw.ellipse([x, y, x+15, y+15], fill=colors['tree_leaves'])
        elif tile_type == 'tree_top_right':
            draw.ellipse([x, y, x+15, y+15], fill=colors['tree_leaves'])
        elif tile_type == 'tree_bottom_left':
            draw.rectangle([x+6, y, x+9, y+15], fill=colors['tree_trunk'])
        elif tile_type == 'tree_bottom_right':
            draw.rectangle([x+6, y, x+9, y+15], fill=colors['tree_trunk'])

        elif tile_type == 'rock':
            draw.ellipse([x+3, y+4, x+12, y+12], fill=colors['rock'])

    # Row 0-1: Grass tiles (0-15)
    for i in range(8):
        draw_tile(i, 0, 'grass')
    for i in range(8):
        draw_tile(i, 1, 'grass')

    # Row 2: Dirt tiles (16-31)
    for i in range(8):
        draw_tile(i, 2, 'dirt')
    for i in range(8):
        draw_tile(i, 3, 'dirt')

    # Row 4: Water tiles (32-47)
    for i in range(8):
        draw_tile(i, 4, 'water')
    for i in range(8):
        draw_tile(i, 5, 'water')

    # Row 6-7: Wall tiles (48-63)
    for i in range(8):
        draw_tile(i, 6, 'wall')
    for i in range(8):
        draw_tile(i, 7, 'wall')

    # Row 8: Tree (64-67) and Rock (72-75)
    draw_tile(0, 8, 'tree_top_left')
    draw_tile(1, 8, 'tree_top_right')
    draw_tile(2, 8, 'tree_bottom_left')
    draw_tile(3, 8, 'tree_bottom_right')
    draw_tile(8, 8, 'rock')
    draw_tile(9, 8, 'rock')

    return img

def main():
    print("Generating placeholder assets...")

    # Create player sprite sheet
    print("Creating player sprite sheet...")
    player_img = create_player_spritesheet()
    player_img.save('../game/assets/sprites/player/player_spritesheet.png')
    print("✓ player_spritesheet.png created")

    # Create tileset
    print("Creating tileset...")
    tileset_img = create_tileset()
    tileset_img.save('../game/assets/tilesets/main_tileset.png')
    print("✓ main_tileset.png created")

    print("\n✅ Placeholder assets generated successfully!")
    print("\nThese are simple placeholders. Replace with professional free assets from:")
    print("docs/FREE_ASSET_SOURCES.md")
    print("\nNext: Open the Godot project and the assets will be auto-imported!")

if __name__ == '__main__':
    try:
        main()
    except ImportError:
        print("ERROR: PIL (Pillow) not installed.")
        print("Install with: pip install Pillow")
        print("Then run this script again.")
