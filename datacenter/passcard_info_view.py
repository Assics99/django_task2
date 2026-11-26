from django.shortcuts import get_object_or_404, render
from django.utils.timezone import localtime

from datacenter.models import Passcard, Visit
from datacenter.visit_duration_tools import (
    format_duration,
    get_duration,
    is_visit_long,
)


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []
    for visit in visits:
        duration = get_duration(visit)
        this_passcard_visits.append({
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(duration),
            'is_strange': is_visit_long(visit),
        })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
