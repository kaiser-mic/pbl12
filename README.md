# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Nome 1: Pedro Henrique Bavaresco dos Santos 
- Nome 2: Nicolas Diovani Oliveira Dias
---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | pbl12 |
| Link do repositório | https://github.com/kaiser-mic/pbl12.git |

### Estrutura de Diretórios

projeto-qualidade-software/
├── src/
│   └── pedido.py
├── tests/
│   └── test_pedido.py
├── .github/
│   └── workflows/
│       └── quality.yml
└── requirements.txt
---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar validação de valor mínimo do pedido no checkout |
| Objetivo da funcionalidade | Somar os preços dos itens do pedido e verificar se o total atinge o valor mínimo exigido pelo restaurante, evitando que pedidos abaixo do valor mínimo avancem. |
| Link da Issue | https://github.com/kaiser-mic/pbl12/issues/1 |

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário (Pytest) |
| Objetivo do teste | Garantir que o cálculo soma corretamente os itens e lança um erro (ValueError) caso o total seja menor que o mínimo exigido.|
| Link para o arquivo do teste | https://github.com/kaiser-mic/pbl12/blob/main/tests/test_pedido.py |

```python
from order import calculate_total

from src.pedido import calcular_total_pedido
import pytest

def test_deve_calcular_total_quando_valor_minimo_e_atingido():
    itens = [{"preco": 10}, {"preco": 20}]
    valor_minimo = 15
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == 30

def test_deve_calcular_total_quando_total_e_exatamente_igual_ao_minimo():
    itens = [{"preco": 15}]
    valor_minimo = 15
    resultado = calcular_total_pedido(itens, valor_minimo)
    assert resultado == 15

def test_deve_lancar_erro_quando_total_e_menor_que_valor_minimo():
    itens = [{"preco": 5}, {"preco": 3}]
    valor_minimo = 15
    with pytest.raises(ValueError):
        calcular_total_pedido(itens, valor_minimo)
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | testando |
| Evento que dispara a execução | push e pull_request na main |
| Link para o workflow | https://github.com/kaiser-mic/pbl12/blob/main/.github/workflows/quality.yml |
| Link da execução | https://github.com/kaiser-mic/pbl12/actions/runs/28905013200 |

```yaml
name: testando

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  testes-unitarios:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout do repositório
      uses: actions/checkout@v4

    - name: Configurar Python 3.12
      uses: actions/setup-python@v5
      with:
        python-version: '3.12'

    - name: Instalar dependências (Pytest)
      run: |
        python -m pip install --upgrade pip
        pip install pytest

    - name: Executar suíte de testes
      env:
        PYTHONPATH: .
      run: |
        pytest tests/ -v
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 3 |
| Quantidade de testes aprovados | 3 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Bug: Sistema permitindo avançar pedidos abaixo do valor mínimo |
| Severidade | Alta |
| Link da Issue | https://github.com/kaiser-mic/pbl12/issues/2 |

O defeito foi encontrado atraves de testes que compararam o valor total do pedido com o valor minimo de um pedido. Foi corrigido adicionando um if total < valor_minimo que devolve ao usuario uma mensagem explicando o erro
