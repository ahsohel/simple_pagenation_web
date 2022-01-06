from django.shortcuts import render
from .models import details
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def index(request):
    d = details.objects.all()

    p = Paginator(d, 2)
    # print("p.num_pages")
    # print(p.num_pages)
    number_p = p.num_pages+1

    list1=[]
    for i in range(1, number_p):
        list1.append(i)
    # print("list1")
    # print(list1)

    page_numeber = request.GET.get('page', 1)
    try:
        page = p.page(page_numeber)
    except PageNotAnInteger:
        page = p.page(1)



    return render(request, 'index.html', {'page':page, 'list1':list1})



def page_2(request):

    f = Paginator(details.objects.all(), 1)
    total_page = f.num_pages+1
    l=[]
    for i in range(1, total_page):
        l.append(i)

    get_page = request.GET.get('page', 1)   # page is a variabl that has get valu from html page
    try:
        page = f.page(get_page)  # f.page() ae page ta holo pagenator ar function
    except PageNotAnInteger:
        page = f.page(1)


    return render(request, 'page_2nd.html', {'l':l, 'page':page})
