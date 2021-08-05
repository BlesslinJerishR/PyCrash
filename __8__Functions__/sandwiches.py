# 8.12
def sandwich_order(*types):
    """To order a sandwich using arbitrary arguments"""
    print('The ordered sandwich is')
    for type in types:
        print(f'- {type}')


sandwich_order('tomato', 'honey', 'cheese')
