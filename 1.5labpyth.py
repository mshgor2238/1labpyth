import timeit
a1, a2, a3 = "Вот ", "скажите ", "мне "
a4, a5, a6 = "пожалуйста ", "нафига ", "нам "
a7, a8, a9, a10 = "10 ", "строк ", "для ", "задания??????????"
def pl():
    return a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8 + a9 + a10
def form():
    return "{}{}{}{}{}{}{}{}{}{}".format(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
def fstr():
    return f"{a1}{a2}{a3}{a4}{a5}{a6}{a7}{a8}{a9}{a10}"
plt = timeit.timeit(pl, number=10**8)
formt = timeit.timeit(form, number=10**8)
fstrt = timeit.timeit(fstr, number=10**8)
print(plt)
print(formt)
print(fstrt)