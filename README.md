# P1-IntroRPI

## Learned

1. Always first connect the ground wire
2. Always connect first to the 3.3 V pins
3. Use the [pinout command](https://gpiozero.readthedocs.io/en/stable/cli_tools.html) to display the pins number
    ```bash
    pinout
    ```
4. How to configure a gpio pin
    ```bash
    # Configure gpio 17
    echo 17 > /sys/class/gpio/export

    # If output then out, otherwise if input the in 
    echo out > /sys/class/gpio/gpio17/direction

    # Value = 1 --> ON or High ; 0 --> OFF or Low
    echo 1 > /sys/class/gpio/gpio17/value
    echo 0 > /sys/class/gpio/gpio17/value

    # Delete all the config we created
    echo 17 > /sys/class/gpio/unexport
    ```

5. All gpio pins are digital, if you want to use an analogic behaviour you need to implement it yourself ( in python )
6. Two different ways to define gpio pins numbers, Board and BCM
7. In Python you need to import the RPi.GPIO library to use Gpio pins
    ```python
    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BOARD) # Board mode, said above in 6.

    GPIO.setup(11,GPIO.OUT) # 11 = Pin number; Out = output, said above in 4.
    ```
8. For analogic behaviour you need to use pwm from GPIO library
    ```python
    pwm = GPIO.PWM (11,100) # 11 = Pin number; 100 = frequency (Hz)
    ```
9. Always remember to clean the gpio port before exiting
    ```python
    GPIO.cleanup()
    ```

## Led practise
### Purpose
This excercise purpose was to work as the starting point for the raspberry pi use.
In this practise we were told to light a LED with an analogic behaviour.

### Observations
The LED turned on with a vey weak light and it did't seem to work in an analogic way, because the light never seemed to vary.