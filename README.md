# Pipeline de ETL - Djalma Noivas 👰💍

Este repositório contém um projeto prático de Engenharia de Dados focado na simulação de um pipeline de **ETL (Extract, Transform, Load)** utilizando a linguagem Python. O cenário de negócios foi inspirado de forma fictícia na famosa loja de noivas da série televisiva *"Tapas & Beijos"*.

## 📌 Contexto de Negócio

O objetivo do projeto é automatizar o processamento dos dados de alugueres de vestidos da loja "Djalma Noivas". O sistema recebe um relatório bruto com informações sobre as clientes, os modelos escolhidos e o estado do pagamento. A partir daí, o pipeline deve limpar os dados inválidos ou cancelados e consolidar a faturação real gerada pelos casamentos confirmados.

## ⚙️ Arquitetura do Pipeline (ETL)

O script `etl_djalma_noivas.py` executa as três etapas fundamentais de um fluxo de dados:

1. **Extração (Extract):** Simula a receção de dados brutos através da leitura de um ficheiro inicial chamado `alugueis_brutos.csv`, que contém dados de registo de clientes (incluindo personagens icónicas como Fátima e Sueli).
2. **Transformação (Transform):** Aplica regras de negócio utilizando estruturas de repetição e condicionais em Python. Nesta etapa, todos os registos com o estado "Cancelado" são descartados da soma final e o pipeline calcula a faturação total consolidada.
3. **Carga (Load):** Exporta os dados limpos, organizados e validados para um novo ficheiro estruturado chamado `relatorio_faturamento_final.csv`, pronto para ser consumido por ferramentas de análise ou dashboards.

## 🛠️ Tecnologias Utilizadas

* **Python 3.x:** Linguagem principal para manipulação lógica e tratamento de dados.
* **Biblioteca CSV:** Manipulação e geração de ficheiros de dados de forma nativa e eficiente.
* **Visual Studio Code:** Ambiente de desenvolvimento integrado (IDE).

## 🚀 Como Executar o Projeto

1. Certifique-se de que tem o Python instalado na sua máquina.
2. Clone este repositório para o seu ambiente local:
   ```bash
   git clone [https://github.com/02mari/djalma_noivas.git](https://github.com/02mari/djalma_noivas.git)
