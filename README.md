# Event Collector

Status: Released (v2.9.1). Receives structured telemetry events from edge
services and validates them against registered schemas.

## Components

- `src/collector.py` - batching, retry and dead-letter handling.
- `src/schemas.py` - schema registration and validation.
