import json

unique_coordinates = {"(0,0)": 1} # "(0,0) holds a different value for Part 2"

# Part 1

with open("./2015/Day 3/data.txt", "r") as f:
    line = f.readline()
    coordinates = [0,0]
    for character in line:
        if character == ">":
            coordinates = [coordinates[0] + 1, coordinates[1]]
        elif character == "<":
            coordinates = [coordinates[0] - 1, coordinates[1]]
        elif character == "^":
            coordinates = [coordinates[0], coordinates[1] + 1]
        elif character == "v":
            coordinates = [coordinates[0], coordinates[1] - 1]

        if f"({coordinates[0]},{coordinates[1]})" in unique_coordinates:
            unique_coordinates[f"({coordinates[0]},{coordinates[1]})"] += 1
        else:
            unique_coordinates[f"({coordinates[0]},{coordinates[1]})"] = 1    

with open("./2015/Day 3/coordinates.json", "r") as f:
    data = json.load(f)

    data["Part 1"] = unique_coordinates

with open("./2015/Day 3/coordinates.json", "w") as f:  
    json.dump(data, f, indent = 4)  

print(f"Final coordinate: ({coordinates[0]}, {coordinates[1]})")
print(f"Houses that received at least 1 present: {len(unique_coordinates)}\n")


# Part 2

unique_coordinates = {"(0,0)": 1}

with open("./2015/Day 3/data.txt", "r") as f:
    line = f.readline()
    santa_coordinates = [0,0]
    robo_coordinates = [0,0]
    done = 1
    while done < len(line):
        character = line[done - 1:done]
        if done % 2 == 0:
            if character == ">":
                santa_coordinates = [santa_coordinates[0] + 1, santa_coordinates[1]]
            elif character == "<":
                santa_coordinates = [santa_coordinates[0] - 1, santa_coordinates[1]]
            elif character == "^":
                santa_coordinates = [santa_coordinates[0], santa_coordinates[1] + 1]
            elif character == "v":
                santa_coordinates = [santa_coordinates[0], santa_coordinates[1] - 1]

            if f"({santa_coordinates[0]},{santa_coordinates[1]})" in unique_coordinates:
                unique_coordinates[f"({santa_coordinates[0]},{santa_coordinates[1]})"] += 1
            else:
                unique_coordinates[f"({santa_coordinates[0]},{santa_coordinates[1]})"] = 1  

        else:
            if character == ">":
                robo_coordinates = [robo_coordinates[0] + 1, robo_coordinates[1]]
            elif character == "<":
                robo_coordinates = [robo_coordinates[0] - 1, robo_coordinates[1]]
            elif character == "^":
                robo_coordinates = [robo_coordinates[0], robo_coordinates[1] + 1]
            elif character == "v":
                robo_coordinates = [robo_coordinates[0], robo_coordinates[1] - 1]

            if f"({robo_coordinates[0]},{robo_coordinates[1]})" in unique_coordinates:
                unique_coordinates[f"({robo_coordinates[0]},{robo_coordinates[1]})"] += 1
            else:
                unique_coordinates[f"({robo_coordinates[0]},{robo_coordinates[1]})"] = 1

        done += 1

with open("./2015/Day 3/coordinates.json", "r") as f:
    data = json.load(f)

    data["Part 2"] = unique_coordinates

with open("./2015/Day 3/coordinates.json", "w") as f:  
    json.dump(data, f, indent = 4) 

print(f"Santa's final coordinate: ({santa_coordinates[0]}, {santa_coordinates[1]})")
print(f"Robo's final coordinate: ({robo_coordinates[0]}, {robo_coordinates[1]})")
print(f"Houses that received at least 1 present: {len(unique_coordinates)}")