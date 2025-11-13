# 🤖 Agent Directory

**Complete Specifications for All 28 AI Agents**

This directory contains detailed specifications for all agents involved in developing the SNES-style Action-RPG game that combines Zelda and Stardew Valley mechanics.

---

## 📋 Quick Reference

| # | Agent Name | Category | Key Specialization |
|---|------------|----------|-------------------|
| 01 | Game Design Researcher | Research & Strategy | Mechanics, Player Psychology |
| 02 | Technical Researcher | Research & Strategy | SNES Hardware, Tools |
| 03 | Player Experience Researcher | Research & Strategy | UX, Accessibility |
| 04 | Character Sprite Artist | Art & Graphics | Character Sprites, Animation |
| 05 | Environment & Tileset Artist | Art & Graphics | Tilesets, Environments |
| 06 | UI/UX Designer | Art & Graphics | Interface Design |
| 07 | Animation Specialist | Art & Graphics | Animation Timing, Effects |
| 08 | Icon & Item Artist | Art & Graphics | Items, Icons |
| 09 | Engine Architect | Programming | Core Engine, Game Loop |
| 10 | Combat System Developer | Programming | Combat Mechanics, AI |
| 11 | Farming System Developer | Programming | Farming, Calendar |
| 12 | NPC & Dialogue System Developer | Programming | NPCs, Relationships |
| 13 | Physics & Collision Developer | Programming | Movement, Collision |
| 14 | Progression & Save System Developer | Programming | Save/Load, Inventory |
| 15 | Menu & UI Developer | Programming | Menus, UI Implementation |
| 16 | Audio System Developer | Programming | Audio Engine, Integration |
| 17 | World & Level Designer | Content Creation | Map Design, Layouts |
| 18 | Dungeon & Puzzle Designer | Content Creation | Puzzles, Challenges |
| 19 | Quest Designer | Content Creation | Quests, Objectives |
| 20 | Character & Lore Writer | Content Creation | Characters, Backstory |
| 21 | Dialogue Writer | Content Creation | Dialogue, Text |
| 22 | Item & Equipment Designer | Content Creation | Item Stats, Balance |
| 23 | Music Composer | Audio | Music, Soundtrack |
| 24 | Sound Effect Designer | Audio | SFX, Audio Feedback |
| 25 | Gameplay Tester | Quality Assurance | Playtesting, Bugs |
| 26 | Balance Specialist | Quality Assurance | Game Balance, Tuning |
| 27 | Performance & QA Engineer | Quality Assurance | Optimization, QA |
| 28 | Project Coordinator | Project Management | Orchestration, Planning |

---

## 📁 Directory Structure

```
agents/
├── 01-research-strategy/
│   ├── agent-01-game-design-researcher.md
│   ├── agent-02-technical-researcher.md
│   └── agent-03-player-experience-researcher.md
├── 02-art-graphics/
│   ├── agent-04-character-sprite-artist.md
│   ├── agent-05-environment-tileset-artist.md
│   ├── agent-06-ui-ux-designer.md
│   ├── agent-07-animation-specialist.md
│   └── agent-08-icon-item-artist.md
├── 03-programming/
│   ├── agent-09-engine-architect.md
│   ├── agent-10-combat-system-developer.md
│   ├── agent-11-farming-system-developer.md
│   ├── agent-12-npc-dialogue-system-developer.md
│   ├── agent-13-physics-collision-developer.md
│   ├── agent-14-progression-save-system-developer.md
│   ├── agent-15-menu-ui-developer.md
│   └── agent-16-audio-system-developer.md
├── 04-content-creation/
│   ├── agent-17-world-level-designer.md
│   ├── agent-18-dungeon-puzzle-designer.md
│   ├── agent-19-quest-designer.md
│   ├── agent-20-character-lore-writer.md
│   ├── agent-21-dialogue-writer.md
│   └── agent-22-item-equipment-designer.md
├── 05-audio/
│   ├── agent-23-music-composer.md
│   └── agent-24-sound-effect-designer.md
├── 06-quality-assurance/
│   ├── agent-25-gameplay-tester.md
│   ├── agent-26-balance-specialist.md
│   └── agent-27-performance-qa-engineer.md
└── 07-project-management/
    └── agent-28-project-coordinator.md
```

---

## 🎯 Agent Categories

### 1. Research & Strategy (3 Agents)
**Purpose:** Research best practices, analyze player needs, and provide strategic direction

- **Game Design Researcher:** Studies successful mechanics and fun factors
- **Technical Researcher:** Investigates SNES hardware and development tools
- **Player Experience Researcher:** Analyzes UX, accessibility, and player feedback

**When to activate:** Project start, before major design decisions

---

### 2. Art & Graphics (5 Agents)
**Purpose:** Create all visual assets within SNES constraints

- **Character Sprite Artist:** Player, NPCs, enemies, bosses
- **Environment & Tileset Artist:** Tilesets for all areas
- **UI/UX Designer:** Interface mockups and designs
- **Animation Specialist:** Animation timing and particle effects
- **Icon & Item Artist:** Items, equipment, icons

**When to activate:** After technical specs established, early in project

---

### 3. Programming (8 Agents)
**Purpose:** Implement all game systems and functionality

