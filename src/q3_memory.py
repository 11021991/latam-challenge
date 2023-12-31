import pandas as pd
from collections import Counter
from typing import List, Tuple

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    # Lectura archivo optimizada con dtype={'content': 'str'}
    # Se recomienda hacerlo porque baja el uso de memoria
    df = pd.read_json(file_path, lines=True, dtype={'content': 'str'})

    # Al igual que la mejora de Q1, eliminé un paso e iteré directamente en el dataframe
    count_mentions = Counter([m[1:] for tweet in df['content'] for m in tweet.split() if m.startswith('@')])

    count_top_users = count_mentions.most_common(10)
    return count_top_users

