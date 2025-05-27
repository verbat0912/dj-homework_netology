from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def omlet_view(request):
    servings = int(request.GET.get("servings", 1))
    for ingr in DATA['omlet']:
        DATA['omlet'][ingr] = DATA['omlet'][ingr] * servings
    context = {
        'recipe': DATA['omlet']
    }
    return render(request, 'calculator/index.html', context)

def pasta_view(request):
    servings = int(request.GET.get("servings", 1))
    for ingr in DATA['pasta']:
        DATA['pasta'][ingr] = DATA['pasta'][ingr] * servings
    context = {
        'recipe': DATA['omlet']
    }
    return render(request, 'calculator/index.html', context)

def buter_view(request):
    servings = int(request.GET.get("servings", 1))
    for ingr in DATA['buter']:
        DATA['buter'][ingr] = DATA['buter'][ingr] * servings
    context = {
        'recipe': DATA['buter']
    }
    return render(request, 'calculator/index.html', context)