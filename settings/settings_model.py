from pydantic import BaseModel

class GeneralSettings(BaseModel):
    fps: int = 60
    screen_width: int = 1280
    screen_height: int = 720
    fullscreen: bool = False
    fixed_timestep: bool = True

class PhysicsSettings(BaseModel):
    max_speed: float = 12.0
    acceleration: float = 0.2
    deceleration: float = 0.1
    braking_force: float = 0.3
    reverse_speed: float = -4.0

class DriftSettings(BaseModel):
    drift_factor: float = 0.96
    grip_factor: float = 0.88
    steering_speed: float = 3.0
    max_steering_angle: float = 35.0

class HandlingSettings(BaseModel):
    traction_control: bool = True
    steering_assist: bool = False
    steering_return_speed: float = 2.0

class AudioSettings(BaseModel):
    enable_audio: bool = True
    engine_volume: float = 0.7
    sfx_volume: float = 0.8
    music_volume: float = 0.6

class VisualSettings(BaseModel):
    show_speedometer: bool = True
    show_minimap: bool = True
    show_drift_meter: bool = True
    camera_zoom: float = 1.0
    camera_follow_delay: float = 0.1

class MapSettings(BaseModel):
    friction: float = 0.98
    offroad_friction: float = 0.85
    grass_slowdown: float = 0.5
    weather_enabled: bool = False
    night_mode: bool = False
    laps_required: int = 3
    countdown_seconds: int = 3
    drift_score_multiplier: float = 1.5

class DebugSettings(BaseModel):
    debug_mode: bool = False
    draw_physics_debug: bool = False

class InputSettings(BaseModel):
    use_gamepad: bool = True
    deadzone: float = 0.1
    invert_steering: bool = False
    sensitivity: float = 1.0

class Settings(BaseModel):
    general: GeneralSettings = GeneralSettings()
    physics: PhysicsSettings = PhysicsSettings()
    drift: DriftSettings = DriftSettings()
    handling: HandlingSettings = HandlingSettings()
    audio: AudioSettings = AudioSettings()
    visuals: VisualSettings = VisualSettings()
    map: MapSettings = MapSettings()
    debug: DebugSettings = DebugSettings()
    input: InputSettings = InputSettings()
