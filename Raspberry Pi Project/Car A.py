#########################################################################
# Date: 2018/10/02
# file name: 3rd_assignment_main.py
# Purpose: this code has been generated for the 4 wheel drive body
# moving object to perform the project with line detector
# this code is used for the student only
#########################################################################

from car import Car
import time


class myCar(object):

    def __init__(self, car_name):
        self.car = Car(car_name)

    def drive_parking(self):
        self.car.drive_parking()

    # =======================================================================
    # 3RD_ASSIGNMENT_CODE
    # Complete the code to perform Third Assignment
    # =======================================================================
    def car_startup(self):
        
        cnt = 0

        #while True:
        #    RGB_data = self.car.color_getter.get_raw_data()
        #    print(RGB_data)
        
        while True:
            record = self.car.line_detector.read_digital()
            RGB_data = self.car.color_getter.get_raw_data()
            #print(RGB_data)
            self.car.accelerator.go_forward(30)


            if (300 < RGB_data[0] <800) and (200 < RGB_data[1] <280) and (210 < RGB_data[2] <290):
                print("@@@@@@@@@@@END@@@@@@@@@@@")
                print(RGB_data[0],RGB_data[1],RGB_data[2])
                self.car.steering.turn(90)
                self.car.accelerator.go_forward(30)
                time.sleep(2.5)
                self.car.accelerator.stop()
                self.car.steering.turn(90)
                break
            
            elif record == [0,0,0,0,0]:
                self.car.steering.turn(120)
                self.car.accelerator.go_backward(30)
                time.sleep(0.4)
                self.car.steering.turn(60)
                self.car.accelerator.go_forward(30)
                time.sleep(0.2)
            elif record == [1,0,0,0,0]:
                self.car.steering.turn(60)
            elif record == [0,1,0,0,0]:
                self.car.steering.turn(75)
            elif record == [0,0,1,0,0]:
                self.car.steering.turn(90)
            elif record == [0,0,0,1,0]:
                self.car.steering.turn(105)
            elif record == [0,0,0,0,1]:
                self.car.steering.turn(120)
            elif record == [1,1,0,0,0]:
                self.car.steering.turn(60)
            elif record == [0,1,1,0,0]:
                self.car.steering.turn(75)
            elif record == [0,0,1,1,0]:
                self.car.steering.turn(105)
            elif record == [0,0,0,1,1]:
                self.car.steering.turn(120)
            
            elif cnt ==0:
                if record == [1,1,1,1,1]:
                    cnt += 1
                    self.car.accelerator.stop()
                    time.sleep(0.5)
                
                    self.car.steering.turn(120)
                    self.car.accelerator.go_forward(30)
                    time.sleep(4.0)
                    self.car.accelerator.stop()
                    time.sleep(0.5)
                    self.car.steering.turn(60)
                    self.car.accelerator.go_backward(30)
                    time.sleep(1.1)

                    self.car.steering.turn(90)
                    time.sleep(1.3)

                    self.car.accelerator.stop()
                    time.sleep(1.0)

                    self.car.steering.turn(60)
                    self.car.accelerator.go_forward(25)
                    time.sleep(0.7)
                    print(cnt)

            

                    
                
            



if __name__ == "__main__":
    try:
        myCar = myCar("CarName")
        myCar.car_startup()

    except KeyboardInterrupt:
        # when the Ctrl+C key has been pressed,
        # the moving object will be stopped
        myCar.drive_parking()
