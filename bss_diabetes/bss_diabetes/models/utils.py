def parse_int(value, default=None):
    try:
        return int(value)
    except ValueError:
        return default
