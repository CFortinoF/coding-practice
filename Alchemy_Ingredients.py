def check_ingredient_match(recipe, ingredients):
    amount_needed = len(recipe)
    in_possession = 0
    missing = []
    visited = []
    
    for rec in recipe:
        if (rec in ingredients) == False and (rec in visited) == False:
            missing.append(rec)
        else:
            visited.append(rec)
            in_possession+=1
    
    return (in_possession / amount_needed) * 100, missing