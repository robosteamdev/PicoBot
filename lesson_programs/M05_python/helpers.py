"""My helper functions for PicoBot planning."""


def travel_time(distance_cm, speed_cm_s=25):
    return distance_cm / speed_cm_s


def average(values):
    return sum(values) / len(values)
