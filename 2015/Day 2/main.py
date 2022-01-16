from numpy import prod
import os

print(os.getcwd())

def surface_area(l, w, h):
    return 2*l*w + 2*w*h + 2*h*l

def smallest_face(l, w, h):
    array = [l*w, w*h, h*l]
    array.sort()
    return array[0]

def smallest_perimeter(l, w, h):
    array = [l, w, h]
    array.sort()
    return 2*array[0] + 2*array[1]

def wrapping_paper(file):
    with open(file, "r") as f:
        paper = 0
        while True:
            line = f.readline().rstrip("\n")
            if file != "data.txt":
                print(line)
                if line != "":
                    measurements = line.split("x")
                    print(measurements)
                    measurements_array = [int(i) for i in measurements]
                    print(measurements_array)
                    measurements_array.sort()
                    print(measurements_array)
                    paper += surface_area(measurements_array[0], measurements_array[1], measurements_array[2]) + smallest_face(measurements_array[0], measurements_array[1], measurements_array[2])
                else:
                    return f"Wrapping paper to order: {paper} ft"
            else:
                if line != "":
                    measurements = line.split("x")
                    measurements_array = [int(i) for i in measurements]
                    measurements_array.sort()
                    paper += surface_area(measurements_array[0], measurements_array[1], measurements_array[2]) + smallest_face(measurements_array[0], measurements_array[1], measurements_array[2])
                else:
                    return f"Wrapping paper to order: {paper} ft"    

def ribbon(file):
    with open(file, "r") as f:
        ribbon = 0
        while True:
            line = f.readline().rstrip("\n")
            if file != "data.txt":
                print(line)
                if line != "":
                    measurements = line.split("x")
                    print(measurements)
                    measurements_array = [int(i) for i in measurements]
                    print(measurements_array)
                    measurements_array.sort()
                    print(measurements_array)
                    ribbon += prod(measurements_array) + smallest_perimeter(measurements_array[0], measurements_array[1], measurements_array[2])
                else:
                    return f"Ribbon to order: {ribbon} ft"
            else:
                if line != "":
                    measurements = line.split("x")
                    measurements_array = [int(i) for i in measurements]
                    measurements_array.sort()
                    ribbon += prod(measurements_array) + smallest_perimeter(measurements_array[0], measurements_array[1], measurements_array[2])
                else:
                    return f"Ribbon to order: {ribbon} ft"        

filename = "./Day 2/data.txt"

print(wrapping_paper(filename))
print(ribbon(filename))