extends Node

## Global autoloaded singleton
## Manages game state, player data, and global systems

# Game state
var player: Player = null
var current_scene: String = ""

# Player stats (will expand in Phase 2)
var player_data = {
	"health": 100,
	"max_health": 100,
	"energy": 100,
	"max_energy": 100,
	"money": 500,
	"day": 1,
	"season": "spring",
	"year": 1
}

# Game settings
var game_settings = {
	"fullscreen": false,
	"vsync": true,
	"show_fps": false
}

func _ready():
	print("Global system initialized")
	# Set up initial settings
	DisplayServer.window_set_vsync_mode(DisplayServer.VSYNC_ENABLED if game_settings.vsync else DisplayServer.VSYNC_DISABLED)

func _process(delta):
	# Debug: Show FPS if enabled
	if game_settings.show_fps:
		pass  # Will add FPS display in Phase 2

# Player management
func set_player(p: Player):
	player = p
	print("Player reference set in Global")

func get_player() -> Player:
	return player

# Scene management
func change_scene(scene_path: String):
	current_scene = scene_path
	get_tree().change_scene_to_file(scene_path)

# Save/Load (placeholder for Phase 2)
func save_game():
	print("Save functionality coming in Phase 2")
	# Will implement save system

func load_game():
	print("Load functionality coming in Phase 2")
	# Will implement load system

# Utility functions
func get_current_time_string() -> String:
	return "Day %d, %s, Year %d" % [player_data.day, player_data.season.capitalize(), player_data.year]
