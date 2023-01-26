def cakes(recipe, available):
    kolmin = 0
    for key in recipe:
        try:
            available[key]
        except KeyError:
            return 0
        kol = available[key] / recipe[key]
        if kolmin == 0:
            kolmin = kol
        if kolmin > kol:
            kolmin = int(kol)
    return int(kolmin)






recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
cakes(recipe, available)# , 2, 'example #1')

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
cakes(recipe, available)# , 0, 'example #2')