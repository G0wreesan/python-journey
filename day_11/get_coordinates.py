
directions =[];

def get_coordinates(directions):
    x=0;
    y=0;
    for direction in directions:
        if direction == "N":
            y += 1;
        elif direction == "S":
            y -= 1;
        elif direction == "E":
            x += 1;
        elif direction == "W":
            x -= 1;
    return (x, y);

# example 
directions = ["N", "E", "S", "W", "N", "E"];
coordinates = get_coordinates(directions);
print(coordinates);  # Output: (1, 1)