
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

print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
while True:
    user_input=input("enter directions (N,E,W,S) one by one blank enter show the results : ").strip().upper();
    if user_input == "":
        print("calculating final coordinates...");
        break;
    if user_input in ["N", "E", "W", "S"]:
        directions.append(user_input);
    else:
        print("invalid input only N,E,W,S are allowed");
final_coordinates = get_coordinates(directions);
print(f"final coordinates: {final_coordinates}");
