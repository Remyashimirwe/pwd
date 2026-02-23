def process_readings(readings, *processors, **options):
    strict = options.get("strict", True)

    def iterator():
        for reading in readings:
            try:
                result = reading
                for func in processors:
                    result = func(result, **options)
                yield result
            except Exception:
                if strict:
                    raise
                # skip faulty reading
                continue

    return iterator()
def clean(r, **kwargs):
    return r.strip()

def to_float(r, **kwargs):
    return float(r)

def round_value(r, **kwargs):
    digits = kwargs.get("round_to", 2)
    return round(r, digits)
readings = [" 12.3456 ", " 9.8765 ", "bad_data", " 3.14159 "]

iterator = process_readings(
    readings,
    clean,
    to_float,
    round_value,
    strict=False,   # skip errors instead of stopping
    round_to=3      # pass to processing functions
)

for value in iterator:
    print(value)