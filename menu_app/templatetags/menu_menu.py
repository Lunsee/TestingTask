from django import template
from ..models import MenuItem
from django.utils.safestring import mark_safe

register = template.Library()

SAVED_URLS = {                                     #справочник для именованных ссылок
    'github_url': 'https://github.com/Lunsee',
    'some_other_url': 'https://github.com/',
}
@register.simple_tag
def draw_menu(menu_name, current_url):
    try:
        menu = MenuItem.objects.prefetch_related('menuitem_set').get(title=menu_name)
    except MenuItem.DoesNotExist:
        return ""

    def render_menu(menu_item, processed_items=None):
        if processed_items is None:
            processed_items = set()

        if menu_item in processed_items:
            return ""

        processed_items.add(menu_item)
        output = '<ul>'

        if menu_item.url and not menu_item.url.endswith('/'):
            menu_item.url += '/'

        if current_url == menu_item.url:
            output += f'<li><a href="{menu_item.url}" style="background-color: #00b6e9; color: white;">{menu_item.title}</a></li>'  # добавляем стили для обозначения активного элемента меню
        else:
            output += f'<li><a href="{menu_item.url}">{menu_item.title}</a></li>'

        children = menu_item.menuitem_set.all()
        if children:
            output += '<ul>'
            for child in children:
                output += render_menu(child, processed_items)
            output += '</ul>'
        output += '</ul>'
        return output

    menu_html = render_menu(menu)
    return mark_safe(menu_html)
