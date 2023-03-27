from ai import recipe

def load_recipes( filename = 'recipes.txt' ):
    try:
        with open( filename, 'r') as f:
            return f.read().split('@')
    except:
        with open( filename, 'w' ) as _:
            pass
        return []

def save_recipe( text, filename = 'recipes.txt' ):
    with open('recipes.txt', 'a') as f:
        f.write(recip + '@')
        
def delete_recipe( number,  filename = 'recipes.txt'  ):
    L = load_recipes( filename )
    if 1<=number<=len(L):
        with open( filename, 'w' ) as f:
            for i,r in enumerate(L):
                if i!= number-1:
                    f.write(r+'@')


while True:
    print("\nWelcome to Codebook, select an option")
    print("1) Show all the recipes")
    print("2) Create recipe")
    print("3) Delete recipe")
    print("4) Exit")

    opc = input("> ")[0]

    if opc == '1':
        R = load_recipes()
        for i,r in enumerate(R):
            if len(r)>10:
                print( f'\nRecipe {i+1} .- ')
                print(r)
                print('---------------------------------\n')
    elif opc == '2':
        Ingredients = []
        instructions = ""

        print("Inrtoduce a list of ingredients and a brief description")
        while True:
            I = input( "New ingredient:  " )
            Ingredients.append( I )
            if input('Do you want to append more ingredients? [y,n] : ')[0].lower() =='n':
                break
        instructions = input('Instructions for the recipe: ')

        recip = recipe( Ingredients, instructions ).choices[0].text
        print('\n--------------------------------------------------')
        print( recip )
        print('--------------------------------------------------\n')
        if input('Do you want to save it? [y,n] ')[0].lower() =='y':
            save_recipe( recip )
            print("Saved!\n")
    elif opc=='3':
        number = int(input('Introduce the number of recipe to delete: '))
        delete_recipe( number )
        print( 'Deleted!' )
    elif opc=='4':
        break