- **Engine Architect:** Core game engine (CRITICAL PATH)
- **Combat System Developer:** Combat mechanics and AI
- **Farming System Developer:** Farming and calendar systems
- **NPC & Dialogue System Developer:** Social systems
- **Physics & Collision Developer:** Movement and collision
- **Progression & Save System Developer:** Save/load, inventory
- **Menu & UI Developer:** UI implementation
- **Audio System Developer:** Audio engine

**When to activate:** Engine first, then systems in parallel

---

### 4. Content Creation (6 Agents)
**Purpose:** Create game content, narrative, and data

- **World & Level Designer:** Maps and layouts
- **Dungeon & Puzzle Designer:** Dungeons and puzzles
- **Quest Designer:** Quests and objectives
- **Character & Lore Writer:** Characters and world lore
- **Dialogue Writer:** All dialogue and text
- **Item & Equipment Designer:** Item stats and progression

**When to activate:** After core systems functional

---

### 5. Audio (2 Agents)
**Purpose:** Create music and sound effects

- **Music Composer:** All game music
- **Sound Effect Designer:** All SFX

**When to activate:** Early for planning, main work mid-project

---

### 6. Quality Assurance (3 Agents)
**Purpose:** Test, balance, and ensure quality

- **Gameplay Tester:** Playtesting and bug discovery
- **Balance Specialist:** Game balance and tuning
- **Performance & QA Engineer:** Optimization and technical QA

**When to activate:** Throughout project, intensify near completion

---

### 7. Project Management (1 Agent)
**Purpose:** Orchestrate all agents and manage project

- **Project Coordinator:** Task management, coordination, timeline

**When to activate:** Project start, remains active throughout

---

## 🔄 Typical Workflow

### Phase 1: Foundation
1. **Activate:** Research agents (#01-03)
2. **Activate:** Engine Architect (#09)
3. **Activate:** Basic art agents (#04-05)
4. **Output:** Technical specs, core engine, basic assets

### Phase 2: Core Systems
1. **Activate:** Programming agents (#10-16) in parallel
2. **Activate:** Remaining art agents (#06-08)
3. **Activate:** Content agents begin planning (#17-22)
4. **Output:** Functional game systems

### Phase 3: Content Creation
1. **Activate:** All content agents (#17-22) in full production
2. **Activate:** Audio agents (#23-24)
3. **Continue:** Programming for features
4. **Output:** Complete game content

### Phase 4: Polish & Release
1. **Activate:** All QA agents (#25-27) at full capacity
2. **Continue:** All agents on bug fixes and polish
3. **Coordinate:** Final integration
4. **Output:** Release-ready game

---

## 🔗 Critical Dependencies

### Must Complete First
- **Agent #02 (Technical Researcher)** → Specs for all technical agents
- **Agent #09 (Engine Architect)** → Foundation for all programming
- **Agent #04 (Character Sprite Artist)** → Player sprite for testing
- **Agent #05 (Environment Tileset Artist)** → Tiles for testing

### Can Work in Parallel
- All art agents (#04-08) can work simultaneously
- Programming agents on different systems (#10-16) can work simultaneously
- Content agents on different areas (#17-22) can work simultaneously

---

## 📊 Agent Activation Checklist

When activating an agent:
- [ ] Read their complete specification
- [ ] Verify dependencies are met
- [ ] Provide necessary context and resources
- [ ] Establish clear deliverables
- [ ] Set timeline expectations
- [ ] Define success criteria
- [ ] Establish communication channels

---

## 💡 Tips for Working with Agents

### Research Agents
- Let them research thoroughly before making recommendations
- Use their findings to inform design decisions
- Re-activate when encountering design challenges

### Art Agents
- Provide clear technical specifications
- Request mockups before final assets
- Iterate based on in-game appearance
- Maintain consistent style across agents

### Programming Agents
- Ensure clean API boundaries
- Regular integration testing
- Document code thoroughly
- Coordinate on shared systems

### Content Agents
- Establish content pipeline early
- Use templates for consistency
- Review content in context
- Iterate based on playtesting

### Audio Agents
- Provide clear context for each track/SFX
- Test audio in actual gameplay
- Balance audio levels carefully
- Optimize for SNES constraints

### QA Agents
- Activate early and often
- Prioritize their findings
- Use feedback for iteration
- Plan time for bug fixing

---

## 🎮 Project Coordinator Role

**Agent #28** is special - it orchestrates all other agents:
- Assigns tasks to agents
- Manages dependencies
- Tracks progress
- Resolves conflicts
- Reports status

**Activate first** and keep active throughout the project.

---

## 📈 Success Metrics

### Agent Effectiveness
- Delivers on time
- Meets quality standards
- Collaborates effectively
- Adapts to feedback
- No major rework needed

### Project Success
- All agents coordinated
- Dependencies managed
- Milestones hit
- Quality maintained
- Game completed

---

## 🚀 Getting Started

**Step 1:** Read this README completely
**Step 2:** Review main project README (in root directory)
**Step 3:** Activate Agent #28 (Project Coordinator)
**Step 4:** Follow Project Coordinator's agent activation plan
**Step 5:** Begin development!

---

**Ready to build an amazing SNES game with 28 specialized AI agents!** 🎮✨

For questions about individual agents, see their detailed specification files in their respective category directories.
