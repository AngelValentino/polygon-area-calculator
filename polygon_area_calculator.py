class Rectangle:
    def __init__(self, width, height):
        # Initializes a Rectangle object with width and height.
        self.width = width
        self.height = height
        # Stores the class name (Rectangle or Square)
        self.class_name = self.__class__.__name__

    # Returns a formatted string representation of the object.
    def __str__(self):
        formatted_str = self.class_name

        # Check if the rectangle is a square or not and format accordingly
        if not self.is_square():
            formatted_str += f'(width={self.width}, height={self.height})'
        else:
            formatted_str += f'(side={self.width})' # If it's a square, show side length
        
        return formatted_str

    def is_square(self):
        # Checks if the shape is a square by comparing its class name
        return self.class_name == 'Square'
    
    # Sets the width of the rectangle. If it's a square, sets both width and height to the same value
    def set_width(self, width):
        self.width = width
        if self.is_square():  # If it's a square, height should be updated as well
            self.height = width
    
    # Sets the height of the rectangle. If it's a square, sets both width and height to the same value
    def set_height(self, height):
        self.height = height
        if self.is_square():  # If it's a square, width should be updated as well
            self.width = height

    # Returns the area of the rectangle
    def get_area(self):
        return self.width * self.height

    # Returns the perimeter of the rectangle
    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    # Returns the length of the diagonal using the Pythagorean theorem
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    # Returns a string representation of the shape with stars, limited to width/height <= 50
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        formatted_rect_picture = ''

        # Generate the picture line by line
        for _ in range(self.height):
            formatted_rect_picture += '*' * self.width + '\n'

        # Return the generated rectangle picture
        return formatted_rect_picture
    
    # Returns the number of times the other rectangle could fit inside the current one
    def get_amount_inside(self, other):
        other_fit_count = 0 # Initialize fit count
        self_area = self.get_area()
        other_area = other.get_area()

        # Subtract the area of the 'other' rectangle as long as it fits inside 'self'
        while self_area >= other_area:
            self_area -= other_area
            other_fit_count += 1

        return other_fit_count

class Square(Rectangle):
    def __init__(self, side):
        # Initializes a Square object, inheriting from Rectangle (side is both width and height)
        super().__init__(side, side)

    # Sets both the width and height of the square to the same value
    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)

rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_area())
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())
print(rect.get_amount_inside(sq))