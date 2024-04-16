from django import template
from django.urls import reverse
from ..models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name: str) -> str:
    """
    Отображает меню на основе предоставленного имени меню.
    
    Параметры:
        context (dict): Контекст, содержащий запрос.
        menu_name (str): Имя меню для отображения.
    
    Возвращает:
        str: Отображенный HTML-код меню.
    """
    global menu_list, active_url, tree
    menu_list = Menu.objects.all()
    active_url = context['request'].path
    if active_url:
        active_url = active_url.split('/')[-2]
    tree = []
    
    for menu in menu_list:
        if menu.name == menu_name:
            tree.append(menu)

    success = _build_menu_tree(tree[0]) if tree else False
    if success: return _render_html(tree[0])
    else: return ''

def _build_menu_tree(parent: Menu) -> bool:
    """
    Рекурсивно строит дерево меню, начиная с заданного родительского меню.

    Параметры:
        parent (Menu): Родительское меню, с которого начинается построение дерева.

    Возвращает:
        bool: True, если дерево меню успешно построено, False в противном случае.
    """
    global menu_list, active_url, tree
    for menu in menu_list:
        if menu.parent == parent:
            if menu.url == active_url:
                tree.append(menu)
                return True
            tree.append(menu)
            found = _build_menu_tree(menu)
            if found:
                return found
            else:
                tree.pop()
    return False

def _render_html(parent: Menu) -> str:
    """
    Отображает HTML-разметку для меню на основе предоставленного родительского меню.

    Параметры:
        parent (Menu): Родительское меню, с которого начинается построение дерева.

    Возвращает:
        str: Строковое представление меню в HTML-формате.
    """
    global menu_list, tree
    html = f'<ul class="{parent.name}">'
    for menu in menu_list:
        if menu.parent == parent:
            html += '<li>'
            html += f'<a href="{reverse(menu.name)}">{menu.title}</a>'
            if menu in tree:
                html += _render_html(menu)
            html += '</li>'
    html += '</ul>'
    return html