def calcular_total_pedido(itens, valor_minimo):
    total = sum(item['preco'] for item in itens)
    if total < valor_minimo:
        raise ValueError(f"O total do pedido ({total}) é menor que o mínimo exigido ({valor_minimo}).")
    return total