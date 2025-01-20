import pygame as pg
import numpy as np
from math import pi, sin, cos
import cv2

# Constants
FPS = 30
DURATION = 15  # Total video duration in seconds
WIDTH = 720
HEIGHT = 1280
R = 250
MAP_WIDTH = 139
MAP_HEIGHT = 34
FILE_PATH = r"C:\Users\iederees\Desktop\earth_W140_H35.txt"

pg.init()
pg.font.init()

# Fonts
font_small = pg.font.SysFont("arial", 18)
font_large = pg.font.SysFont("arial", 36, bold=True)

# Load ASCII Earth data
with open(FILE_PATH, "r") as file:
    data = [file.read().replace("\n", "")]
ascii_chars = [char for line in data for char in line]
inverted_ascii_chars = ascii_chars[::-1]

# Classes for Projection and Object
class Projection:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.Surface((width, height))
        self.background = (10, 10, 60)
        self.surfaces = {}

    def addSurface(self, name, surface):
        self.surfaces[name] = surface

    def display(self, message=None):
        self.screen.fill(self.background)
        
        # Draw rotating ASCII Earth
        for surface in self.surfaces.values():
            i = 0
            for node in surface.nodes:
                text = inverted_ascii_chars[i]
                text_surface = font_small.render(text, False, (0, 255, 0))
                if MAP_WIDTH - 1 < i < (MAP_WIDTH * MAP_HEIGHT - MAP_WIDTH) and node[1] > 0:
                    self.screen.blit(
                        text_surface,
                        (WIDTH / 2 + int(node[0]), HEIGHT / 2 + int(node[2])),
                    )
                i += 1

        # Optional message overlay
        if message:
            text_surface = font_large.render(message, True, (255, 255, 255))
            text_rect = text_surface.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(text_surface, text_rect)

    def rotateAll(self, theta):
        for surface in self.surfaces.values():
            center = surface.findCentre()
            c = np.cos(theta)
            s = np.sin(theta)
            matrix = np.array([[c, -s, 0, 0], [s, c, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
            surface.rotate(center, matrix)


class Object:
    def __init__(self):
        self.nodes = np.zeros((0, 4))

    def addNodes(self, node_array):
        ones_column = np.ones((len(node_array), 1))
        ones_added = np.hstack((node_array, ones_column))
        self.nodes = np.vstack((self.nodes, ones_added))

    def findCentre(self):
        return self.nodes.mean(axis=0)

    def rotate(self, center, matrix):
        for i, node in enumerate(self.nodes):
            self.nodes[i] = center + np.matmul(matrix, node - center)


# Generate globe points
xyz = []
for i in range(MAP_HEIGHT + 1):
    lat = (pi / MAP_HEIGHT) * i
    for j in range(MAP_WIDTH + 1):
        lon = (2 * pi / MAP_WIDTH) * j
        x = round(R * sin(lat) * cos(lon), 2)
        y = round(R * sin(lat) * sin(lon), 2)
        z = round(R * cos(lat), 2)
        xyz.append((x, y, z))

# Video writer setup
video_name = "business_online_transformation.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
video = cv2.VideoWriter(video_name, fourcc, FPS, (WIDTH, HEIGHT))

# Animation Parameters
spin = 0
frame_count = FPS * DURATION
phase_duration = frame_count // 3  # Divide video into three phases

for frame in range(frame_count):
    pv = Projection(WIDTH, HEIGHT)
    globe = Object()
    globe.addNodes(np.array(xyz))
    pv.addSurface("globe", globe)

    # Phase 1: Rotating Earth with initial message
    if frame < phase_duration:
        message = "Your World, Your Business"
    # Phase 2: Interconnected globe
    elif frame < 2 * phase_duration:
        message = "Connecting Small Businesses Online"
    # Phase 3: Growth arrow and final message
    else:
        message = "Take Your Business Global with NEXTGENWEBS"

    pv.rotateAll(spin)
    pv.display(message)

    # Convert pygame surface to numpy array for OpenCV
    frame_surface = pg.surfarray.array3d(pv.screen)
    frame_surface = np.transpose(frame_surface, (1, 0, 2))  # Transpose to match OpenCV format
    frame_surface = cv2.cvtColor(frame_surface, cv2.COLOR_RGB2BGR)
    video.write(frame_surface)

    spin += 0.05

# Cleanup
video.release()
pg.quit()
