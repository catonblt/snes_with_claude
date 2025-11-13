# Phase 1: Foundation - Build Instructions

**Project:** Harvest & Hero
**Engine:** Godot 4.2+
**Target:** Playable foundation build with movement and collision

---

## Overview

This document guides you through completing Phase 1 by creating assets and configuring the Godot project.

**Time Estimate:** 6-12 hours (depending on experience level)

---

## Prerequisites

### Software Required
1. **Godot 4.2+** (free) - https://godotengine.org/download
2. **Pixel Art Editor** (choose one):
   - Aseprite ($20) - https://www.aseprite.org/
   - Libresprite (free) - https://libresprite.github.io/
   - Piskel (free, web) - https://www.piskelapp.com/
3. **Optional:**
   - Tiled Map Editor (free) - https://www.mapeditor.org/

### Skills Needed
- Basic pixel art (or willingness to learn)
- Basic Godot knowledge (or follow tutorials)
- Patience and attention to detail

---

## Phase 1 Checklist

- [ ] 1. Set up Godot project
- [ ] 2. Create player sprite sheet
- [ ] 3. Create tileset
- [ ] 4. Configure player in Godot
- [ ] 5. Create test map
- [ ] 6. Test and validate
- [ ] 7. Build executable (optional)

---

## Step 1: Set Up Godot Project (30 min)

### 1.1 Install Godot
1. Download Godot 4.2+ from official website
2. Extract (no installation needed)
3. Run Godot executable

### 1.2 Import Project
1. Launch Godot
2. Click "Import"
3. Navigate to `/game/project.godot`
4. Click "Import & Edit"

### 1.3 Verify Project Settings
1. Go to Project → Project Settings
2. Check Display settings:
   - Window size: 320×180 viewport
   - Stretch Mode: viewport
   - Stretch Aspect: keep
   - Stretch Scale Mode: integer
3. Check Rendering settings:
   - Textures → Canvas Textures → Default Texture Filter: **Nearest**
   - 2D → Snapping → Use GPU Pixel Snap: **On**

✅ **Checkpoint:** Project opens without errors

---

## Step 2: Create Player Sprite Sheet (2-4 hours)

### 2.1 Read Specification
- Open `/assets/sprites/player/PLAYER_SPRITE_SPEC.md`
- Review all requirements

### 2.2 Create Sprite Sheet
**Option A: Quick Placeholder**
1. Create simple 16×16 colored squares
2. Use different colors for directions (testing only)
3. Skip to Step 2.3

**Option B: Proper Pixel Art** (recommended)
1. Open your pixel art editor
2. Create new file: 64×64 pixels, indexed color
3. Set up 16×16 grid
4. Follow the specification to draw:
   - idle_down (frame 0,0)
   - idle_up (frame 0,1)
   - idle_left (frame 0,2)
   - idle_right (frame 0,3)
   - walk_down frames (1,0), (2,0), (3,0)
   - walk_up frames (1,1), (2,1), (3,1)
   - walk_left frames (1,2), (2,2), (3,2)
   - walk_right frames (1,3), (2,3), (3,3)

### 2.3 Export Sprite Sheet
1. Export as PNG
2. Enable transparency
3. No padding or margins
4. Save as: `/game/assets/sprites/player/player_spritesheet.png`

### 2.4 Import into Godot
1. Godot will auto-import the PNG
2. Select the file in FileSystem panel
3. In Import tab (top):
   - Filter: **Nearest** (NOT Linear!)
   - Mipmaps: Off
   - Repeat: Disabled
4. Click "Reimport"
5. Verify sprite looks sharp (not blurry)

### 2.5 Create SpriteFrames Resource
1. In FileSystem, right-click `assets/sprites/player/`
2. Create → Resource → SpriteFrames
3. Save as `player_animations.tres`
4. Double-click to open
5. Create animations:
   - **idle_down:** Add frame (0,0) from sprite sheet
   - **idle_up:** Add frame (0,1)
   - **idle_left:** Add frame (0,2)
   - **idle_right:** Add frame (0,3)
   - **walk_down:** Add frames (1,0), (2,0), (3,0), set FPS to 7
   - **walk_up:** Add frames (1,1), (2,1), (3,1), set FPS to 7
   - **walk_left:** Add frames (1,2), (2,2), (3,2), set FPS to 7
   - **walk_right:** Add frames (1,3), (2,3), (3,3), set FPS to 7

