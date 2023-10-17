from django.shortcuts import render
from .templatetags.menu_menu import draw_menu

def main_page(request):
    current_url = request.path
    return render(request, 'base.html', {'current_url': current_url})

def block1(request):
    current_url = request.build_absolute_uri()
    menu_html = draw_menu('Block1', current_url)
    return render(request, 'block1_template.html', {'menu_html': menu_html})

def block2(request):
    current_url = request.build_absolute_uri()
    menu_html = draw_menu('Block2', current_url)
    return render(request, 'block2_template.html', {'menu_html': menu_html})
