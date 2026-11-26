from django.shortcuts import render
from django.utils.timezone import localtime

from datacenter.models import Visit
from datacenter.visit_duration_tools import format_duration, get_duration


def storage_information_view(request):
    visits_in_storage = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visit in visits_in_storage:
        duration = get_duration(visit)
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': localtime(visit.entered_at),
            'duration': format_duration(duration),
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
