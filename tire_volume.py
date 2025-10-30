#Improvements: I created a separate file with the calculation so I can simply call the function later.
#Improvements: 
import datetime
import math

tire_width = float(input(f"Enter the width of the tire in mm: "))
aspect_ratio = float(input(f"Enter the aspect ratio of the tire: "))
diameter_inches = float(input(f"Enter the diameter of the wheel in inches: "))


volumes = (math.pi * tire_width**2 * aspect_ratio * (tire_width * aspect_ratio + 2540 * diameter_inches)) / 10000000000


#improvements:
if volumes <= 35:
    print(f"Volume of the tire is {volumes:.2f} liters, so the recommended pressure is '30-33 psi'.")
elif 36 <= volumes <= 45:
    print(f"Volume of the tire is {volumes:.2f} liters, so the recommended pressure is '34-37 psi'.")
elif 46 >= volumes <= 55:
    print(f"Volume of the tire is {volumes:.2f} liters, so the recommended pressure is '38-41 psi'.")
else:
    print(f"Volume of the tire is {volumes:.2f} liters, so the recommended pressure is '42-48 psi'.")
current_date = datetime.datetime.today().strftime("%d/%m/%y")

line = (
    f"{current_date}, "
    f"{tire_width: .0f}, "
    f"{aspect_ratio: .0f}, "
    f"{diameter_inches: .0f},"
    f"{volumes: .2f}\n"
)


with open("volumes.txt", "at") as volumes_file:
    volumes_file.write(line)
