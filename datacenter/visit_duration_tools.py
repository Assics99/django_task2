from django.utils.timezone import localtime

SECONDS_IN_MINUTE = 60
SECONDS_IN_HOUR = 3600


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if visit.leaved_at:
        return localtime(visit.leaved_at) - entered_at
    return localtime() - entered_at


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    seconds = total_seconds % SECONDS_IN_MINUTE
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * SECONDS_IN_MINUTE
