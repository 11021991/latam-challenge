import pandas as pd
from typing import List, Tuple
from datetime import datetime

def q1_solution(file_path: str) -> List[Tuple[datetime.date, str]]:
    # Cuando intenté leer el archivo la su estructura tenía varios objetos json separados por lineas
    # Usé lines=True para leerlo correctamente
    df = pd.read_json(file_path, lines=True)
    
    # Se convierte la columna date para considerar la fecha y no la hora
    df['date'] = pd.to_datetime(df['date'])

    # Cuando comencé a agrupar date y username, me di cuenta que {username} estaba dentro de {user}, por lo que tuve que cambiar mi lógica.
        # group_date_user = df.groupby(['date','username']).size().reset_index(name='q_tweets')

    # Primero, extrae el username del diccionario user y lo agrega como columna al dataframe
    df['username'] = df['user'].apply(lambda user_extract: user_extract.get('username'))

    # Segundo, agrupa por date y username y cuenta la cantidad de tweets asignandolos a la columna q_tweets
    group_date_user = df.groupby(['date','username']).size().reset_index(name='q_tweets')

    # Tercero, selecciona los usuarios con más tweet por fecha
    user_max_tweet = group_date_user.loc[group_date_user.groupby('date')['q_tweets'].idxmax()]

    # Cuarto, selecciona las 10 fechas con más tweets junto con el usuario
    date_max_tweet = user_max_tweet.groupby('date').apply(lambda x: x.nlargest(1, 'q_tweets')).head(10)

    # Quinto, elimina duplicados de fecha quedándose con el primer usuario con más tweets 
    date_max_tweet = user_max_tweet.drop_duplicates(subset='date')

    # Crea lista con el formato de retorno requerido
    results = [(date.date(), username) for date, username in zip(date_max_tweet['date'], date_max_tweet['username'])] 
    return results
    

    