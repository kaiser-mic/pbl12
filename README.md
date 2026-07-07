# Aula 17 – Integração Contínua, Qualidade Automatizada, Métricas e Gestão de Defeitos

## Integrantes

- Nome 1
- Nome 2
- Nome 3
- Nome 4

---

## 1. Repositório da Atividade

| Item | Descrição |
|--------|--------|
| Nome do repositório | localeats-ci-laboratorio |
| Link do repositório | https://github.com/grupo/localeats-ci-laboratorio |

### Estrutura de Diretórios

```text
localeats-ci-laboratorio/
├── tests/
│   ├── test_order.py
│   └── features/
│       └── order_total.feature
├── .github/
│   └── workflows/
│       └── quality.yml
├── order.py
└── requirements.txt
```

---

## 2. Planejamento da Funcionalidade

| Item | Descrição |
|--------|--------|
| Título da Issue | Implementar cálculo do valor total do pedido |
| Objetivo da funcionalidade | Calcular automaticamente a soma dos itens do pedido |
| Link da Issue | https://github.com/grupo/localeats-ci-laboratorio/issues/1 |

---

## 3. Teste Automatizado

| Item | Descrição |
|--------|--------|
| Tipo de teste | Unitário |
| Objetivo do teste | Verificar o cálculo correto do valor total |
| Link para o arquivo do teste | https://github.com/grupo/localeats-ci-laboratorio/blob/main/tests/test_order.py |

```python
from order import calculate_total

def test_calculate_total():
    assert calculate_total([10, 20, 30]) == 60
```

---

## 4. Pipeline de Integração Contínua

| Item | Descrição |
|--------|--------|
| Nome do workflow | Quality Check |
| Evento que dispara a execução | push e pull_request |
| Link para o workflow | https://github.com/grupo/localeats-ci-laboratorio/blob/main/.github/workflows/quality.yml |
| Link da execução | https://github.com/grupo/localeats-ci-laboratorio/actions |

```yaml
name: Quality Check

on:
  push:
  pull_request:

jobs:
  tests:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - run: pip install pytest

      - run: pytest
```

---

## 5. Indicadores de Qualidade

| Indicador | Valor |
|------------|---------|
| Quantidade de testes executados | 1 |
| Quantidade de testes aprovados | 1 |
| Quantidade de testes com falha | 0 |
| Status final do pipeline | Sucesso |

---

## 6. Registro de Defeito

| Item | Descrição |
|--------|--------|
| Título do defeito | Erro no cálculo do valor total |
| Severidade | Alta |
| Link da Issue | https://github.com/grupo/localeats-ci-laboratorio/issues/2 |

O defeito foi simulado alterando a função para retornar um valor incorreto. O problema foi identificado pela falha do teste automatizado durante a execução do pipeline. Após corrigir a implementação, os testes voltaram a ser aprovados.
