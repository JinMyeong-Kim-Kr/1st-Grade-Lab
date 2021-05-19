from car import Car
import time
import RPi.GPIO as GPIO

class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)
        self.led_pinR = 37
        self.buzzer_pin = 8
        GPIO.setmode(GPIO.BOARD)
        
    def drive_parking(self):
        self.car.drive_parking()

    def car_startup(self):
        
        scale = [261.6, 293.6, 329.6, 349.2, 391.9, 440.0, 493.8, 523.2]

        while True:
            distance = self.car.distance_detector.get_distance()
            print(distance)
            if 3 <distance< 6:
                GPIO.setup(self.buzzer_pin, GPIO.OUT)
                try:
                    p = GPIO.PWM(self.buzzer_pin, 100)
                    p.start(3)     # start the PWM on 5% duty cycle

                    for i in range(8):
                        print (i + 1)
                        p.ChangeFrequency(scale[i])
                        time.sleep(0.5)

                    p.stop()  # stop the PWM output

                finally:
                                    
                    time.sleep(3.5)
                    self.car.steering.turn(60)
                    self.car.accelerator.go_forward(25)
                    time.sleep(3.5)
                    break            
        GPIO.setmode(GPIO.BOARD)   
        
        GPIO.setup(self.led_pinR, GPIO.OUT)
        while True:
            
            RGB_data = self.car.color_getter.get_raw_data()
            print(RGB_data)
            time.sleep(0.1)
            
            if RGB_data[0] < 100 and RGB_data[1] < 100 and RGB_data[2] < 100:
                GPIO.output(self.led_pinR, True)
                time.sleep(0.02)  # 500ms
            
            if RGB_data[0] > 100 or RGB_data[1] > 100 or RGB_data[2] >100:
                GPIO.output(self.led_pinR, False)

            if (self.car.line_detector.is_equal_status([0,1,1,1,0])):
                print("slow")
                self.car.accelerator.go_forward(20)
                time.sleep(0.1)
            
            elif (self.car.line_detector.is_equal_status([0, 0, 1, 1, 0])):
                    self.car.steering.turn_right(99)
                    self.car.accelerator.go_forward(35)
                    time.sleep(0.01)

            elif (self.car.line_detector.is_equal_status([1, 0, 0, 1, 1])):
                self.car.steering.turn_right(95)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 1, 1, 0, 1])):
                self.car.steering.turn_right(95)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 0, 1, 1, 1])):
                self.car.steering.turn_right(100)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 0, 0, 1, 0])):
                self.car.steering.turn_right(100)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 1, 1, 1, 1])):
                self.car.steering.turn_right(95)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 0, 0, 1, 1])):
                self.car.steering.turn_right(100)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 0, 1, 0, 1])):
                self.car.steering.turn_right(100)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 0, 0, 0, 1])):
                self.car.steering.turn_right(125)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 1, 1, 0, 0])):
                self.car.steering.turn_left(75)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 1, 1, 0, 0])):
                self.car.steering.turn_left(70)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 1, 0, 0, 0])):
                self.car.steering.turn_left(75)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 0, 1, 0, 0])):
                self.car.steering.turn_left(75)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 0, 0, 0, 0])):
                self.car.steering.turn_left(55)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 0, 1, 1, 0])):
                self.car.steering.turn_left(70)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 1, 1, 1, 0])):
                self.car.steering.turn_left(70)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 1, 0, 0, 1])):
                self.car.steering.turn_left(70)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 0, 0, 0, 0])):
                self.car.steering.turn_right(120)
                self.car.accelerator.go_backward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([0, 1, 0, 0, 0])):
                self.car.steering.turn_left(70)
                self.car.accelerator.go_forward(35)
                time.sleep(0.01)
            elif (self.car.line_detector.is_equal_status([1, 1, 1, 1, 1])):
                break
            else:
                time.sleep(0.01)

        self.car.accelerator.stop()



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
