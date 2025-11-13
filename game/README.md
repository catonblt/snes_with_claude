# Harvest & Hero - Game Project

**A Zelda-inspired action-RPG meets Stardew Valley farming simulation**

---

## Quick Start

### Prerequisites
1. Install [Godot 4.2+](https://godotengine.org/download)
2. Have pixel art software ready (Aseprite, Libresprite, or Piskel)

### Opening Project
1. Launch Godot
2. Click "Import"
3. Select `project.godot` from this directory
4. Click "Import & Edit"

---

## Project Status

**Phase:** 1 - Foundation
**Status:** Code Complete - Assets Pending

✅ **Complete:**
- Core engine scripts
- Movement system
- Collision detection
- Scene structure
- Animation system

⏳ **Pending:**
- Player sprite sheet creation
- Tileset creation
- Godot resource configuration
- Test map building

**Next Steps:** Follow `/docs/BUILD_INSTRUCTIONS.md`

---

## Project Structure

```
game/
├── project.godot          # Godot project configuration
├── scenes/                # Game scenes
│   ├── player/           # Player character scene
│   ├── world/            # Main world scene
│   └── ui/               # UI scenes (future)
├── scripts/              # GDScript code
│   ├── player/           # Player movement & logic
│   ├── systems/          # Game systems (future)
│   └── autoload/         # Global singletons
└── assets/               # Game assets
    ├── sprites/          # Character & entity sprites
    ├── tilesets/         # Environment tiles
    ├── audio/            # Music & SFX (future)
    └── fonts/            # UI fonts (future)
```

---

## Controls (Phase 1)

- **WASD** or **Arrow Keys**: Move player
- **Shift**: Run (if implemented)
- **ESC**: Pause (future)

---

## Development Guide

### Creating Assets
1. **Player Sprites:** Follow `/assets/sprites/player/PLAYER_SPRITE_SPEC.md`
2. **Tilesets:** Follow `/assets/tilesets/TILESET_SPEC.md`

### Building the Game
Follow step-by-step guide: `/docs/BUILD_INSTRUCTIONS.md`

### Testing
Run comprehensive tests: `/docs/PHASE_1_TESTING_GUIDE.md`

---

## Technical Specifications

**Engine:** Godot 4.2+
**Resolution:** 320×180 (scaled 4× to 1280×720)
**Art Style:** 16×16 pixel art (SNES aesthetic)
**Target FPS:** 60
**Platforms:** Windows, Linux, macOS

---

## Key Scripts

### `scripts/player/player.gd`
Player character controller
- 8-directional smooth movement
- Animation state machine
- Collision handling
- Camera following

### `scripts/autoload/global.gd`
Global game state
- Player data management
- Scene transitions
- Save/load (future)
- Settings

---

## Asset Requirements

### Phase 1 Assets Needed:

**Player Sprite Sheet:**
- Size: 64×64 pixels
- 16 frames total
- Animations: idle (4) + walk (12)
- Location: `assets/sprites/player/player_spritesheet.png`

**Main Tileset:**
- Size: 256×256 pixels
- ~50-60 tiles minimum
- Grass, dirt, water, walls, trees, rocks
- Location: `assets/tilesets/main_tileset.png`

---

## Testing

### Run in Editor
Press **F5** or click **Play** button

### Run Specific Scene
Open scene, press **F6**

### Debug Mode
Press **F4** to show output/errors

---

## Common Issues

### Blurry Graphics
- Check Project Settings → Rendering → Textures
- Default Texture Filter must be "Nearest" (0)
- Reimport all assets

### Player Won't Move
- Check Output (F4) for script errors
- Verify player script is attached
- Check Input Map in Project Settings

### Collision Not Working
- Verify TileSet has Physics Layer configured
- Check collision shapes are created for solid tiles
- Verify collision layer/mask bits

---

## Next Phases

### Phase 2: Core Systems (Future)
- Combat system (sword, bow, enemies)
- Farming system (crops, tools, seasons)
- NPC interactions (dialogue, quests)

### Phase 3: Content (Future)
- Multiple dungeons
- Town with NPCs
- Quests and events
- Items and equipment

### Phase 4: Polish (Future)
- Music and sound effects
- Visual effects
- Balancing
- Bug fixes

---

## Resources

- **Project Docs:** See `/docs/` in parent directory
- **Agent Specs:** See `/agents/` for detailed requirements
- **Godot Docs:** https://docs.godotengine.org/
- **Pixel Art Guide:** https://lospec.com/

---

## Version History

**v0.1.0-alpha** (Phase 1 - Foundation)
- Core movement system
- Basic collision
- Scene structure
- Documentation complete

---

**Ready to build!** Follow BUILD_INSTRUCTIONS.md to complete Phase 1. 🎮
