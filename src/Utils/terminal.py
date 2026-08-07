import sys
import time
import threading


def thinking_bar(stop_event):

    total = 20

    while not stop_event.is_set():

        for i in range(total + 1):

            if stop_event.is_set():
                break

            bar = "█" * i + "░" * (total - i)

            sys.stdout.write(
                f"\rMystique is thinking... [{bar}]"
            )
            sys.stdout.flush()

            time.sleep(0.04)

        for i in range(total, -1, -1):

            if stop_event.is_set():
                break

            bar = "█" * i + "░" * (total - i)

            sys.stdout.write(
                f"\rMystique is thinking... [{bar}]"
            )
            sys.stdout.flush()

            time.sleep(0.04)


def start_thinking():

    stop_event = threading.Event()

    thread = threading.Thread(
        target=thinking_bar,
        args=(stop_event,)
    )

    thread.start()

    return stop_event, thread