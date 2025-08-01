# Objetivo do projeto:

Criar pipelines automatizados (DAGs) para extrair, transformar e carregar dados (ETL/ELT) de fontes variadas, possibilitando a atualização periódica de dados em um data warehouse (ex: BigQuery). Esses dados alimentam dashboards dinâmicos que permitem visualizações analíticas em tempo real ou quase real, facilitando a tomada de decisão rápida e embasada.

# Como rodar as DAGs:

Basta entrar no diretório principal do projeto e digitar `astro dev start`, ao mesmo tempo que para parar a run basta escrever `astro dev stop`.

# Airflow em execução:
<img width="366" height="289" alt="image" src="https://github.com/user-attachments/assets/acaaaf56-71d2-44b5-a8c2-42104a91d1be" />

ps: até que funcionasse, foi preciso fazer manutenção de dependências e refatoração de código para evitar problemas com serialização.

<img width="1080" height="768" alt="image" src="https://github.com/user-attachments/assets/b21f0ae0-4b55-4b4a-9fab-ec386d5f039c" />

# Dados no Big Query e Looker Studio:

<img width="1520" height="730" alt="image" src="https://github.com/user-attachments/assets/668f92c8-966c-4a12-a049-bf09eb79e5d1" />
<img width="1520" height="730" alt="image" src="https://github.com/user-attachments/assets/11f72b15-e9be-4ba4-965d-3bd5f08ee30c" />


# Tecnologias utilizadas
### Apache Airflow — orquestração de workflows via DAGs para automação das tarefas ETL.

### Docker — ambiente isolado para rodar o Airflow e dependências de forma padronizada.

### Astronomer — plataforma gerenciada para deploy e execução do Airflow na nuvem.

### Google BigQuery — data warehouse escalável para armazenar e consultar dados.

### Looker Studio (antigo Google Data Studio) — ferramenta para criação de dashboards dinâmicos e relatórios.

### Python — linguagem usada para escrever scripts das tasks no Airflow e manipulação dos dados.

### APIs (exchangerate-api) — para conexão, ingestão e exportação dos dados.
