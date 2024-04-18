from django import template
from django.urls import reverse
from ..models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name: str) -> str:
    """
    Draws a menu based on the provided menu name.
    Options:
        context (dict): The context containing the request.
        menu_name (str): Name of the menu to display.
    
    Returns:
        str: The rendered HTML code of the menu.
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
    Recursively builds a menu tree starting
    from a given parent menu until it finds active_url.

    Options:
        parent (Menu): The parent menu from which to start building the tree.

    Returns:
        bool: True if the menu tree was successfully built, False otherwise.
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
    Renders HTML markup for a menu based on the tree that was build before.
    Options:
        parent (Menu): The parent menu from which to start building the tree.

    Returns:
        str: String representation of the menu in HTML format.
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