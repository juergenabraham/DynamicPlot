#!/bin/env  python3

class MetaSensor:
    def __init__(self, kwargs):
        self.state = False
        self.set_state(kwargs['state'])
        self.data = list()

    def set_state(self, state):
        self.state = True if state is not None else False

    def get_state(self):
        return self.state

    def _get_data_from_sensor(self):
        pass
