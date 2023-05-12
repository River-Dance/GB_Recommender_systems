import pandas as pd
import numpy as np


def recall_at_k(recommended_list, bought_list, k=5):
    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    #TODO: Ваш код здесь
    flags = np.isin(bought_list, recommended_list)
    recall = flags.sum() / len(bought_list)
    
    return recall


def money_recall_at_k(recommended_list, bought_list, prices_recommended, prices_bought, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    prices_recommended = np.array(prices_recommended)
    prices_bought = np.array(prices_bought)

    # Проверяем, что recommended_list не пустой
    if not recommended_list.any():
        raise ValueError('Список рекомендаций пуст')

    recommended_list = recommended_list[:k]

    flags = np.isin(bought_list, recommended_list)

    precision = np.sum(flags * prices_recommended) / np.sum(prices_recommended)

    return precision # Добавьте сюда результат расчета метрики


def mrr_at_k(recommended_list, bought_list, k=5):
    if not isinstance(recommended_list, np.ndarray):
        raise TypeError("recommended_list должен быть массивом NumPy")
    if not isinstance(bought_list, np.ndarray):
        raise TypeError("bought_list должен быть массивом NumPy")
    if not isinstance(k, int):
        raise TypeError("k должен быть целым числом")
    if k < 1:
        raise ValueError("k должен быть положительным целым числом")
    if recommended_list.size == 0:
    raise ValueError("recommended_list не должен быть пустым")
if bought_list.size == 0:
    raise ValueError("bought_list не должен быть пустым")    
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    #TODO: Ваш код здесь
    bought_list.resize(len(bought_list))
    recommended_list.resize(k)
    
    rr_list = np.isin(recommended_list, bought_list)
    rr = np.sum(rr_list * 1 / (np.arange(len(recommended_list)) + 1))
    
    return rr #Добавьте сюда результат расчета метрики


def ndcg_at_k(recommended_list, bought_list, k=5):
    bought_list = np.array(bought_list)
    recommended_list = np.array(recommended_list)
    
    #TODO: Ваш код здесь
    relevant_indexes = np.isin(recommended_list, bought_list)
    # Если рекомендации не содержат релевантных продуктов, то nDCG@K = 0
    if not relevant_indexes.any():
        return 0.
    else:
        # Вычисляем значение DCG@K
        dcg = np.sum(relevant_indexes / np.log2(np.arange(2, relevant_indexes.size + 2)))
        # Вычисляем значение IDCG@K
        idcg = np.sum(np.ones(np.min([relevant_indexes.size, k])) / np.log2(np.arange(2, relevant_indexes.size + 2)))
        # Если IDCG@K равен 0, то nDCG@K = 0
        if not idcg:
            return 0.
        else:
            return dcg / idcg #Добавьте сюда результат расчета метрики    
        




