import pygame as pg
import numpy as np
from math import pi, sin, cos
import cv2  # For video saving

# Constants
FPS = 30
DURATION = 15  # seconds
WIDTH = 720  # 9:16 aspect ratio width
HEIGHT = 1280  # 9:16 aspect ratio height
R = 250
MAP_WIDTH = 139
MAP_HEIGHT = 34
FILE_PATH = r"C:\Users\iederees\Desktop\earth_W140_H35.txt"
CENTER_TEXT = "NEXTGENWEBS"

pg.init()
my_font = pg.font.SysFont('arial', 14)
center_font = pg.font.SysFont('arial', 36, bold=True)

# Load ASCII map data
with open(FILE_PATH, 'r') as file:
    data = [file.read().replace('\n', '')]

ascii_chars = [char for line in data for char in line]
inverted_ascii_chars = ascii_chars[::-1]

class Projection:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pg.Surface((width, height))
        self.background = (10, 10, 60)
        self.surfaces = {}

    def addSurface(self, name, surface):
        self.surfaces[name] = surface

    def display(self):
        self.screen.fill(self.background)
        
        # Draw ASCII Earth
        for surface in self.surfaces.values():
            i = 0
            for node in surface.nodes:
                text = inverted_ascii_chars[i]
                text_surface = my_font.render(text, False, (0, 255, 0))
                if MAP_WIDTH - 1 < i < (MAP_WIDTH * MAP_HEIGHT - MAP_WIDTH) and node[1] > 0:
                    self.screen.blit(text_surface, (WIDTH / 2 + int(node[0]), HEIGHT / 2 + int(node[2])))
                i += 1

        # Draw stationary "NEXTGENWEBS" text
        center_text_surface = center_font.render(CENTER_TEXT, True, (255, 255, 255))
        text_rect = center_text_surface.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(center_text_surface, text_rect)

    def rotateAll(self, theta):
        for surface in self.surfaces.values():
            center = surface.findCentre()
            c = np.cos(theta)
            s = np.sin(theta)
            matrix = np.array([[c, -s, 0, 0],
                               [s, c, 0, 0],
                               [0, 0, 1, 0],
                               [0, 0, 0, 1]])
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
video_name = "ascii_3d_earth_with_nextgenwebs.mp4"
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter(video_name, fourcc, FPS, (WIDTH, HEIGHT))

spin = 0
frame_count = FPS * DURATION
for _ in range(frame_count):
    pv = Projection(WIDTH, HEIGHT)
    globe = Object()
    globe.addNodes(np.array(xyz))
    pv.addSurface('globe', globe)
    pv.rotateAll(spin)
    pv.display()

    # Convert pygame surface to numpy array for OpenCV
    frame = pg.surfarray.array3d(pv.screen)
    frame = np.transpose(frame, (1, 0, 2))  # Transpose to match OpenCV format
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    video.write(frame)

    spin += 0.05

# Cleanup
video.release()
pg.quit()
