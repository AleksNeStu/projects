from tkinter import *
import time
import random
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(first: Point, second: Point):
    """Calculates the distance between two points."""
    return math.sqrt((second.x - first.x) ** 2 + (second.y - first.y) ** 2)


def center(points: []):
    """Calculates a point with the coordinates of the center of a set of points."""
    x = sum(p.x for p in points) / float(len(points))
    y = sum(p.y for p in points) / float(len(points))

    return Point(x, y)


def create_dot(canvas, point, thickness=6, color='black'):
    return canvas.create_oval(
        point.x - thickness / 2,
        point.y - thickness / 2,
        point.x + thickness / 2,
        point.y + thickness / 2,
        fill=color)


def create_line(canvas, first: Point, second: Point, color='black'):
    canvas.create_line(first.x, first.y, second.x, second.y, fill=color)


window = Tk()
window.geometry("600x600")
window.title("k-means demo")

canvas = Canvas(window, width=600, height=600)
canvas.pack()

# test points
# points = [Point(random.randint(1, 600), random.randint(1, 600)) for i in range(100)]
points = \
    *[Point(random.randint(1, 300), random.randint(1, 300)) for i in range(50)], \
    *[Point(random.randint(310, 600), random.randint(1, 300)) for i in range(50)], \
    *[Point(random.randint(310, 600), random.randint(310, 600)) for i in range(50)]

# random generated centroids
centroids = {
    'red': Point(random.randint(1, 600), random.randint(1, 600)),
    'green': Point(random.randint(1, 600), random.randint(1, 600)),
    'blue': Point(random.randint(1, 600), random.randint(1, 600))
}

# clusters
clusters = {}
for color, centroid in centroids.items():
    clusters[color] = []

while True:
    for color, cluster in clusters.items():
        if cluster:
            centroids[color] = center(cluster)
            cluster.clear()

    for point in points:
        color_of_nearest_centroid, nearest_centroid = min(
            centroids.items(), key=lambda item: distance(point, item
                                                         ))



        # min_distance = sys.maxsize
        # color_of_nearest_centroid = None
        #
        # for color, centroid in centroids.items():
        #     distance_to_centroid = distance(point, centroid)
        #     if distance_to_centroid < min_distance:
        #         min_distance = distance_to_centroid
        #         color_of_nearest_centroid = color

        clusters[color_of_nearest_centroid].append(point)

    # redraw
    canvas.delete("all")
    for point in points:
        create_dot(canvas, point)
    for color, centroid in centroids.items():
        create_dot(canvas, centroid, 8, color)
    for color, cluster in clusters.items():
        for point in cluster:
            create_line(canvas, point, centroids[color], color)
    window.update()
    time.sleep(0.5)

window.mainloop()