# library/templatetags/library_tags.py

from django import template
register = template.Library()

@register.simple_tag(takes_context=True)
def is_correct_ip(context):
    request = context['request']
    user_ip = request.META.get('REMOTE_ADDR')
    print("User IP:", user_ip)  # Debugging statement
    return user_ip == '192.168.1.112'
