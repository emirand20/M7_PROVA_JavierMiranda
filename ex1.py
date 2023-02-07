import pandas as pd

def ex1():
    df = pd.read_csv('Llistat.csv', usecols=['NAME', 'NOTES'])
    deleteNan = df.dropna()
    abril = df[(df['NAME'] ==  'Abril')]
    abirilMedia = abril.mean()
    
    Andres = df[(df['NAME'] ==  'Bruno')]
    andresMedia = Andres.mean()
    
    Ivan = df[(df['NAME'] ==  'Ivan')]
    ivanMedia = Ivan.mean()
    
    Kevin = df[(df['NAME'] ==  'Kevin')]
    kevinMedia = Kevin.mean()
    
    Marta = df[(df['NAME'] ==  'Marta')]
    martaMedia = Marta.mean()
    
    Sara = df[(df['NAME'] ==  'Sara')]
    saraMedia = Sara.mean()
    
    Roger = df[(df['NAME'] ==  'Roger')]
    rogerMedia = Roger.mean()
    
    notas = [abirilMedia, andresMedia, ivanMedia, kevinMedia, martaMedia, saraMedia, rogerMedia]
    media = pd.DataFrame(notas)
    return media

print(ex1())