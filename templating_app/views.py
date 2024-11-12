from django.shortcuts import render

def home(request):
    context = {}
    return render(request,"index.html",context)

def starterpage(request):
    context = {}
    return render(request,"starter-page.html",context)

#About Page

def about(request):
    context = {}
    return render(request,"about.html", context)

#Menu  Page

def menu(request):
    context = {}
    return render(request,"menu.html", context)

#My story Page

def specials(request):
    context = {}
    return render(request,"specials.html", context)

#About Page

def events(request):
    context = {}
    return render(request,"events.html", context)

#Menu  Page

def gallery(request):
    context = {}
    return render(request,"gallery.html", context)

#My story Page

def chefs(request):
    context = {}
    return render(request,"chefs.html", context)

def book_a_table(request):
    return render(request, "book_table.html")