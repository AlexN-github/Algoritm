#Задача№3
#По введенным пользователем координатам двух точек
#вывести уравнение прямой вида y = kx + b, проходящей через эти точки.
#Ссылка:
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=lesson01_task03#R7VlLb%2BM2EP41ArYFHOht%2BehX2kMKLBCgbfZGW7SsNS2qFB1L%2FfUdSqREWbajpHacXcQHmRzOg%2BTMfBxRhjPd5r8xlK7%2FoCEmhm2GueHMDNsOfA%2BeglBUBDdwKkLE4rAiWQ3hMf4XS6Ipqbs4xFmLkVNKeJy2iUuaJHjJWzTEGN232VaUtK2mKMIdwuMSkS71rzjka7kse9jQf8dxtFaWLX9UjWyRYpYrydYopHuN5MwNZ8oo5VVrm08xEXun9qWSuz8xWk%2BM4YT3Edg83E8Tczh%2BSvDDePFtF%2F7pZgO5jIwXasE4hPXLLmV8TSOaIDJvqBNGd0mIhVYTeg3PA6UpEC0gfsecF9KZaMcpkNZ8S%2BQozmP%2BtxC%2F82TvSRuZ5VJz2SlUJ%2BGs0IRE90kfa8TKnpKr1icWdXLbJCmjO7bEZ%2FZKhR9iEeZn%2BJzauZAUmG4xzAfkGCaIx8%2FteSAZnlHN13gQGtKJr3Co1PuMyE5aMmyfwHQnKwoL1l3t%2F7OjamCQlc4aA8MozZsxaEXlP2zmaCaeE9MAVwVD1YZnOTqZK0Mw78qWFO1EGCGQvSKS9uuY48cUldu%2BB%2Fxox4lcCmYc5%2Be9191tKeCo7JPwM5TdfZPLlmJZa3nsmFfyj931T6%2Bt%2FUB76Fm33sTgE7V6o5bTE7XcW6KWc0XUssukqhLJlukknq4ysWCH%2FDWnJznFMyj1KLpd5edYUzgvGcy2CDz13FaT6Zq2fbQVuZsssrScSm1srqGCJ62C%2BbltBK4x8sEnU7sv9kIRkoomRBIiBBMaMbQFxhSzGFyJ2eHY12bgBlBTw8pLUONdC2pGn1DTG2rcnlDj3RJq3OtCzRtApuZ8K6S8CCa5wIhCPHJbtH5auBjdGi4s55Z4YWlo0WDHh8ULrydeWCei4J3eqIbHS3ZX5uChvyGceds9iMRRAu0l7FCZGSLo4yUiYzmwjcOwigQMMIMWpSqx2SmNE14uyJsY3kxsvzMhaIHJBC03URk4U0ooK007q%2FJ3LrfkNYk0YdSXE7r7zgT2yUwcmHcjq5WL6k20t5Ok7q9iyRoLXa0yiI5DL9ZT%2BB%2BO9Y47dqYqrQpcP4%2F%2FC6ez%2F1Ik%2BcNh8NGDpxs7cMjCvzPLuzHD1nS72GXvcya67TPR9rtnYnDkSAyudiT6P0oOXTAXTsT4W%2BNZ%2BTY4cROjVFS5J6UuH%2FR%2BJ%2Bg38PelsAeF9Qto%2FJLbg1y0jhSkJSWMn49W2OLMHMhjUpTYBK%2F4kRpbaslSlCjaAvQU1mDzq6hx66JW59DIpfkTpW474t6%2FdnXNnrWrf7VE%2FTzsXvExoO%2FXAPsSSDBmDBUag6wLTwKFdwAUbnDwbegFYDngh0Y1g8vWX9f8VvGKWz9xYJvai7apCc3U%2FXvF4Fl3onn8nf5e0xGcuET0NK3B4VWirVsOlBTodI4aFb7awPoBA6XkTLOhL7q6O5xqFL%2B9up%2FiNsA7QNS6EroCokK3%2BXJbJUTz%2BduZ%2Fwc%3D
print("Введите координаты точки №1")
x1 = int(input("Введите x1:\n"))
y1 = int(input("Введите y1:\n"))
print("Введите координаты точки №2")
x2 = int(input("Введите x2:\n"))
y2 = int(input("Введите y2:\n"))

#Вычисляем k,b
if(x2==x1):
    print("x2 равно x1. Приведение к виду y=kx+b невозможно")
    exit()
k = (y2-y1)/(x2-x1)
b = y1 - k*x1

#Выводим формулу прямой
print("y = {0}*x + {1}".format(k,b))


