
text = "<h2>見出し１</h2>ここはテキスト<h2>見出し2</h2>ここはテキスト<h2>見出し3</h2>ここはテキスト"

sum = text.count("<h2>")
count = 0
for i in range(sum):
    count += 1
    replaced_text = "<h2 id=\"link" + str(count) + "\" >"
    text = text.replace("<h2>", replaced_text, 1)

print(text)
