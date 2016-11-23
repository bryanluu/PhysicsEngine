import math

class Vector2D:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector2D(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __eq__(self, other):
        if isinstance(other, Vector2D):
            return (self.x == other.x) and (self.y == other.y)
        elif isinstance(other, list):
            return (self.x == other[0]) and (self.y == other[1])
        else:
            return False

    def __neg__(self):
        return Vector2D(-self.x, -self.y)

    # Scalar operations, other must be a scalar
    def __mul__(self, other):
        return Vector2D(other * self.x, other * self.y)

    def __div__(self, other):
        return Vector2D(self.x.__truediv__(other), self.y.__truediv__(other))

    def __rmul__(self, other):
        return Vector2D(other * self.x, other * self.y)

    def __str__(self):
        return str([self.x, self.y])

    def __repr__(self):
        return [self.x, self.y]

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def angle(self):
        """
        Returns the angle, measured as 0 radians from x-axis, in radians
        """

        if self.x == 0:
            return math.pi/2 if self.y > 0 else -math.pi/2

        if self.y == 0:
            return 0 if self.x > 0 else math.pi

        angle = math.atan2(self.y, self.x)

        return angle

    @staticmethod
    def create_from_angle(angle, length):
        """
        Creates a vector according to the angle and length of the vector.
        Angle: an angle in radians, where the angle is measured from 0 on the x-axis,
        and angle goes from -180 (on the bottom) to +180 (on the top).
        Length: must be a scalar number
        """
        # convert to radians
        x = length * math.cos(angle)
        y = length * math.sin(angle)
        return Vector2D(x, y)

    @staticmethod
    def zero():
        return Vector2D(0, 0)

    @staticmethod
    def dot(v1, v2):
        """
        Calculates the vector scalar product (dot product) of v1 and v2.
        :param v1: Vector V1
        :param v2: Vector V2
        :return: Dot Product of the Vectors
        """
        return v1.x * v2.x + v1.y * v2.y

    @staticmethod
    def angle_between(v1, v2):
        """
        Finds the angle of v2 w.r.t to v1.
        :param v1: Reference vector to measure angle to
        :param v2: Vector to measure angle of w.r.t v1
        :return: Angle between the two vectors, where 0 means they point in the same direction
        -90 means v2 points to the west of v1, etc. 0 is returned if either is a zero vector.
        """
        if v1 == Vector2D.zero() or v2 == Vector2D.zero():
            return 0
        # Use dot product to find angle
        angle = math.acos(Vector2D.dot(v1, v2) / (v1.length() * v2.length()))

        v1_angle = v1.angle()
        v2_angle = v2.angle()

        if v1_angle >= 0:
            if v2_angle < v1_angle:
                return -angle if v2_angle > v1_angle - math.pi else angle
            else:
                return angle
        else:
            if v2_angle > v1_angle:
                return angle if v2_angle <= v1_angle + math.pi else -angle
            else:
                return -angle