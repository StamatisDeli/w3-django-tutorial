from django.http import HttpResponse
from django.template import loader
from .models import Member
from django.db.models import Q


def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("all_members.html")
    context = {
        "mymembers": mymembers,
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember,
    }
    return HttpResponse(template.render(context, request))


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def testing(request):
    mymembers = Member.objects.all().values()
    mydata = Member.objects.all().values()
    myrecord = Member.objects.filter(firstname='Emil').values()
    myfilter = Member.objects.filter(lastname='Refsnes', id=2).values()
    my2filter = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
    myQExpfilter = Member.objects.filter(Q(firstname='Emil') | Q(firstname='Tobias')).values()
    myorderedbyfirstnamedata = Member.objects.all().order_by('firstname', "id").values()

    template = loader.get_template("template.html")
    context = {
        "fruits": ["Apple", "Banana", "Cherry"],
        "mymembers": mymembers,
        "mydata": mydata,
        "myrecord": myrecord,
        "myfilter": myfilter,
        "my2filter": my2filter,
        "myQExpfilter": myQExpfilter,
        "myorderedbyfirstnamedata": myorderedbyfirstnamedata
    }

    print("Printing to the console from views.py", myfilter[0]['firstname'])

    return HttpResponse(template.render(context, request))
