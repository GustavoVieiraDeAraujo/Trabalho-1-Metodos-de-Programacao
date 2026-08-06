# Problema das 8 Rainhas

Trabalho 1 da disciplina **Metodos de Programacao (MP)** do Departamento de Ciencia da Computacao da Universidade de Brasilia. Verificador do problema das 8 rainhas implementado em Python com desenvolvimento orientado a testes (TDD), integrado com SonarCloud para analise de qualidade e cobertura de codigo.

---

## Sumario

- [Participantes](#participantes)
- [Tecnologias](#tecnologias)
- [Escopo do Projeto](#escopo-do-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Requisitos](#requisitos)
- [Como Executar](#como-executar)
- [Funcoes Implementadas](#funcoes-implementadas)
- [Testes](#testes)

---

## Participantes

| Nome                              | Matricula |
|-----------------------------------|-----------|
| Gustavo Vieira de Araujo          | 211068440 |

---

## Tecnologias

| Tecnologia      | Uso                                              |
|-----------------|--------------------------------------------------|
| Python 3        | Linguagem de implementacao                       |
| pytest          | Framework de testes                              |
| coverage        | Medicao de cobertura de codigo                   |
| tox             | Automacao de ambientes de teste                  |
| SonarCloud      | Analise estatica e qualidade de codigo            |

---

## Escopo do Projeto

| Requisito                                    | Implementacao                                                    |
|----------------------------------------------|------------------------------------------------------------------|
| Verificar se entrada tem 64 posicoes         | `verifica_se_o_tabalueiro_tem_64_posicoes`: valida 8x8          |
| Verificar se tabuleiro tem 8 rainhas         | `verifica_se_o_tabuleiro_tem_8_rainhas`: conta posicoes com 1   |
| Verificar conflitos em retas                 | `verifica_as_retas_da_rainha`: linhas e colunas                 |
| Verificar conflitos em diagonais             | `verifica_as_diagonais_da_rainha`: 4 direcoes diagonais         |
| Funcao principal de verificacao              | `verificar_se_o_tabuleiro_e_solucao`: retorna 1, 0 ou -1        |
| Testes TDD (7 testes)                        | Cada funcao testada individualmente com pytest                   |
| Analise de qualidade e cobertura             | SonarCloud (`sonar-project.properties`) + coverage               |

---

## Estrutura do Projeto

| Arquivo                      | Descricao                                                     |
|------------------------------|---------------------------------------------------------------|
| `oito_rainhas.py`            | Funcoes de verificacao do problema das 8 rainhas               |
| `testa_oito_rainhas.py`     | 7 testes unitarios (pytest)                                    |
| `testes.txt`                 | Justificativa de cada teste                                    |
| `tox.ini`                    | Configuracao do tox (pytest + coverage)                        |
| `sonar-project.properties`   | Configuracao do SonarCloud                                     |

---

## Requisitos

- Python 3.9+
- pytest
- coverage

```bash
pip install pytest coverage tox
```

---

## Como Executar

```bash
# Executar testes
python3 -m pytest testa_oito_rainhas.py -v

# Executar com cobertura
coverage run -m pytest testa_oito_rainhas.py
coverage report

# Executar via tox
tox
```

---

## Funcoes Implementadas

| Funcao                                      | Entrada                    | Saida              | Descricao                                         |
|---------------------------------------------|----------------------------|--------------------|----------------------------------------------------|
| `posiciona_rainhas_no_tabuleiro`             | String de 0s e 1s          | Matriz 8x8         | Converte entrada em tabuleiro                      |
| `pega_as_posicoes_das_rainhas`              | Matriz 8x8                 | Lista de posicoes   | Retorna coordenadas [linha, coluna] das rainhas    |
| `verifica_se_o_tabuleiro_tem_8_rainhas`     | Matriz 8x8                 | bool                | True se tem exatamente 8 rainhas                   |
| `verifica_se_o_tabalueiro_tem_64_posicoes`  | Matriz 8x8                 | bool                | True se tem 8 linhas de 8 elementos                |
| `verifica_as_diagonais_da_rainha`           | Matriz 8x8 + posicao       | bool                | True se nenhuma rainha nas 4 diagonais              |
| `verifica_as_retas_da_rainha`               | Matriz 8x8 + posicao       | bool                | True se nenhuma rainha nas linhas/colunas            |
| `verificar_se_o_tabuleiro_e_solucao`        | String de 0s e 1s          | 1, 0 ou -1          | 1=solucao, 0=nao solucao, -1=entrada invalida      |

---

## Testes

7 testes TDD executados com pytest:

| # | Teste                                                              | O que verifica                          |
|---|--------------------------------------------------------------------|-----------------------------------------|
| 1 | `testa_montagem_tabuleiro_corretamente`                            | String → matriz 8x8 correta            |
| 2 | `testa_pega_as_posicoes_das_rainhas_corretamente`                  | Posicoes das rainhas extraidas          |
| 3 | `testa_se_tabuleiro_tem_8_rainhas`                                 | Contagem de rainhas = 8                  |
| 4 | `testa_se_tabuleiro_tem_64_posicoes`                               | Dimensao 8x8 do tabuleiro               |
| 5 | `testa_se_as_diagonais_da_rainha_escolhida_nao_tem_outras_rainhas` | Diagonais livres                        |
| 6 | `testa_se_as_retas_da_rainha_escolhida_nao_tem_outras_rainhas`     | Linhas e colunas livres                  |
| 7 | `testa_se_tabuleiro_e_solucao`                                     | Entrada valida retorna 1                 |

```
$ python3 -m pytest testa_oito_rainhas.py -v
7 passed in 0.01s
```

---

> Documentacao gerada com auxilio de IA.