✅ **Checkpoint:** Player animations preview correctly in SpriteFrames editor

---

## Step 3: Create Tileset (3-5 hours)

### 3.1 Read Specification
- Open `/assets/tilesets/TILESET_SPEC.md`
- Review tile requirements

### 3.2 Create Tileset Image
**Option A: Quick Placeholder**
1. Create 256×256 image
2. Fill with simple colored 16×16 squares:
   - Green = grass (walkable)
   - Brown = dirt (walkable)
   - Blue = water
   - Gray = wall (collision)
   - Dark green = tree (collision)
3. Skip to Step 3.3

**Option B: Proper Tileset** (recommended)
1. Open pixel art editor
2. Create 256×256 pixel image
3. Set up 16×16 grid
4. Draw tiles following specification:
   - Grass tiles (variations)
   - Dirt/path tiles
   - Water tiles
   - Wall/cliff tiles
   - Tree tiles (2×2 = 4 tiles)
   - Rock tiles
5. Focus on tiles 0-79 for Phase 1

### 3.3 Export Tileset
1. Export as PNG
2. Transparency where needed
3. Save as: `/game/assets/tilesets/main_tileset.png`

### 3.4 Create TileSet Resource
1. In FileSystem, right-click `assets/tilesets/`
2. Create → Resource → TileSet
3. Save as `main_tileset.tres`
4. Double-click to open TileSet editor

### 3.5 Configure TileSet
1. In TileSet editor (bottom panel):
2. Click "Add Texture(s)" (or drag PNG)
3. Select `main_tileset.png`
4. Set Texture Region Size: 16×16
5. Click "Create" or use auto-slicing
6. Godot creates tiles automatically from grid

### 3.6 Set Up Collision Shapes
1. Select Physics tab in TileSet editor
2. Click "Add Physics Layer"
3. For each solid tile (walls, trees, rocks):
   - Select the tile
   - Click "Create Physics Polygon"
   - Draw collision shape (usually full 16×16 square)
   - Can use Rectangle tool for quick squares

**Tiles that need collision:**
- Walls/cliffs
- Trees (all 4 tiles of 2×2 tree)
- Rocks
- Any obstacle

**Tiles that should NOT have collision:**
- Grass
- Dirt/paths
- Small decorations
- (Water - decide based on design)

✅ **Checkpoint:** Tileset configured with collision shapes

---

## Step 4: Configure Player Scene (30 min)

### 4.1 Open Player Scene
1. Navigate to `scenes/player/player.tscn`
2. Double-click to open

### 4.2 Set SpriteFrames Resource
1. Select "AnimatedSprite2D" node
2. In Inspector, find "Sprite Frames" property
3. Drag `player_animations.tres` into this field
4. Set "Animation" to "idle_down"
5. Play animation to test

### 4.3 Verify Collision Shape
1. Select "CollisionShape2D" node
2. Should have RectangleShape2D
3. Size should be about 12×8 (smaller than 16×16 visual sprite)
4. Position slightly below center (feet position)

### 4.4 Test Player Script
1. Select root "Player" node
2. Verify script is attached: `player.gd`
3. Open script, review code
4. No changes needed for Phase 1

✅ **Checkpoint:** Player scene configured

---

## Step 5: Create Test Map (1-2 hours)

### 5.1 Open World Scene
1. Navigate to `scenes/world/world.tscn`
2. Double-click to open

### 5.2 Set TileSet Resource
1. Select "Ground" TileMapLayer node
2. In Inspector, find "Tile Set" property
3. Drag `main_tileset.tres` into this field
4. Repeat for "Collision" TileMapLayer

### 5.3 Paint Ground Layer
1. Select "Ground" TileMapLayer
2. In TileMap editor (bottom), select grass tile
3. Paint a 32×32 area of grass
4. Add dirt paths using path tiles
5. Add water in corner or edge
6. Add visual details (flowers, rocks)

### 5.4 Paint Collision Layer
1. Select "Collision" TileMapLayer
2. Paint walls around perimeter (create boundaries)
3. Add trees as obstacles (use all 4 tiles for 2×2 tree)
4. Add rocks scattered around
5. Create interesting layout (not too cluttered)

**Map Design Tips:**
- Leave open spaces for movement testing
- Create narrow corridors (1-2 tiles wide) for collision testing
- Add corners for corner-sliding testing
- Make it interesting but not overwhelming

### 5.5 Verify Player Start Position
1. Select "Player" node (child of World)
2. Set position to center of open area
3. Ensure player doesn't start inside a wall!

