from django.http import Http404, HttpResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from .models import Product
from django.views.generic.edit import CreateView
from django.views.generic import ListView

# Create your views here.
# Функции представления страниц

menu = [{'title' : "О сайте", 'url_name' : 'about'},
        # {'title' : "Добавить статью", 'url_name' : 'add_post'},
        {'title' : "Добавить товар", 'url_name' : 'add_product'},
        {'title' : "Обратная связь", 'url_name' : 'contact'},
        {'title' :  "Войти", 'url_name' : 'login'}
         ]
# context = {'menu': menu, 'title': 'Главная страница'}

# def index(request):
#     product = Product.objects.all()
#     context={'menu': menu, 'title': 'Главная страница', 'product' : product}
#     return render(request, 'school/index.html', context=context)
class ProductHome(ListView):
    model = Product
    template_name = 'school/index.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        print(context)
        return context
    
def about(request):
    return render(request, 'school/about.html', {'menu': menu, 'title': 'О нас'})

def archive(request, year):
    if int(year) > 2024:
        # raise Http404()
        # return redirect ('/') #302 URL перемещён временно
        return redirect ('home', permanent = True) #301 URL перемещён постоянно
    return HttpResponse(f"АРХИВ - {year}")

# def products(request, products_id): #HttpRequest
#     if(request.GET):
#         print(request.GET)
    
    return HttpResponse(f"products page {products_id}")

def pageNotFound(request, exception): #HttpRequest
    return HttpResponseNotFound(f"<H1>PAGE NOT FOUND</H1>")

def add_post(request):
    return HttpResponse("Добавить статью")

def contact(request):
    return HttpResponse("Обратная связь")

def login(request):
    return HttpResponse("Войти")

def product_description(request, prodid):
    product = get_object_or_404(Product, slag=prodid)
    # product = Product.objects.all()
    # p = product.get(slag=prodid)
    p_discription = product.description
    context = {'title' : "Карточка товара",
               'url_name' : 'product_description',
               'p_discription' : p_discription}
    return render(request, 'school/product_description.html', context=context)


from .forms import ProductForm
class ProductCreateView(CreateView):
    # model = Product
    form_class = ProductForm
    template_name = 'school/create.html'
    # success_url = reverse_lazy('home')
    # success_url = 'school/create.html'
    
    # def get_context_data(self, **kwargs):
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Добавить товар'
        print(context)
        return context