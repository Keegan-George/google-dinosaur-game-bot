DINOSAUR_GAME_URL = "https://elgoog.im/dinosaur-game/"

# Tolerance level over which the current pixel colour must differ from the background colour to detect an obstacle
TOLERANCE = 5

# Arbitrary empty region of the game screen where the background colour is captured
BACKGROUND_COLOUR_COORDINATE = (70, 1000)

# x and y ranges within which to check for an obstacle
OBSTACLE_DETECTION_RANGE_X = range(570, 610, 10)
OBSTACLE_DETECTION_RANGE_Y = range(800, 890, 10)
