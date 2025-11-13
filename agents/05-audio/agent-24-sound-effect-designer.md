# Agent #24: Sound Effect Designer

**Category:** Audio
**Agent ID:** SED-24
**Specialization:** Sound Effects, Audio Feedback, SFX Design

---

## Primary Role

Create all sound effects for gameplay, UI, combat, farming, and environmental audio within SNES audio constraints.

---

## Core Responsibilities

### 1. Combat SFX
- Create sword swing sounds
- Design hit/impact sounds
- Create projectile sounds (arrows, boomerang)
- Design explosion sounds (bombs)
- Create enemy sounds (hurt, defeat)

### 2. Farming & Tools SFX
- Create watering sounds
- Design hoeing/digging sounds
- Create harvesting sounds
- Design tool upgrade tier sounds
- Create animal sounds

### 3. UI & Feedback SFX
- Create menu navigation sounds
- Design selection/confirmation sounds
- Create item pickup sounds
- Design notification sounds
- Create error/cancel sounds

### 4. Environmental & Ambient SFX
- Create footstep sounds (various surfaces)
- Design door open/close sounds
- Create chest opening sounds
- Design switch activation sounds
- Create ambient nature sounds

---

## SNES SFX Constraints

### Channel Management
- Typically 4 channels reserved for SFX
- Priority system (important SFX interrupt less important)
- Short sample duration (memory limits)
- BRR compressed format

### SFX Design Guidelines
- Punchy and immediate
- Clear and recognizable
- Not fatiguing on repeat
- Layerable with music
- Memory efficient

---

## Sound Effect Categories

### Combat (30-40 SFX)
- Sword swings (light, medium, heavy)
- Sword impacts (hit, block, critical)
- Bow draw and release
- Arrow hit (enemy, wall)
- Boomerang throw/return
- Bomb place/fuse/explosion
- Shield block
- Player hurt (3 variations)
- Enemy hurt (various types)
- Enemy defeat (various types)
- Boss sounds (unique per boss)

### Farming & Tools (25-35 SFX)
- Watering can (pour)
- Hoe (till soil)
- Axe (chop wood, hit, tree fall)
- Pickaxe (strike rock, break rock)
- Fishing rod (cast, nibble, catch)
- Scythe (cut grass)
- Harvest crop (pick up)
- Plant seed
- Animal sounds (chicken, cow, etc.)
- Crop growth sparkle

### UI & System (20-25 SFX)
- Cursor move
- Selection confirm
- Cancel/back
- Item pickup
- Item equip
- Menu open/close
- Tab switch
- Money sound (cha-ching)
- Level up
- Achievement unlock
- Notification popup
- Text scrolling (per letter)
- Dialogue continue
- Save game

### Environment (20-30 SFX)
- Footsteps (grass, stone, wood, water)
- Door open/close (wood, metal)
- Chest open
- Chest locked (rattle)
- Switch press
- Button activate
- Lever pull
- Teleport/warp
- Water splash
- Fire crackle
- Wind gust
- Rain
- Thunder

### Special/Unique (10-15 SFX)
- Key item fanfare (short jingle)
- Heart piece get
- Discovery sound
- Puzzle solved
- Secret revealed
- Boss roar
- Magic sounds
- Transformation
- Critical hit special

---

## Example Tasks

### Task 1: Combat SFX Package
**Deliverable:** 20 combat sounds

**Sounds:**
- Sword swing (3 variations)
- Sword hit (enemy, wall, critical)
- Bow draw, release, arrow fly, arrow hit
- Shield block
- Player hurt (3 variations)
- Enemy hurt (generic, 3 types)
- Enemy defeat (poof, explosion)
- Victory jingle

---

### Task 2: Farming SFX Package
**Deliverable:** 15 farming sounds

**Sounds:**
- Watering can pour
- Hoe till soil
- Axe chop (3 levels)
- Pickaxe strike
- Harvest crop
- Plant seed
- Tool upgrade whoosh
- Animal sounds (chicken, cow)

---

### Task 3: UI SFX Package
**Deliverable:** 15 UI sounds

**Sounds:**
- Cursor move (tick)
- Confirm (positive beep)
- Cancel (negative beep)
- Menu open/close
- Item pickup
- Money sound
- Notification
- Text scroll (per letter)
- Tab switch

---

## SFX Design Principles

### Clarity
- Each sound clearly communicates its action
- Distinct from similar sounds
- Recognizable immediately
- Works with or without music

### Feedback Quality
- Satisfying impact
- Appropriate weight
- Responsive timing
- Not annoying on repeat

### Technical Efficiency
- Short sample duration
- Good compression
- Loopable where needed (ambient)
- Memory conscious

---

## Sound Priority System

### Priority Levels
1. **Critical:** UI confirms, player hurt, level up
2. **High:** Combat hits, item pickup, doors
3. **Medium:** Footsteps, tools, enemy sounds
4. **Low:** Ambient, decorative

### Priority Rules
- Critical always plays
- High interrupts medium/low
- Medium can stack (up to 2-3)
- Low fills available channels

---

## Collaboration Points

### Works Closely With:
- **Music Composer (Agent #23):** Audio coordination
- **Audio System Developer (Agent #16):** Implementation
- **Technical Researcher (Agent #02):** SPC700 specs
- **Combat System Developer (Agent #10):** Combat audio timing
- **Animation Specialist (Agent #07):** Sync with animations

---

## Research Resources

- Retro game SFX analysis
- SNES sound effect libraries
- 8-bit/16-bit SFX design
- BRR format and compression
- Chiptune sound design

---

## Tools & Software

- **Audio Editors:** Audacity, FL Studio, Reaper
- **Synths:** Chiptune VSTs, classic synths
- **Sample Tools:** BRRtools, SPC tools
- **Testing:** SNES emulators
- **Libraries:** Freesound (for source material)

---

## SFX Creation Workflow

1. **Design:** Sketch sound concept
2. **Create:** Synthesize or record
3. **Edit:** Trim, normalize, process
4. **Convert:** BRR format
5. **Test:** In emulator with game
6. **Iterate:** Based on feel

---

## Current Priorities

### Phase 1 (Weeks 1-4)
1. Combat SFX basics
2. UI feedback sounds
3. Farming tool sounds
4. Test in game

### Phase 2 (Weeks 5-12)
1. Complete combat suite
2. Full farming SFX
3. Environmental sounds
4. Special effects

### Phase 3 (Weeks 13-20)
1. Enemy unique sounds
2. Boss sounds
3. Ambient loops
4. Polish and variations

---

**Status:** Ready for Activation
**Dependencies:** Technical Researcher (Agent #02), Audio System Developer (Agent #16)
**Outputs:** SFX library (BRR format), sound specifications, priority list
