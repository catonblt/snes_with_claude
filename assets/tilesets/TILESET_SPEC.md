# Main Tileset Specification
## Phase 1: Foundation

**Artist:** Environment & Tileset Artist (Agent #05)
**Target Engine:** Godot 4.2
**File Format:** PNG tileset image
**Tile Size:** 16×16 pixels

---

## Specifications

### Tileset Dimensions
- **Single Tile:** 16×16 pixels
- **Tileset Grid:** 16 columns × 16 rows = 256 tiles
- **Total Image Size:** 256×256 pixels

### Phase 1 Tile Requirements (~50-60 tiles)

**Terrain Types:**
1. Grass (8-10 variations)
2. Dirt/Path (8-10 variations)
3. Water (4-6 tiles)
4. Walls/Cliffs (12-16 tiles)
5. Trees (4-6 tiles)
6. Rocks (3-4 tiles)
7. Flowers/Details (6-8 tiles)

---

## Color Palette (SNES-Style Nature)

```
Grass:
- Light: #9ACD32, #7CFC00
- Medium: #32CD32, #228B22
- Dark: #006400

Dirt/Path:
- Light: #D2B48C, #F4A460
- Medium: #CD853F, #8B4513
- Dark: #654321

Water:
- Light: #87CEEB, #4682B4
- Medium: #4169E1, #1E90FF
- Dark: #00008B

Stone/Cliff:
- Light: #D3D3D3, #C0C0C0
- Medium: #808080, #696969
- Dark: #2F4F4F, #000000 (outline)

Trees:
- Leaves: #228B22, #006400
- Trunk: #8B4513, #654321
```

---

## Tile Index Layout (First 64 tiles)

### Row 0-1: Grass Tiles (0-15)
```
0: Plain grass
1-3: Grass with small flowers (variation)
4-7: Grass edge transitions (N, S, E, W)
8-11: Grass corners (NW, NE, SW, SE)
12-15: Tall grass variants
```

### Row 2-3: Dirt/Path Tiles (16-31)
```
16: Plain dirt
17-19: Dirt path straight (horizontal, vertical, cross)
20-23: Path corners (4 directions)
24-27: Grass-to-dirt transitions
28-31: Path variations (stones, worn)
```

### Row 4: Water Tiles (32-47)
```
32-35: Water (animated, 4 frames)
36-39: Water edges (N, S, E, W)
40-43: Water corners
44-47: Shore/beach tiles
```

### Row 5-6: Walls/Cliffs (48-63)
```
48-51: Cliff top edge (N, S, E, W)
52-55: Cliff corners
56-59: Cliff face (height tiles)
60-63: Stone wall tiles
```

### Row 7: Trees & Objects (64-79)
```
64-67: Tree (4 tiles: top-left, top-right, bottom-left, bottom-right)
68-71: Bush/small tree
72-75: Rocks (small, medium, large, boulder)
76-79: Flowers, mushrooms, details
```

---

## Collision Configuration

### Godot TileSet Physics Layers

**Layer 0: Solid Terrain**
- Walls, cliffs, rocks, trees, large objects
- Blocks player movement completely

**Layer 1: Water** (Future)
- Water tiles
- Requires swimming ability (Phase 2)

**Non-Collidable:**
- Grass, dirt, paths (walkable)
- Small flowers, decorations

---

## Creating Tiles (Guidelines)

### General Principles
1. **Seamless Tiling:** Edges must connect perfectly
2. **Visual Interest:** Avoid repetitive patterns
3. **Readable:** Clear what's walkable vs. blocked
4. **Consistent Style:** All tiles feel cohesive
5. **Lighting:** Consistent light source (top-left)

### Grass Tiles
```
ASCII representation of grass tile variations:

Tile 0 (plain):          Tile 1 (flowers):       Tile 2 (tall grass):
................         ................        ......##........
.##..##...##....         .##.o##o..##....        ....####........
..##..##....##..         ..##..##....##..        .##..##...##....
....##..##......         ....##..##......        ..##....####....
.##....##...##..         .##....##o..##..        ......##..##....
..##......##....         ..##......##....        .##..........##.
```

### Cliff/Wall Tiles
```
Top edge (facing down):  Cliff face:
################         ................
################         ....####........
################         ..######........
##............##         ########........
```

### Tree Tiles (2×2 composition)
```
Top-left:    Top-right:       Bottom-left:  Bottom-right:
  ####         ####              ##            ##
 ######       ######             ##            ##
###  ###      ###  ###           ##            ##
##    ##      ##    ##           ##            ##
```

---

## Step-by-Step Creation

### Tools
- Aseprite, Libresprite, or Tiled
- Godot's built-in tileset editor

### Workflow:

1. **Create Tileset Image (256×256)**
   - Set up 16×16 grid
   - Start with basic grass (tile 0)
   - Create variations

2. **Draw Transition Tiles**
   - Grass to dirt edges
   - Water to shore
   - Use smooth, natural transitions

3. **Add Detail Tiles**
   - Flowers, rocks, decorations
   - Place strategically for visual interest

4. **Create Obstacle Tiles**
   - Trees (2×2 large objects)
   - Cliffs and walls
   - Ensure clear silhouettes

5. **Export**
   - PNG format, transparency where needed
   - No padding or margin
   - Save as `main_tileset.png`

---

## Godot TileSet Resource Setup

### Import Settings:
1. Import PNG: **Filter = Nearest**, Mipmaps = Off
2. Create TileSet resource: `main_tileset.tres`

### Configure in Godot:
1. **Open TileSet editor**
2. **Add tileset image**
3. **Set tile size:** 16×16
4. **Auto-create tiles** from grid

5. **Set up Physics Layers:**
   - Physics Layer 0: Terrain collision
   - Select solid tiles (walls, trees, rocks, cliffs)
   - Create collision polygon (usually full 16×16 square)

6. **Terrain Sets** (optional for Phase 1):
   - Grass terrain
   - Dirt terrain
   - Can add auto-tiling later

---

## Phase 1 Test Map Requirements

To test tileset, create a small test map with:
- [ ] Grass areas (walkable)
- [ ] Dirt path (walkable)
- [ ] Water (blocked, or walkable if no collision)
- [ ] Trees as obstacles (blocked)
- [ ] Cliffs/walls defining boundaries (blocked)
- [ ] Rocks scattered (blocked)
- [ ] Visual variety (different grass tiles)

**Test Map Size:** 32×32 tiles (512×512 pixels)

---

## Time Estimate

**Experienced pixel artist:** 4-6 hours for 50-60 tiles
**Beginner:** 8-12 hours
**With auto-tiling setup:** +2-3 hours

---

## Quick Placeholder Option

For immediate testing:
1. Create simple colored squares:
   - Green = grass (walkable)
   - Brown = dirt (walkable)
   - Blue = water (walkable for now)
   - Gray = wall (collision)
   - Dark green = tree (collision)

2. This allows testing collision and movement while creating proper art

---

## References

- Link to the Past overworld tiles
- Stardew Valley farm tiles
- Pokemon Gen 2/3 tiles (transition style)
- Celeste level tiles

---

## Deliverable Checklist

- [ ] 256×256 tileset image created
- [ ] At least 50 unique tiles
- [ ] Grass, dirt, water, walls, trees, rocks included
- [ ] Proper transparency
- [ ] Clean pixel art (no anti-aliasing)
- [ ] Imported into Godot with Nearest filter
- [ ] TileSet resource configured
- [ ] Collision shapes set for solid tiles
- [ ] Test map created and functional

---

**Status:** Specification Complete
**Next Step:** Create tileset PNG and configure in Godot
