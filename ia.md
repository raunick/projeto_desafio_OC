# Detecção de Padrões de Espera usando Mineração de Dados

🏥 A detecção de padrões de espera usando técnicas de mineração de dados permite analisar os dados de filas de atendimento e identificar padrões recorrentes. Essa análise ajuda a identificar gargalos no processo de atendimento e possibilita o planejamento de ações para reduzir os tempos de espera nos hospitais. 📊

# Contexto:
👨‍⚕️ Imagine um hospital que deseja melhorar o fluxo de atendimento na emergência. Eles coletam dados de filas de atendimento, incluindo informações como horário de chegada dos pacientes, gravidade do caso, tempo de espera e tempo de atendimento. Utilizando técnicas de mineração de dados, eles podem analisar esses dados e identificar padrões recorrentes. 📈

Por exemplo, eles podem descobrir que nos horários de pico, como às 9h e às 18h, há um aumento significativo no tempo de espera. Além disso, podem identificar padrões específicos relacionados à gravidade dos casos, como longos tempos de espera para casos de menor gravidade, devido à priorização de casos mais urgentes. ⏱️

Com base nessas informações, o hospital pode planejar ações para reduzir os tempos de espera. Por exemplo, eles podem redistribuir a equipe médica e de enfermagem para os horários de pico, garantindo uma maior capacidade de atendimento. Além disso, podem implementar protocolos de triagem mais eficientes para identificar rapidamente os casos de maior gravidade e priorizá-los no atendimento. 📅


## Exemplo codigo Python:

```python
import pandas as pd
from sklearn.cluster import KMeans

# Exemplo de dados de filas de atendimento
queue_data = pd.DataFrame({
    'horario_chegada': ['09:15', '09:30', '09:45', '10:00', '10:15', '18:00', '18:15', '18:30', '18:45', '19:00'],
    'gravidade_caso': ['Média', 'Baixa', 'Alta', 'Alta', 'Baixa', 'Média', 'Média', 'Baixa', 'Alta', 'Alta'],
    'tempo_espera': [30, 20, 40, 50, 15, 45, 30, 20, 35, 60],
    'tempo_atendimento': [15, 10, 25, 35, 5, 20, 15, 10, 20, 30]
})

# Pré-processamento dos dados
X = queue_data[['tempo_espera', 'tempo_atendimento']]

# Aplicação do algoritmo K-means para identificar clusters de atendimento
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)

# Adicionando a coluna de cluster ao DataFrame
queue_data['cluster'] = kmeans.labels_

# Identificação dos padrões de espera
waiting_patterns = queue_data.groupby('cluster').mean()['tempo_espera']

print(waiting_patterns)

```

O código fornecido realiza a identificação de padrões de espera usando o algoritmo K-means, com base nos dados de filas de atendimento presentes no DataFrame queue_data. Vou explicar linha por linha para facilitar o entendimento:

```python
Copy code
import pandas as pd
from sklearn.cluster import KMeans
```
Essas linhas importam as bibliotecas necessárias: pandas para manipulação de dados em formato de DataFrame e KMeans do sklearn.cluster para realizar o algoritmo de agrupamento K-means.

```python
Copy code
queue_data = pd.DataFrame({
    'horario_chegada': ['09:15', '09:30', '09:45', '10:00', '10:15', '18:00', '18:15', '18:30', '18:45', '19:00'],
    'gravidade_caso': ['Média', 'Baixa', 'Alta', 'Alta', 'Baixa', 'Média', 'Média', 'Baixa', 'Alta', 'Alta'],
    'tempo_espera': [30, 20, 40, 50, 15, 45, 30, 20, 35, 60],
    'tempo_atendimento': [15, 10, 25, 35, 5, 20, 15, 10, 20, 30]
})
```
Essa parte cria o DataFrame queue_data com as informações das filas de atendimento. Cada coluna representa uma informação: horario_chegada é o horário de chegada dos pacientes, gravidade_caso é a gravidade do caso, tempo_espera é o tempo de espera e tempo_atendimento é o tempo de atendimento.

```python
Copy code
X = queue_data[['tempo_espera', 'tempo_atendimento']]
```
Essa linha seleciona as colunas 'tempo_espera' e 'tempo_atendimento' do DataFrame queue_data e armazena em X, que será utilizado como entrada para o algoritmo K-means.

```python
Copy code
kmeans = KMeans(n_clusters=2)
kmeans.fit(X)
```
Essas linhas criam uma instância do algoritmo K-means com n_clusters=2, indicando que queremos identificar dois clusters. Em seguida, o algoritmo é treinado com os dados X usando o método fit().

```python
Copy code
queue_data['cluster'] = kmeans.labels_
```
Essa linha adiciona uma nova coluna chamada 'cluster' ao DataFrame queue_data e atribui os rótulos dos clusters identificados pelo K-means aos exemplos do conjunto de dados.

```python
Copy code
waiting_patterns = queue_data.groupby('cluster').mean()['tempo_espera']
```
Essa linha agrupa os dados por cluster usando o método groupby(), calcula a média do tempo de espera para cada cluster usando o método mean(), e retorna apenas a coluna 'tempo_espera'. O resultado é armazenado em waiting_patterns.

```python
Copy code
print(waiting_patterns)
```
Por fim, essa linha exibe os padrões de espera identificados, ou seja, as médias do tempo de espera para cada cluster.

Esse código demonstra um exemplo básico de como utilizar o algoritmo K-means para identificar padrões