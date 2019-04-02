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
        result += "<li><a href=\"#link"+str(count)+"\">" + str(count) + ". " + h2 + "</a></li>"
        count += 1
    return result

@register.filter
def headline(text):
    sum = text.count("<h2>")
    count = 0
    for i in range(sum):
        count += 1
        replaced_text = "<h2 id=\"link" + str(count) + "\" >"
        text = text.replace("<h2>", replaced_text, 1)
    return text
