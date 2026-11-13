"""Minimal schema registry used by the event collector."""

REQUIRED_FIELDS = {
    "page_view": {"user_id", "path", "ts"},
    "purchase": {"user_id", "amount", "currency", "ts"},
}


def validate(kind, payload):
    required = REQUIRED_FIELDS.get(kind)
    if required is None:
        return False
    return required.issubset(payload.keys())
