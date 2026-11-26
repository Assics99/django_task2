from django.utils.timezone import localtime


def get_duration(visit):
    entered_at = localtime(visit.entered_at)
    if visit.leaved_at:
        return localtime(visit.leaved_at) - entered_at
    return localtime() - entered_at


def format_duration(duration):
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'


def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60
