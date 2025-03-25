from picarx import Picarx
from time import sleep

px = Picarx()

px_power = 10
offset = 20

# Define threshold for detecting a line (based on observed values)
LINE_THRESHOLD = 200  # Adjust if needed based on testing

def get_status(val_list):
    """
    Determines lane position using grayscale sensor data.
    Assumes:
    - Left sensor detects yellow
    - Right sensor detects white
    - Middle sensor detects road (black)
    """
    left, middle, right = val_list  # Unpack sensor values

    left_detects_line = left > (LINE_THRESHOLD-50)    # Yellow line detected
    middle_detects_line = middle > LINE_THRESHOLD  # Off-track
    right_detects_line = right > LINE_THRESHOLD  # White line detected

    if not left_detects_line and not right_detects_line:
        return 'lost'  # Off both lines
    elif middle_detects_line and left_detects_line and right_detects_line:
        return 'stop line'
    elif left_detects_line:
        return 'too_left'  # Close to yellow, steer right
    elif right_detects_line:
        return 'too_right'  # Close to white, steer left
    elif middle_detects_line:
        return 'adjust'  # Middle sensor sees a line (drifted onto a boundary)
    else:
        return 'centered'  # Inside the lane, move forward

if __name__ == '__main__':
    try:
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("gm_val_list: %s, %s" % (gm_val_list, gm_state))

            if gm_state == 'centered':
                px.set_dir_servo_angle(0)
                px.forward(px_power)
            elif gm_state == 'too_left':  # Getting close to yellow line
                px.set_dir_servo_angle(-10)  # Steer right
                px.forward(px_power)
            elif gm_state == 'too_right':  # Getting close to white line
                px.set_dir_servo_angle(10)  # Steer left
                px.forward(px_power)
            elif gm_state == 'adjust':  # Middle sensor sees a line (off-track)
                px.set_dir_servo_angle(20)  # Steer left to correct
                px.forward(px_power)
            elif gm_state == 'stop line':
                sleep(2)
                px.forward(px_power)
            else:  # Lost both lines, reverse and turn
                #px.set_dir_servo_angle(-30)
                #px.backward(10)
                sleep(0.2)

    finally:
        px.stop()
        print("stop and exit")
        sleep(0.1)
