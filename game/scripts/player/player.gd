extends CharacterBody2D
class_name Player

## Player character with smooth 8-directional movement
## Handles input, movement, animation, and collision

# Movement constants
const WALK_SPEED = 100.0
const RUN_SPEED = 150.0

# Animation states
enum State { IDLE, WALKING }
enum Direction { DOWN, UP, LEFT, RIGHT }

# Current state
var current_state: State = State.IDLE
var current_direction: Direction = Direction.DOWN

# References (set in editor)
@onready var animated_sprite: AnimatedSprite2D = $AnimatedSprite2D
@onready var collision_shape: CollisionShape2D = $CollisionShape2D

func _ready():
	# Initialize player
	print("Player initialized")
	# Set up collision layer/mask
	collision_layer = 1  # Player layer
	collision_mask = 2  # Collides with terrain layer

func _physics_process(delta):
	# Get input direction (8-directional)
	var input_dir = Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")

	# Determine speed (walk or run)
	var speed = RUN_SPEED if Input.is_action_pressed("run") else WALK_SPEED

	# Set velocity
	if input_dir != Vector2.ZERO:
		velocity = input_dir * speed
		current_state = State.WALKING
		update_direction(input_dir)
	else:
		velocity = Vector2.ZERO
		current_state = State.IDLE

	# Move and handle collisions
	move_and_slide()

	# Update animation
	update_animation()

func update_direction(input_dir: Vector2):
	"""Update character facing direction based on input"""
	# Prioritize cardinal directions
	if abs(input_dir.x) > abs(input_dir.y):
		# Moving more horizontally
		current_direction = Direction.RIGHT if input_dir.x > 0 else Direction.LEFT
	else:
		# Moving more vertically
		current_direction = Direction.DOWN if input_dir.y > 0 else Direction.UP

func update_animation():
	"""Update sprite animation based on state and direction"""
	if not animated_sprite:
		return

	# Build animation name
	var anim_name = ""

	match current_state:
		State.IDLE:
			anim_name = "idle_"
		State.WALKING:
			anim_name = "walk_"

	match current_direction:
		Direction.DOWN:
			anim_name += "down"
		Direction.UP:
			anim_name += "up"
		Direction.LEFT:
			anim_name += "left"
		Direction.RIGHT:
			anim_name += "right"

	# Play animation if it exists
	if animated_sprite.sprite_frames.has_animation(anim_name):
		if animated_sprite.animation != anim_name:
			animated_sprite.play(anim_name)
	else:
		# Fallback to idle_down if animation doesn't exist
		if animated_sprite.sprite_frames.has_animation("idle_down"):
			animated_sprite.play("idle_down")

func get_facing_direction() -> Vector2:
	"""Returns the direction vector the player is facing"""
	match current_direction:
		Direction.DOWN:
			return Vector2.DOWN
		Direction.UP:
			return Vector2.UP
		Direction.LEFT:
			return Vector2.LEFT
		Direction.RIGHT:
			return Vector2.RIGHT
		_:
			return Vector2.DOWN

func get_facing_tile_position() -> Vector2i:
	"""Returns the tile position in front of the player"""
	var facing_dir = get_facing_direction()
	var tile_size = 16  # Assuming 16x16 tiles
	var check_position = global_position + (facing_dir * tile_size)
	return Vector2i(int(check_position.x / tile_size), int(check_position.y / tile_size))
