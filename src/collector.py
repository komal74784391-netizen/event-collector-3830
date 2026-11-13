"""Batching collector for structured telemetry events."""

import json


class Collector:
    def __init__(self, batch_size=500):
        self.batch_size = batch_size
        self._buffer = []
        self._dead_letter = []

    def add(self, event):
        try:
            json.dumps(event)
        except TypeError:
            self._dead_letter.append(event)
            return
        self._buffer.append(event)
        if len(self._buffer) >= self.batch_size:
            self.flush()

    def flush(self):
        batch, self._buffer = self._buffer, []
        return batch

    @property
    def dead_letter(self):
        return list(self._dead_letter)
