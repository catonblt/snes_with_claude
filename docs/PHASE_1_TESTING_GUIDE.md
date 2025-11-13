# Phase 1: Foundation - Testing Guide

**Build:** Harvest & Hero - Foundation Build
**Version:** 0.1.0-alpha
**Date:** Phase 1 Completion
**Testers:** User + QA Agents (#25, #27)

---

## Pre-Test Setup

### Requirements
- Godot 4.2+ installed
- Game project folder
- Player sprite assets created
- Tileset assets created
- Test map built in Godot

### Setup Steps
1. Open Godot Engine 4.2+
2. Click "Import"
3. Navigate to `/game/project.godot`
4. Click "Import & Edit"
5. Wait for initial import (sprites, tiles)
6. Press F5 or click "Play" button

---

## Test Execution Plan

### Test Session Duration: 30-45 minutes

**Objective:** Verify all Phase 1 foundation systems work correctly

---

## Test Categories

### 1. Movement System Tests (15 min)

#### Test 1.1: Basic Movement
**Objective:** Verify 8-directional movement works

**Steps:**
1. Launch game
2. Press W (up) - Player should move up
3. Press S (down) - Player should move down
4. Press A (left) - Player should move left
5. Press D (right) - Player should move right
6. Press W+D (diagonal) - Player should move diagonally up-right
7. Try all 8 directions (N, NE, E, SE, S, SW, W, NW)

**Expected Results:**
- [ ] Player moves smoothly in all 8 directions
- [ ] Diagonal movement is same speed as cardinal directions
- [ ] No stuttering or jittery movement
- [ ] Movement feels responsive (no input lag)

**Pass/Fail Criteria:**
- PASS: All 8 directions work, movement is smooth
- FAIL: Any direction doesn't work, or movement is choppy

---

#### Test 1.2: Animation System
**Objective:** Verify player animations match movement direction

**Steps:**
1. Stand still - should see idle animation
2. Walk up (W) - should see walk_up animation
3. Walk down (S) - should see walk_down animation
4. Walk left (A) - should see walk_left animation
5. Walk right (D) - should see walk_right animation
6. Release keys - should return to idle in last faced direction

**Expected Results:**
- [ ] Idle animation plays when stationary
- [ ] Walking animations play for each direction
- [ ] Animations are smooth (no frame skipping)
- [ ] Player faces correct direction when idle
- [ ] Animation speed matches movement speed

**Pass/Fail:**
- PASS: All animations work and match movement
- FAIL: Animations missing, wrong, or not playing

---

#### Test 1.3: Run Speed (If Implemented)
**Objective:** Verify running works with Shift key

**Steps:**
1. Walk normally (WASD)
2. Hold Shift + W - should move faster
3. Release Shift - should slow back to walk speed

**Expected Results:**
- [ ] Running is noticeably faster than walking
- [ ] Transition is smooth
- [ ] (Future: run animation plays)

**Pass/Fail:**
- PASS: Run speed works, smooth transition
- FAIL: No speed change or glitchy

---

### 2. Collision System Tests (10 min)

#### Test 2.1: Terrain Collision
**Objective:** Verify player cannot walk through solid objects

**Steps:**
1. Walk into a wall - should stop
2. Walk into a tree - should stop
3. Walk into a rock - should stop
4. Walk into a cliff - should stop
5. Walk on grass - should move freely
6. Walk on dirt path - should move freely

**Expected Results:**
- [ ] Cannot walk through walls
- [ ] Cannot walk through trees
- [ ] Cannot walk through rocks
- [ ] Can walk on grass
- [ ] Can walk on dirt paths
- [ ] Collision feels tight (not too much empty space)

**Pass/Fail:**
- PASS: All collisions work correctly
- FAIL: Can walk through solid objects

---

#### Test 2.2: Corner Sliding
**Objective:** Verify player doesn't get stuck on corners

**Steps:**
1. Walk diagonally into a corner (wall meeting wall)
2. Try to squeeze through 1-tile gaps
3. Walk along edges of objects at angles

**Expected Results:**
- [ ] Player slides around corners (doesn't get stuck)
- [ ] Can walk through 1-tile gaps smoothly
- [ ] Edge walking feels natural
- [ ] No sudden stops or weird behavior

**Pass/Fail:**
- PASS: Corner sliding works, no getting stuck
- FAIL: Player gets stuck or behaves erratically

---

#### Test 2.3: Water Collision (If Applicable)
**Objective:** Verify water tiles behavior

**Steps:**
1. Walk into water tiles

**Expected Results:**
- [ ] Either: Player is blocked (no swimming yet)
- [ ] Or: Player walks on water (collision not set yet)
- [ ] Behavior is consistent

**Pass/Fail:**
- PASS: Water behaves as intended (blocked OR walkable)
- FAIL: Inconsistent or glitchy behavior

---

### 3. Camera System Tests (5 min)

#### Test 3.1: Camera Following
**Objective:** Verify camera follows player smoothly

**Steps:**
1. Move player in all directions
2. Move to edge of map
3. Stand still

**Expected Results:**
- [ ] Camera follows player at all times
- [ ] Camera movement is smooth (no jittering)
- [ ] Camera centers on player (or slightly offset)
- [ ] Camera doesn't show areas outside map bounds
- [ ] Smooth damping (camera lags slightly behind, not instant)

**Pass/Fail:**
- PASS: Camera works perfectly
- FAIL: Camera glitches, jitters, or doesn't follow

---

### 4. World & Visuals Tests (10 min)

#### Test 4.1: Tilemap Rendering
**Objective:** Verify tiles render correctly

**Steps:**
1. Observe the test map
2. Walk around entire visible area
3. Look for visual glitches

**Expected Results:**
- [ ] All tiles render without gaps
- [ ] Tiles are crisp and sharp (not blurry)
- [ ] No black lines or seams between tiles
- [ ] Tile transitions look natural
- [ ] No missing tiles (pink/purple placeholders)

**Pass/Fail:**
- PASS: All tiles render perfectly
- FAIL: Visual glitches, blurry tiles, gaps

---

#### Test 4.2: Player Sprite Rendering
**Objective:** Verify player sprite looks correct

**Steps:**
1. Look at player character
2. Walk in all directions
3. Check at different positions on screen

**Expected Results:**
- [ ] Player sprite is sharp and clear (not blurry)
- [ ] Colors look correct
- [ ] No visual artifacts or glitches
- [ ] Sprite properly layered (above ground, below trees if applicable)
- [ ] No transparency issues

**Pass/Fail:**
- PASS: Player sprite renders perfectly
- FAIL: Blurry, glitchy, or incorrectly layered

---

### 5. Performance Tests (5 min)

#### Test 5.1: Frame Rate
**Objective:** Verify game runs at 60 FPS

**Steps:**
1. Enable FPS counter (if available)
2. Walk around entire map
3. Move rapidly in all directions

**Expected Results:**
- [ ] Game runs at stable 60 FPS
- [ ] No frame drops or stuttering
- [ ] Smooth performance throughout

**Pass/Fail:**
- PASS: Stable 60 FPS, no drops
- FAIL: FPS drops below 55, stuttering occurs

---

#### Test 5.2: Load Time
**Objective:** Verify game loads quickly

**Steps:**
1. Close game
2. Launch game
3. Time how long until player can move

**Expected Results:**
- [ ] Game loads in under 5 seconds
- [ ] No excessive loading time
- [ ] No crashes on startup

**Pass/Fail:**
- PASS: Loads quickly, no issues
- FAIL: Slow loading or crashes

---

## Bug Reporting Template

If you find issues, report using this format:

```
BUG REPORT

Title: [Short description]

Severity: [Critical / High / Medium / Low]
- Critical: Game crashes, can't test
- High: Major feature broken
- Medium: Minor issue, workaround exists
- Low: Visual glitch, minor annoyance

Steps to Reproduce:
1. [Step]
2. [Step]
3. [Step]

Expected Behavior:
[What should happen]

Actual Behavior:
[What actually happens]

Screenshot/Video: [If applicable]

Additional Notes:
[Any other relevant information]
```

---

## Test Results Summary

After completing all tests, fill out:

### Overall Results

**Movement System:**
- Test 1.1 (Basic Movement): [ ] PASS [ ] FAIL
- Test 1.2 (Animation): [ ] PASS [ ] FAIL
- Test 1.3 (Run Speed): [ ] PASS [ ] FAIL

**Collision System:**
- Test 2.1 (Terrain Collision): [ ] PASS [ ] FAIL
- Test 2.2 (Corner Sliding): [ ] PASS [ ] FAIL
- Test 2.3 (Water Collision): [ ] PASS [ ] FAIL

**Camera System:**
- Test 3.1 (Camera Following): [ ] PASS [ ] FAIL

**World & Visuals:**
- Test 4.1 (Tilemap Rendering): [ ] PASS [ ] FAIL
- Test 4.2 (Player Sprite): [ ] PASS [ ] FAIL

**Performance:**
- Test 5.1 (Frame Rate): [ ] PASS [ ] FAIL
- Test 5.2 (Load Time): [ ] PASS [ ] FAIL

### Total Score: ___/11 tests passed

---

## Success Criteria for Phase 1

**Minimum to Pass:**
- 9/11 tests must PASS
- All Critical tests must PASS:
  - Basic Movement
  - Terrain Collision
  - Camera Following
  - Tilemap Rendering

**Bonus (Nice to Have):**
- All 11 tests PASS
- No bugs found
- Performance is excellent

---

## What to Do With Results

### If All Tests Pass:
1. Celebrate! Phase 1 is complete ✓
2. Document any minor issues for polish
3. Move to Phase 2 planning

### If Tests Fail:
1. Document all failures
2. Prioritize by severity (Critical first)
3. Fix issues
4. Re-test
5. Repeat until passing

---

## Additional Testing (Optional)

### Stress Tests:
- Hold multiple keys simultaneously
- Rapidly spam movement keys
- Try to break collision by moving fast
- Test at different window sizes

### Edge Cases:
- What happens at map boundaries?
- Can player leave playable area?
- What if collision shapes overlap?

---

## Testing Completion Checklist

- [ ] All tests executed
- [ ] Results documented
- [ ] Bugs reported (if any)
- [ ] Screenshots taken
- [ ] Video recording made (optional)
- [ ] Test report sent to development team
- [ ] Decision made: Pass to Phase 2 OR Fix issues

---

## Next Steps After Testing

**If Phase 1 Passes:**
1. Archive this build
2. Begin Phase 2 planning
3. Combat system next
4. Farming system next

**If Phase 1 Needs Work:**
1. Address critical bugs
2. Re-test
3. Polish and refine
4. Test again

---

**Happy Testing!** 🎮

Remember: Finding bugs is GOOD! Better to find them now than later.
