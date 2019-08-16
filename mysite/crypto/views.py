from django.shortcuts import render

# Create your views here.


def home(request):
    import requests
    import json

    # Grab Crypto Data
    price_request = requests.get(
        "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD")
    price = json.loads(price_request.content)

    # Grab Crypto News
    api_request = requests.get(
        "https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)
    return render(request, 'crypto/home.html', {'api': api, 'price': price})


def prices(request):
    if request.method == 'POST':
        import requests
        import json
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get(
            "https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD")
        crypto = json.loads(crypto_request.content)
        return render(request, 'crypto/prices.html', {'quote': quote, 'crypto': crypto})

    else:
        notfound = "Start by Typing in a symbol"
        return render(request, 'crypto/prices.html', {'notfound': notfound})
