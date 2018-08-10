from django.shortcuts import render, HttpResponse, redirect

def index(request):
    if 'total_spent' not in request.session:
        request.session['total_spent'] = 0
    if 'total_quantity' not in request.session:
        request.session['total_quantity'] = 0
    return render(request, 'store/index.html')

def process(request):
    request.session['price'] = 0
    request.session['product'] = request.POST.get('product_id')
    request.session['quantity'] = request.POST.get('quantity')
    if request.method == "POST":
        prices = {
            "1" : 19.99,
            "2" : 29.99,
            "3" : 4.99,
            "4" : 49.99
        }
        for key, value in prices.items():
            if request.session['product'] == key:
                request.session['price'] = value
        request.session['final_price'] = request.session['price'] * float(request.session['quantity'])
        request.session['total_spent'] += request.session['final_price']
        request.session['total_quantity'] += int(request.session['quantity'])
        return redirect('/amadon/checkout')
    else:
        return redirect('/')

def checkout(request):
    return render(request, 'store/checkout.html')