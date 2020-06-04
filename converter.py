from kml_temp import top, bottom, placemark_path, placemark_point


text_file = input("Enter full filename here >>> ")
trash_lines = int(input("Specify the line where you want to start converting (Recommended: 300) >>> "))
accuracy = int(input("Enter stepsize in sec >>> "))
stop_line = int(input("Enter line to stop converting >>> "))

lines = [(0,0,0)]
with open(text_file, "r") as file:
    for i, line in enumerate(file):
        if i%accuracy == 0 and i>trash_lines and i<= stop_line: #the first lines are always trash
            sl = line.strip().split(";")
            gx, gy, time= int(sl[3])/10000000, int(sl[4])/10000000, sl[-4]
            if (lines[-1][0],lines[-1][1]) != (gy, gx):
                lines.append((gy, gx, time))
            else:
                print("Ignoring Point due to equality of ccordinates")

lines.pop(0)

path_coords = ""
points = []

for coord in lines:
    path_coords += f"{coord[0]},{coord[1]},0 \n"
    points.append((f"{coord[0]},{coord[1]},0", coord[2]))
    print(coord)

points_kml = []
for point in points:
    points_kml.append(placemark_point.format(coords=point[0], name=point[1]))

path = placemark_path.format(coords = path_coords)

result = top
for point in points_kml:
    result += point

result += path
result += bottom

with open("result.kml", "w") as file:
    file.write(result)

