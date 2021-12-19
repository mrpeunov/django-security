from case2_2.models import SupportServiceTicket
from django.http import JsonResponse


def create_post(request):
    text = request.POST.get("text")
    file = request.FILES.get("file")

    SupportServiceTicket.objects.create(text=text, file=file)

    return JsonResponse({"ok": True}, status=201)
