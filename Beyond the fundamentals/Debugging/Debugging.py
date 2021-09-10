def plant_recommendation(care):
    if care == 'low': #Syntax error
        print('aloe')
    elif care == 'medium':
        print('pothos')
    elif care == 'high': #Logic error
        print('orchid')

plant_recommendation('low') #Runtime error
plant_recommendation('medium')
plant_recommendation('high')

