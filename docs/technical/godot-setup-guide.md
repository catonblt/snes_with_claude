# Godot 4 Setup Guide for Pixel Art Game

**Engine:** Godot 4.2+ (Free, Open Source)
**Style:** Retro pixel art (Stardew Valley aesthetic)
**Platform:** Windows, Linux, macOS

---

## Installation

### Download Godot 4.2+
1. Go to https://godotengine.org/download
2. Download Godot 4.2 (Standard version)
3. Extract and run (no installation needed)

**Cost: $0**

---

## Project Configuration for Pixel Art

### Step 1: Project Settings

**Display Settings:**
- Window Width: 1280
- Window Height: 720
- Base Resolution: 320x180 (scales 4x)
- Stretch Mode: `viewport`
- Stretch Aspect: `keep`
- Stretch Scale Mode: `integer` (keeps pixels sharp)

**Rendering Settings:**
- Rendering > Textures > Canvas Textures > Default Texture Filter: **Nearest**
- Rendering > 2D > Snapping > Use GPU Pixel Snap: **On**

### Step 2: Import Settings

For all pixel art sprites and tilesets:
- Filter: **Nearest**
- Mipmaps: **Off**
- Repeat: **Disabled** (or **Enabled** for tiling)

---

## Recommended Project Structure

```
project/
├── scenes/
│   ├── world/
│   │   ├── world.tscn           # Main game world
│   │   └── test_map.tscn        # Test area
│   ├── player/
│   │   └── player.tscn          # Player character
│   └── ui/
│       └── hud.tscn             # HUD overlay
├── scripts/
│   ├── player/
│   │   └── player.gd            # Player movement script
│   ├── systems/
│   │   └── game_manager.gd      # Global game state
│   └── autoload/
│       └── global.gd            # Autoloaded singleton
├── assets/
│   ├── sprites/
│   │   ├── player/
│   │   └── environment/
│   ├── tilesets/
│   │   └── tileset.tres         # TileSet resource
│   ├── audio/
│   │   ├── music/
│   │   └── sfx/
│   └── fonts/
└── project.godot
```

---

## Key Godot 4 Systems for Our Game

### 1. TileMap System
- Used for world terrain
- Built-in physics layers for collision
- Multiple layers for backgrounds and foregrounds
- Physics Layer 0: Solid terrain
- Physics Layer 1: Player
- Physics Layer 2: Enemies

### 2. CharacterBody2D
- Player and NPC movement
- Built-in collision detection
- `move_and_slide()` for smooth movement

### 3. AnimatedSprite2D
- Character animations
- Easy frame-by-frame animation
- Supports sprite sheets

### 4. Camera2D
- Follows player smoothly
- Configurable smoothing
- Viewport boundaries

---

## Quick Start GDScript Primer

### Player Movement Example
```gdscript
extends CharacterBody2D

const SPEED = 100.0

func _physics_process(delta):
    var direction = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
    velocity = direction * SPEED
    move_and_slide()
```

### Input Actions (project.godot)
```
[input]
ui_up = { "keys": ["W", "Up"] }
ui_down = { "keys": ["S", "Down"] }
ui_left = { "keys": ["A", "Left"] }
ui_right = { "keys": ["D", "Right"] }
```

---

## Development Tools (All Free)

### Pixel Art
- **Aseprite** ($20) or **Libresprite** (free fork)
- **Piskel** (free, web-based)
- **GIMP** (free)

### Tilemap Editor
- **Tiled** (free, standalone) - Can export to Godot
- Godot's built-in tilemap editor (recommended)

### Audio
- **LMMS** (free) - Music composition
- **Audacity** (free) - Audio editing
- **Bfxr** (free) - SFX generation

---

## Performance Targets

- **FPS:** 60 (vsync on)
- **Resolution:** 320x180 base (scales to fullscreen)
- **Sprite Sizes:** 16x16 characters, 8x8 tiles
- **Max Entities:** 100+ on screen without lag

---

## Learning Resources

### Official Docs
- https://docs.godotengine.org/en/stable/
- TileMap Tutorial: https://docs.godotengine.org/en/stable/tutorials/2d/using_tilemaps.html

### Pixel Art Games
- GDQuest: https://www.gdquest.com/library/pixel_art_setup_godot4/
- Fungies.io Stardew Clone: https://fungies.io/how-to-make-a-stardew-valley-clone-in-godot/

### Video Tutorials
- HeartBeast RPG Series (Godot)
- Brackeys 2D Platformer (concepts transfer)

---

## Common Issues & Solutions

### Blurry Sprites
**Problem:** Sprites look blurry/fuzzy
**Solution:** Set texture filter to "Nearest" in import settings and project settings

### Jittery Camera
**Problem:** Camera doesn't follow smoothly
**Solution:** Enable camera smoothing, adjust smoothing speed

### Collision Not Working
**Problem:** Player walks through walls
**Solution:** Ensure TileMap has Physics Layer and collision shapes defined

### Poor Performance
**Problem:** FPS drops
**Solution:**
- Reduce entity count
- Use object pooling
- Optimize draw calls (fewer unique sprites per frame)

---

## Phase 1 Technical Checklist

For Foundation phase, ensure:
- [ ] Godot 4.2+ installed
- [ ] Project settings configured for pixel art
- [ ] TileMap system set up
- [ ] Player CharacterBody2D created
- [ ] Camera2D following player
- [ ] Input system configured
- [ ] Test scene created

**Estimated Setup Time:** 30-60 minutes for first-time setup

---

**Ready to build!** Start with creating the Godot project and basic player movement.
