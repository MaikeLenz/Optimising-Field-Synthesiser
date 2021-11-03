from zaber_motion import Library
from zaber_motion.ascii import Connection
from zaber_motion import Units


Library.enable_device_db_store()
with Connection.open_serial_port("COM3") as connection:
    device_list = connection.detect_devices()
    print("Found {} devices".format(len(device_list)))

    device = device_list[0]

    axis = device.get_axis(1)
    axis.home()
    # Move to the 10mm position
    axis.move_absolute(10, Units.LENGTH_MILLIMETRES)
    # Move by an additional 5mm
    axis.move_relative(5, Units.LENGTH_MILLIMETRES)