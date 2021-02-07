from django.shortcuts import render

# Create your views here.
import requests
import json
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "fff34e463bmshb704917899569eep168baajsna88882782d71",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers).json()


def helloworldview(request):
    mylist = []
    noofcountry = int(response['results'])
    for x in range(0, noofcountry):
        mylist.append(response['response'][x]['country'])

    if request.method == "POST":
        selectedcountry = request.POST['selectedcountry']
        for x in range(0, noofcountry):
            if selectedcountry == response['response'][x]['country']:
                active = response['response'][x]['cases']['active']
                new = response['response'][x]['cases']['new']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total) - int(active) - int(recovered)
        context = {'selectedcountry': selectedcountry, 'mylist': mylist, 'new': new, 'active': active, 'critical': critical,
                   'recovered': recovered, 'deaths': deaths, 'total': total}
        return render(request, 'helloworld.html', context)

    context = {'mylist': mylist}
    return render(request, 'helloworld.html', context)
