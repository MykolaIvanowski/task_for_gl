FIRE_WARNING = "fire_warning"
EARTHQUAKE_WARNING = "earthquake_warning"


class AlarmNotifier:

    def __init__(self, warnings):
        self.alarm_system = {warning: dict() for warning in warnings}

    def register_system(self, warning, system, notify=None):
        if notify is None:
            notify = getattr(system, "alarm")
        self.alarm_system[warning][system] = notify

    def unregister_system(self, system):
        del self.alarm_system[system]

    def notify_alarm(self, warning, message):
        for notify in self.alarm_system[warning].values():
            notify(message)


class VisualSignal:
    def alarm(self, message):
        print(f"{message}! Turn on the visual alarm")


class SoundAlert:
    def alarm(self, message):
        print(f"{message}! Turn on the audible alarm")


class EmergencyFire:
    def alarm(self, message):
        print(f"{message}! Call to firefighter")


def fire_sensor(alarm):
    alarm.notify_alarm(FIRE_WARNING, "Fire")


def earthquake_sensor(alarm):
    alarm.notify_alarm(EARTHQUAKE_WARNING, "Earthquake")


if __name__ == "__main__":

    alarm_notifier = AlarmNotifier([FIRE_WARNING, EARTHQUAKE_WARNING])

    visual_system = VisualSignal()
    sound_system = SoundAlert()
    emergency_firefighter = EmergencyFire()

    alarm_notifier.register_system(FIRE_WARNING, visual_system)
    alarm_notifier.register_system(FIRE_WARNING, sound_system)
    alarm_notifier.register_system(EARTHQUAKE_WARNING, visual_system)
    alarm_notifier.register_system(EARTHQUAKE_WARNING, sound_system)
    alarm_notifier.register_system(FIRE_WARNING, emergency_firefighter)

    fire_sensor(alarm_notifier)
    earthquake_sensor(alarm_notifier)
