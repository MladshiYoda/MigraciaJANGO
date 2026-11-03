from django.shortcuts import render

# Главная страница
def home(request):
    return render(request, 'home.html')

# О компании
def about(request):
    return render(request, 'about.html')

# Контакты
def contacts(request):
    return render(request, 'contacts.html')

# Как нас найти
def how_to_find(request):
    return render(request, 'how_to_find.html')

# Услуги (Страница 1 по вашей теме)
def page1(request):
    return render(request, 'page1.html')

# Цены (Страница 2 по вашей теме)
def page2(request):
    return render(request, 'page2.html')