✅ **Checkpoint:** Test map created, player has space to move

---

## Step 6: Test in Godot (30-60 min)

### 6.1 Initial Launch
1. Press F5 or click Play button (▶)
2. Game should launch
3. You should see:
   - Test map rendered
   - Player character in starting position
   - Smooth graphics (not blurry)

### 6.2 Movement Testing
1. Press WASD to move
2. Verify 8-directional movement works
3. Check all directions feel responsive
4. Verify animations change with direction

### 6.3 Collision Testing
1. Walk into walls - should stop
2. Walk into trees - should stop
3. Try corners - should slide smoothly
4. Walk on grass/paths - should move freely

### 6.4 Camera Testing
1. Move player around
2. Camera should follow smoothly
3. No jittering or jumping

### 6.5 Visual Testing
1. Tiles should be sharp and clear
2. No gaps or seams
3. Player sprite should be sharp
4. Animations smooth

### 6.6 Performance Testing
1. Game should run at 60 FPS
2. No stuttering or lag
3. Smooth throughout

✅ **Checkpoint:** Basic movement works, collisions work

---

## Step 7: Build Executable (Optional, 30 min)

### 7.1 Configure Export
1. Go to Project → Export
2. Click "Add..." and select your platform:
   - Windows Desktop
   - Linux/X11
   - macOS
3. Download export templates if prompted

### 7.2 Export Settings
1. Name: "Harvest & Hero - Phase 1"
2. Runnable: Checked
3. Export path: Choose location

### 7.3 Export
1. Click "Export Project"
2. Choose filename: `HarvestHero_Phase1.exe` (or .x86_64 for Linux)
3. Save

### 7.4 Test Build
1. Navigate to export location
2. Run executable
3. Verify game works outside Godot

✅ **Checkpoint:** Game builds and runs as standalone

---

## Troubleshooting

### Sprites Look Blurry
- Check import settings: Filter must be "Nearest"
- Check project settings: Canvas Textures filter = 0 (Nearest)
- Reimport all images

### Player Won't Move
- Check that player script is attached
- Verify input actions in Project Settings
- Check console for errors (F4 or Output panel)

### Collision Not Working
- Verify TileSet has Physics Layer
- Check that solid tiles have collision shapes
- Verify TileMapLayer has collision enabled
- Check collision layer/mask settings

### Animation Not Playing
- Verify SpriteFrames resource is assigned
- Check that animations exist with correct names
- Verify animation names match code:
  - idle_down, idle_up, idle_left, idle_right
  - walk_down, walk_up, walk_left, walk_right

### Game Crashes on Launch
- Check Output panel for errors
- Verify all resource paths are correct
- Ensure TileSet and SpriteFrames resources exist
- Try running in Debug mode (F6)

---

## Phase 1 Complete Checklist

- [ ] Godot project opens without errors
- [ ] Player sprite sheet created and imported
- [ ] Player animations configured (8 total)
- [ ] Tileset created and imported
- [ ] TileSet resource configured with collision
- [ ] Test map created (32×32 tiles minimum)
- [ ] Player moves in all 8 directions
- [ ] Animations play correctly
- [ ] Collision works (can't walk through walls)
- [ ] Camera follows player smoothly
- [ ] Game runs at 60 FPS
- [ ] All tests in PHASE_1_TESTING_GUIDE.md pass

---

## Next Steps

Once Phase 1 is complete and tested:
1. Review test results
2. Fix any critical bugs
3. Document completion
4. Begin Phase 2 planning:
   - Combat system
   - Farming system
   - NPC interactions

---

## Time Estimates Summary

- Godot setup: 30 min
- Player sprites: 2-4 hours
- Tileset: 3-5 hours
- Godot configuration: 1 hour
- Map creation: 1-2 hours
- Testing: 1 hour
- Building: 30 min (optional)

**Total: 8-14 hours** (varies by experience)

---

## Getting Help

### Resources
- Godot Docs: https://docs.godotengine.org/
- Pixel Art Tutorials: https://lospec.com/articles
- Godot Discord: https://discord.gg/godot
- This Project: Review agent specifications in `/agents/` directory

### Common Issues
- Refer to agent documentation for detailed specs
- Check Godot forums for specific errors
- Review example projects (Godot demos)

---

**Good luck building Phase 1!** 🎮

Remember: Start simple, test frequently, iterate and improve.
