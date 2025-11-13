# Player Character Sprite Specification
## Phase 1: Foundation

**Artist:** Character Sprite Artist (Agent #04)
**Target Engine:** Godot 4.2
**File Format:** PNG (with transparency)
**Color Depth:** Indexed color, retro SNES-style palette

---

## Specifications

### Sprite Dimensions
- **Character Size:** 16×16 pixels per frame
- **Sheet Layout:**4 rows × 4 columns = 16 frames total
- **Sheet Size:** 64×64 pixels

### Animation Sets Needed (Phase 1)

1. **idle_down** - 1 frame (standing, facing down/forward)
2. **idle_up** - 1 frame (standing, facing up/away)
3. **idle_left** - 1 frame (standing, facing left)
4. **idle_right** - 1 frame (standing, facing right)

5. **walk_down** - 3 frames (walking down/forward)
6. **walk_up** - 3 frames (walking up/away)
7. **walk_left** - 3 frames (walking left)
8. **walk_right** - 3 frames (walking right)

---

## Color Palette (SNES-Style)

```
Skin:      #FFDBAC, #F4A460, #D2691E
Hair:      #8B4513, #654321
Clothes:   #4169E1 (blue shirt), #228B22 (green pants)
Outline:   #000000
Highlights: #FFFFFF (eyes, shine)
```

---

## Character Design

**Character Concept:** Young farmer/adventurer
- Simple, friendly design
- Clear silhouette
- Gender-neutral or customizable (Phase 1: default design)
- Wears practical farmer clothes with adventurer elements

**Visual Style:**
- SNES RPG character (Link to the Past, Earthbound aesthetic)
- Bold outlines (1px black border)
- Readable at small size
- Expressive despite pixel limitations

---

## Sprite Sheet Layout

```
Row 1: idle_down(0,0), walk_down_1(1,0), walk_down_2(2,0), walk_down_3(3,0)
Row 2: idle_up(0,1), walk_up_1(1,1), walk_up_2(2,1), walk_up_3(3,1)
Row 3: idle_left(0,2), walk_left_1(1,2), walk_left_2(2,2), walk_left_3(3,2)
Row 4: idle_right(0,3), walk_right_1(1,3), walk_right_2(2,3), walk_right_3(3,3)
```

---

## ASCII Art Reference (Visual Guide)

### Facing Down (Front View)
```
  ####
 ######
#O#OO#O#  <- face
 #####
  ####    <- body (blue shirt)
 ##  ##
 ##  ##   <- legs (green)
##    ##  <- feet
```

### Facing Up (Back View)
```
  ####
 ######
 ######  <- back of head
 #####
  ####   <- body
 ##  ##
 ##  ##  <- legs
##    ##
```

### Facing Left
```
  ###
 ####
#O###    <- profile
 ####
  ###
 ####
  ####
 ##  ##
```

### Facing Right (mirror of left)
```
 ###
####
###O#
####
 ###
####
####
##  ##
```

---

## Walking Animation Timing

- **Frame Duration:** 0.15 seconds per frame (150ms)
- **Total Walk Cycle:** 0.45 seconds (3 frames)
- **Loop:** Yes (seamless)

**Walk Cycle Frames:**
1. Contact position (one foot forward)
2. Pass-through (legs passing each other)
3. Contact position (other foot forward)
4. (loop back to idle or frame 1)

---

## Creating the Sprite Sheet (Step-by-Step)

### Tools Needed
- **Aseprite** (recommended, $20) or **Libresprite** (free fork)
- OR **Piskel** (free, web-based)
- OR any pixel art editor

### Steps:

1. **Create New File**
   - Size: 64×64 pixels
   - Color mode: Indexed

2. **Set Up Grid**
   - Grid size: 16×16 pixels
   - This helps align sprites

3. **Draw Idle Down** (0, 0)
   - Start with simple silhouette
   - Add black outline
   - Fill with colors
   - Add face details (eyes, mouth)

4. **Create Walk Down Frames**
   - Copy idle frame
   - Modify leg positions for each frame
   - Subtle head bob (1-2 pixels)
   - Arms swing slightly

5. **Create Other Directions**
   - Up: Back of head, different leg positions
   - Left: Profile view, one arm visible
   - Right: Mirror of left (can flip in code)

6. **Export**
   - Format: PNG
   - Transparency: Enabled
   - No padding or margins
   - Save as: `player_spritesheet.png`

---

## Godot Import Settings

Once sprite sheet is created:

1. Import the PNG into Godot
2. Select the image in FileSystem
3. In Import tab, set:
   - **Filter:** Nearest (NOT Linear!)
   - **Mipmaps:** Off
   - **Repeat:** Disabled
4. Click "Reimport"

---

## Creating SpriteFrames Resource

1. Create new SpriteFrames resource: `player_animations.tres`
2. Add animations:
   - idle_down, idle_up, idle_left, idle_right
   - walk_down, walk_up, walk_left, walk_right
3. For each animation, add frames from sprite sheet
4. Set FPS to 6.67 (or use default and adjust speed)

---

## Phase 1 Deliverable Checklist

- [ ] 64×64 sprite sheet PNG created
- [ ] All 16 frames present (4 idle + 12 walk)
- [ ] Proper transparency
- [ ] Clean pixel art (no anti-aliasing)
- [ ] Imported into Godot with Nearest filter
- [ ] SpriteFrames resource configured
- [ ] Animations play smoothly in-game

---

## Time Estimate

**Experienced pixel artist:** 2-3 hours
**Beginner:** 4-6 hours
**With tutorials:** 6-8 hours

---

## Quick Start Option (Placeholder)

If you need a quick placeholder to test the game:

1. Use a simple colored rectangle (16×16 blue square)
2. Add a small colored dot for "face" direction
3. This allows testing movement while creating proper sprites

---

## References

- Link to the Past character sprites
- Stardew Valley character design
- Earthbound character style
- Celeste character animation

---

**Status:** Specification Complete
**Next Step:** Create actual sprite sheet PNG file using this specification
