import pandas as pd
from collections import Counter
from typing import List, Tuple

def q3_solution(file_path: str) -> List[Tuple[str, int]]:
    # Lectura archivo
    df = pd.read_json(file_path, lines=True)

    # Primero, se divide el textos de los tweets con split y se tranforman en una lista.
    # Se itera filtrando solo palabras que su primer caracter comience con @
    # Se asigna en mentions
    mentions = df['content'].apply(lambda x: [m[1:] for m in x.split() if m.startswith('@')])

    # Segundo, Teniendo la lista de palabras se hace un conteo con Counter 
    count_mentions = Counter([mention for sublist in mentions for mention in sublist])
    
    # Tercero, se seleccionan los 10 usuario mas mencionados con la función most_common de Counter 
    count_top_users = count_mentions.most_common(10)
    return count_top_users

