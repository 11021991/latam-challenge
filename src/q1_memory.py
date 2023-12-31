import pandas as pd
from typing import List, Tuple
from datetime import datetime

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    
    # Lectura archivo optimizada con dtype={'content': 'str'}
    # Se recomienda hacerlo porque baja el uso de memoria
    df = pd.read_json(file_path, lines=True, dtype={'content': 'str'})
    df['username'] = df['user'].apply(lambda user_extract: user_extract.get('username'))
    group_date_user = df.groupby(['date', 'username']).size().reset_index(name='q_tweets')

    # user_max_tweet = group_date_user.loc[group_date_user.groupby('date')['q_tweets'].idxmax()]
    # Modifiqué la lógica anterior porque en primera instancia estaba creando un dataframe con data que no estaba utilizando ya que solo necesitaba los máximos.
    # Con esto, de paso, tambien reduzco el consumo de memoria. 

    # En vez de crear el dataframe, solo obtengo los indices de los maximos valores por fecha.
    max_date_id = group_date_user.groupby('date')['q_tweets'].idxmax()
    # Ahora si, creo el dataframe solo con los valores máximos
    date_max_tweet = group_date_user.loc[max_date_id]
    # Finalmente, selecciono las 10 fechas con más tweets y el usuario. 
    date_max_tweet = date_max_tweet.nlargest(10, 'q_tweets')[['date', 'username']]


    results = [(date.date(), username) for date, username in zip(date_max_tweet['date'], date_max_tweet['username'])] 
    return results




    