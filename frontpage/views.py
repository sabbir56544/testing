from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from .models import Category, Sub_Category, Item, AboutUs, Course



from .forms import ContactForm



def index(request):
    try:
        form = ContactForm()
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home')
            else:
                form = ContactForm()

        abouts = AboutUs.objects.all()
        courses = Course.objects.all()[:4]
        category = Category.objects.all()
        sub = Sub_Category.objects.all()
        catId = request.GET.get('category')
        print(request.GET)
        if catId:
            item = Item.objects.filter(sub_category=catId)
        else:
            item = Item.objects.all()

        context = {
            'categories': category,
            'sub': sub,
            'items': item,
            'abouts': abouts,
            'courses':courses,
            'form': form,
        }

        return render(request, 'home.html', context)
    except:
        return render(request, 'category.html')


def category(request):
    category = Category.objects.all()
    # sub = Sub_Category.objects.all()
    catId = request.GET.get('category')
    print(request.GET)
    if catId:
        sub = Sub_Category.objects.filter(category=catId)
    else:
        sub = Sub_Category.objects.all()
    context = {
        'categories': category,
        'sub': sub,
        # 'items': item,
    }

    return render(request, 'index.html', context)




def serach_product(request):
    if request.method == 'POST':
        search_keyword = request.POST['search_keyword']
        serach_items = Category.objects.filter(name__contains=search_keyword)
        return render(request, 'search.html', {'serach_items': serach_items, 'serch_key': search_keyword})
    return render(request, 'search.html')



def autosuggest(request):
    query_original = request.GET.get('term')
    queryset = Category.objects.filter(name__icontains=query_original)
    mylist = []
    mylist += [x.name for x in queryset ]
    return JsonResponse(mylist, safe=False)