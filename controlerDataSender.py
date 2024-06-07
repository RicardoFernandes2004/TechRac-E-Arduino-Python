import serial
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# setup serial connection
ser = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # wait for connection to establish

# function to read potentiometer value
def read_pot_value():
    if ser.in_waiting > 0:
        try:
            raw_data = ser.readline().decode('utf-8').rstrip()
            pot_value = int(raw_data)
            return pot_value
        except Exception as e:
            print(f'error reading data: {e}')
            return None
    return None

# function to map potentiometer value to car speed
def map_pot_to_speed(pot_value):
    # assuming pot_value ranges from 0 to 1023
    # map this to a speed range of 0 to 200 (will be changed later when added the EEG sensor)
    return (pot_value / 1023) * 200

# plot
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = plt.plot([], [], 'ro', animated=True)

def init():
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 200)
    return ln,

def update(frame):
    pot_value = read_pot_value()
    if pot_value is not None:
        speed = map_pot_to_speed(pot_value)
        xdata.append(frame)
        ydata.append(speed)
        ln.set_data(xdata, ydata)
        ax.set_xlim(0, max(10, frame + 1))
        print(f'potentiometer value: {pot_value}, speed: {speed}')
    return ln,

ani = FuncAnimation(fig, update, frames=range(100), init_func=init, blit=True)
plt.xlabel('Time (s)')
plt.ylabel('Car Speed')
plt.title('Car Speed Simulation Using Potentiometer')
plt.show()
