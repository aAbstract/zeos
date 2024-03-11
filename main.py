from machine import Pin, Timer  # type: ignore


led_state = True
led = Pin(23, Pin.OUT)
led.value(led_state)
timer = Timer(0)


def timer_callback(_):
    global led_state

    led_state = not led_state
    led.value(led_state)
    print(f"led_state={led_state}")


timer.init(freq=1, mode=Timer.PERIODIC, callback=timer_callback)
