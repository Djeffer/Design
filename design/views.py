from django.shortcuts import render
from .models import DesignSlid
from price.models import PriceCard
from yawn.models import Order
from yawn.forms import OrderForm
from bottelegram.sendmessage import send_tg


def design_page(request):
    img_port = DesignSlid.objects.all()
    form = OrderForm()
    price_table = PriceCard.objects.all()
    dict_odj = {
        'img_port': img_port,
        'price_table': price_table,
        'form': form,
    }
    return render(request, 'design/index.html', dict_odj)


def price_page(request):
    return render(request, 'design/price.html')


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        city = request.POST['city']
        element = Order(order_name=name, order_phone=phone, order_city=city)
        element.save()
        send_tg(tg_name=name, tg_phone=phone, tg_city=city)
        return render(request, 'design/thanks.html', {'name': name})
    else:
        return render(request, 'design/thanks.html')


def works_page(request):
    return render(request, 'design/works.html')
