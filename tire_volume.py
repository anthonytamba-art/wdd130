import datetime
# Get the current date
current_date = datetime.datetime.now()
width = int(input("Enter the width of the tire in mm (ex 205): ") )
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): ") )
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): ") )

# Calculate the volume of the tire
volume = (3.14159 * (width ** 2) * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000
print(f"The approximate volume is {volume:.2f} liters")

# Get the current date
current_date = datetime.datetime.now() 
print(f"Current date: {current_date.strftime('%Y-%m-%d')}")

# Append data to volumes.txt
with open("volumes.txt", "at") as file:
    file.write(f"{current_date.strftime('%Y-%m-%d')}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}\n")
print(
    f"Data appended to volumes.txt"
f"aspect_ratio: {aspect_ratio}, diameter: {diameter}, volume: {volume:.2f} liters")
