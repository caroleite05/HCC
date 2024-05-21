# HCC

***PREVISÃO ACERCA DA SOBREVIVÊNCIA DE PACIENTES COM CARCINOMA HEPATOCELULAR***

<img width="669" alt="Captura de ecrã 2024-05-21, às 21 08 59" src="https://github.com/caroleite05/HCC/assets/166618304/02f97056-fa55-4117-b0ed-1d78d501a2ed">

***Introdução***
<br>
O HCC(carcinoma hepatocelular) é o tipo mais comum e grave de cancro no fígado,e origina-se nas células hepáticas(células parenquimatosas do fígado). Por este motivo, é necessário um rastreio mais eficaz e um diagnóstico precoce desta doença, de modo a que possam ser reduzidos os riscos potencialmente causados pela mesma, e salvar vidas de pacientes. Para isto, com o desenvolvimento do nosso projeto, são elaboradas técnicas de supervised learning para uma melhor compreensão das variáveis importantes a serem consideradas, e assim prever a sobrevivência dos pacientes. 
Para o efeito, usamos  diversos algoritmos e métodos. Realizamos uma análise detalhada dos dados, incluindo pré-processamento, análise exploratória e definição do alvo (target). Para a classificação, aplicamos os algoritmos KNN e Decision Tree, e para lidar com desequilíbrios nas classes, aplicamos a técnica SMOTE. Além disso, fizemos testes com diferentes configurações de dados e dividimos os dados em conjuntos de treino e teste para validação. A importância das variáveis foi avaliada para entender quais as características  que mais influenciam na sobrevivência dos pacientes. Realizamos também uma comparação visual dos resultados obtidos com KNN e Decision Tree, utilizando gráficos para interpretar a performance dos modelos. Finalmente, ajustamos os parâmetros (tuning) para otimizar o desempenho dos algoritmos.

***Ficheiros utilizados:***
  - **hcc_dataset.csv:** conjunto de dados iniciais
  - **hcc_dataset_filled.csv:** conjunto de dados já preenchidos
  - **HCC.ipynb:** código implementado com os modelos aplicados
  - **app.py:** implementação de uma aplicação para prever se uma pessoa irá "morrer" ou "viver" após 1 ano do diagnóstico de acordo com os seus dados

***Requisitos:***
Para executar o programa, é aconselhável a utilização do ambiente Anaconda, de modo a que a visualização do projeto possa conter as bibliotecas de Python utilizadas no seu desenvolvimento. Estas bibliotecas são:
  - Pandas
  - Numpy
  - Scikit-learn
  - Matplotlib e searborn
  - Jupyter notebook

Para aceder à aplicação de previsão, deve escrever o seguinte comando:
<br>
   > **streamlit run app.py**

***Referências***
https://github.com/Dr-Salcedo/hepatocellular_carcinoma_one_year_survival

  
## Autores 

* **Beatriz Pereira** - *Bioinformática - FCUP* - [Beapereirax](https://github.com/Beapereirax) 
* **Carolina Leite** - *Bioinformática - FCUP* - [caroleite05](https://github.com/caroleite05)
* **Inês Santos** - *Bioinformática - FCUP* - [up202305589](https://github.com/up202305589)

Elementos de Inteligência Artificial e Ciência de Dados - FCUP - 2023/2024 
