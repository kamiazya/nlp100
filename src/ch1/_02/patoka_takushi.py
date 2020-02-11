a = "パトカー"
b = "タクシー"

join = "".join

print(join((map(join, zip(a, b)))))
