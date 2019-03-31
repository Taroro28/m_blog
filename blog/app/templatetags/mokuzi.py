from django import template
import re
register = template.Library()

@register.filter
def index(text):
    pattern = r"<h2>(.*)</h2>"
    h2_list = re.findall(pattern, text)
    result = ""
    count = 1
    for h2 in h2_list:
        result += "<li>" + str(count) + ". " + h2 + "</li>"
        count += 1
    return result
