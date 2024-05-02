from .models import ExchangeRate
from django.http import JsonResponse


def exchange_rate(request):
    if request.method == 'GET':
        charcode = request.GET.get('charcode')
        date = request.GET.get('date')
        if charcode and date:
            data = ExchangeRate.objects.filter(charcode=charcode, date=date)
        elif charcode:
            data = ExchangeRate.objects.filter(charcode=charcode)
        elif date:
            data = ExchangeRate.objects.filter(date=date)
        else:
            data = ExchangeRate.objects.all()
        data = list(data.values('charcode', 'date', 'rate'))
        return JsonResponse(data, safe=False)
