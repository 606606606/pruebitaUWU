#pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
#pluralize(["table", "table", "table"]) ➞ { "tables" }
#pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }

def pluralize(lista):
    nueva_lista = []
    for x in lista:
        if lista.count(x) == 1:
            nueva_lista.append(x)
        else:
            if (str(x) + 's') not in nueva_lista:
                nueva_lista.append(str(x) + 's')
    return set(nueva_lista)
print(pluralize(["chair", "pencil", "arm"]))
