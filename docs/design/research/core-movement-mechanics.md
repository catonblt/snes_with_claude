# Core Movement Mechanics Research

**Agent:** Game Design Researcher (#01)
**Date:** Phase 1 Foundation
**Topic:** Player Movement System Design

---

## Research Summary

### Movement Style: Smooth Pixel-Based (Like Link to the Past)

**Key Decision:** Use **smooth, pixel-based movement** NOT grid-locked movement

### Reference Game Analysis

#### The Legend of Zelda: A Link to the Past
- **Movement:** Smooth pixel movement (not grid-based)
- **Collision:** 8×8 sub-tile collision detection
- **Corner Rounding:** When player collides with corners, physics deflects them at 45° angle
- **Feel:** Fluid, responsive, no "snapping" to grid

#### Stardew Valley
- **Controls:** WASD 8-directional movement
- **Movement:** Smooth (not grid-locked)
- **Speed:** Moderate walking speed, run available
- **Input:** Keyboard primary, controller secondary

---

## Our Implementation (Phase 1)

### Movement Specifications

**Speed Values:**
- Walk Speed: 100 pixels/second
- Run Speed: 150 pixels/second (hold Shift)
- Diagonal Speed: Same as cardinal (normalized vector)

**Input:**
- WASD or Arrow Keys for movement
- Shift for running (optional for Phase 1)
- Controller support (future)

**Physics:**
- Smooth acceleration (no instant start/stop)
- Corner sliding/rounding (don't get stuck on corners)
- 8×8 tile collision (sub-tile precision)

**Animation:**
- 4-direction sprites (N, S, E, W)
- Walking animation (3-4 frames per direction)
- Idle animation (facing last direction)

---

## Technical Implementation Notes

### Godot CharacterBody2D
- Use `move_and_slide()` for smooth collision
- `Input.get_vector()` for 8-directional input
- Normalize diagonal movement (prevents faster diagonal movement)

### Collision System
- Tiles: 16×16 visual, but collision can be per-8×8 sub-tile
- Character collision box: 12×8 pixels (smaller than visual sprite)
- Collision layers: Player (1), Terrain (2), NPCs (3), Enemies (4)

### Corner Rounding
- Godot handles this automatically with `move_and_slide()`
- Player doesn't get "stuck" on corners
- Slides smoothly around obstacles

---

## Feel Targets

Based on research, player movement should feel:
- **Responsive:** Immediate input recognition
- **Smooth:** No stuttering or jerkiness
- **Precise:** Can navigate tight spaces
- **Natural:** Corner sliding, not getting stuck
- **Satisfying:** Animations match movement well

---

## Phase 1 Implementation Checklist

- [ ] 8-directional input (WASD/Arrows)
- [ ] Smooth pixel movement (not grid-locked)
- [ ] Walk speed: 100 px/s
- [ ] Collision with tiles
- [ ] Corner sliding (automatic with Godot)
- [ ] Walking animation (4 directions)
- [ ] Idle animation
- [ ] Camera follows player

**Future Enhancements (Phase 2+):**
- Running (Shift key)
- Swimming mechanics
- Climbing ladders
- Rolling/dodge

---

## Code Snippet (Preview)

```gdscript
extends CharacterBody2D

const WALK_SPEED = 100.0

func _physics_process(delta):
    # Get 8-directional input
    var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")

    # Set velocity (automatically normalized for diagonals)
    velocity = input_dir * WALK_SPEED

    # Move with collision
    move_and_slide()

    # Update animation based on direction
    update_animation(input_dir)
```

---

## References

- Link to the Past movement analysis
- Stardew Valley control documentation
- Godot CharacterBody2D documentation

**Status:** Research Complete ✓
**Next:** Implement in Godot with Engine Architect
