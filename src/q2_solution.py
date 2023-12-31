import pandas as pd
import emoji
from collections import Counter
from typing import List, Tuple

# Primero, busqué documentación para trabajr con emojis y encontré la librería y este metodo.
# Fue el mayor desafio del ejercicio, porque estaba ocupando UNICODE_EMOJI y a partir de la versión 1.6.3 cambió por EMOJI_DATA
# Dejo link donde encontré la info. https://github.com/carpedm20/emoji/issues/221
def count_emojis(texto: str) -> List[str]:
    return [c for c in texto if c in emoji.EMOJI_DATA]

def q2_solution(file_path: str) -> List[Tuple[str, int]]:
    
    # Lectura archivo
    df = pd.read_json(file_path, lines=True)

    # Segundo, la lógica que apliqué fue primero concatenar todo el texto de todos los tweets.
    content = df['content']
    content_concat = ' '.join(content)

    # terceero, identifico los emojis en el texto
    emojis = count_emojis(content_concat)
    
    # Cuarto, con la clase Counter, cuento los emojis que existen en el texto concatenado
    q_emojis = Counter(emojis)

    # Quinto, seleccionar los 10 emojis más utilizados con la función most_common de Counter
    count_top_emoji = q_emojis.most_common(10)

    # Crea lista con el formato de retorno requerido
    results = [(emoji, conteo) for emoji, conteo in count_top_emoji] 
    return results
    




    