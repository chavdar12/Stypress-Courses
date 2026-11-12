import math

G = 9.81


class Projectile:
    def __init__(self, mass, x):
        self.mass = mass
        self.x = x
        self.y = 0.0
        self.vx = self.vy = 0.0

    def move(self, t):
        self.x += self.vx * t
        self.y += self.vy * t - G * t * t / 2
        self.vy -= G * t
        if self.y < 0:
            self.y = 0.0

    def shoot(self, angle, velocity, step=0.1):
        alpha = math.radians(angle)
        self.vx = velocity * math.cos(alpha)
        self.vy = velocity * math.sin(alpha)
        points = [(self.x, self.y)]
        while True:
            self.move(step)
            points.append((self.x, self.y))
            if self.y == 0:
                return points


# 45 degrees, 10 m/s: flight time ~1.44 s, range ~10.2 m
path = Projectile(1, 0).shoot(45, 10)
assert path[-1][1] == 0 and 9.5 < path[-1][0] < 11

if __name__ == "__main__":
    projectile = Projectile(float(input("Mass: ")), 0)
    angle = float(input("Angle (degrees): "))
    velocity = float(input("Initial velocity: "))
    print("x;y")  # semicolon-separated, ready for a spreadsheet
    for x, y in projectile.shoot(angle, velocity):
        print(f"{x:.3f};{y:.3f}")
