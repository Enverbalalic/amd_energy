from time import sleep

uJ_TO_J_FACTOR = 1000000;

last_value = 0

# energy17_input is the socket power file for a 7945HX
file = open("/sys/module/amd_energy/drivers/platform:amd_energy/amd_energy.0/hwmon/hwmon12/energy17_input", "r")

def get_joules():
    value = int(file.read()) / uJ_TO_J_FACTOR
    file.seek(0)
    return value;

last_value = get_joules();
sleep(1)

while True:
    value = get_joules();
    power_usage = round(value - last_value, 2)
    print(power_usage, end="")
    print("W")
    last_value = value
    sleep(1)
