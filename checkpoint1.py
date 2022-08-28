# Sophia Masrour    sim7mfv

# Game Summary: The user will play as a character attempting to escape haunted house. There will be multiple levels
# of increasing difficulty, and each level will be a different room of the haunted house. The player will start at one
# corner of the screen and attempt to reach the exit of the room. There will be a count down timer in which the player
# must exit the room in the allotted time in order to move onto the next level. The player will also have three "hearts"
# at the start of each level and will "die" if they lose all three before reaching the exit of the level. There will be
# various enemies such as ghosts and other themed enemies that if the player were to touch would remove a heart from
# their health bar. The player will be animated and from a sprite sheet in order to match the theme of the game. The
# enemies will also be from a sprite sheet and will be themed as well (ghosts, skeletons, vampires, etc.). There will be
# a scrolling level so the player will not see the entire room until the player progresses through the level. There will
# also be an inter-session progress report in which the high score (the fastest time) the player was able to complete a
# certain level will be made available to them prior and after completing/failing a level.

# REQUIRED FEATURES :

# User Input : the player will move the character by pressing on the left and right arrow keys. The player will be able
# to make the character jump by pressing the space bar. To move past the introduction screen to each level the player
# will simply have to press the space bar. At this point in the game design process I see no need for mouse clicks.

# Graphics / Images : The game will be themed like a haunted house. The player will use a character from a sprite sheet
# that will be a person trying to escape each room of the haunted house. The enemies will follow this theme and will be
# ghosts, vampires, skeletons, etc. Each level will be constructed to appear like a haunted house as well, so the colors
# will be dark.

# Start Screen : The start screen will follow the theme of the game and will include dark colors and a message about
# the premise of the game. This will include the name of the game and the instructions as well. My name and student id
# will also appear in this screen.

# Small Enough Window : The size of my window will most likely be the largest available to us, which will be
# gamebox.Camera(800, 600). This will be to ensure that I have ample space to maintan the theme of the game in the
# graphics of each level.


# OPTIONAL FEATURES :

# Animation : The movable character the player will use to navigate each level will be taken from a sprite sheet.
# The enemies in the game will also be taken from a sprite sheet, and will match the theme of the game by being various
# monsters and ghosts.

# Enemies : There will be various moving enemies in each level. If the player comes into contact with these enemies,
# they will lose one of their three hearts from the health bar. If they come into contact with three of these enemies,
# they will "die" and have to restart the level.

# Scrolling Level : The camera will not show the entirety of the level, and as the player moves the camera will center
# on the player and show more of the level/room as the player navigates towards the exit/end of the level.

# Timer : Each level will also have a timer in which the player must complete the level in the allotted time or else
# they must restart. I have not determined what this allotted time will be. This will be one of my last decisions since
# I will have to play the finished product of the game before deciding on an appropriate amount of time to be allowed. I
# do plan on perhaps decreasing the amount of time for each level as the difficulty increased, but I am still unsure.

# Health Bar : There will be a health bar at the top corner of the screen at all times. The default health will be three
# hearts. This will decrease as the player comes into contact with the moving enemies. Each contact will result in the
# loss of one heart. If the player loses all three hearts they will "die" and have to restart the level.

# Multiple Levels : There will be multiple levels in this game. Each level will be a different room of the haunted
# house. The end of the game will be once the player is able to complete the most difficult level and exit the final
# room of the haunted house which will free them from the house. Each level will increase in difficulty and complexity.

# Inter-Session Progress : The fastest time the player was able to complete a certain level will be saved and displayed
# following the completion or failure of each level. I am considering having a separate screen in which all the
# unlocked levels are listed so they can be replayed as many times as the player wants without going through all the
# levels. If I do this then beside each level the fastest time will be displayed.