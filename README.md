# Projeto para Submissão na Competição [Data Science Challenge at EEF 2024](https://www.kaggle.com/competitions/data-science-challenge-at-eef-2024)

## Equipe:
- Eduardo Zaffari Monteiro - eduardozaffarimonteiro@usp.br
- Pedro Henrique de Freitas Maçonetto - pedromaconetto@usp.br

### Explicação dos Notebooks

#### Preparação dos Dados

Os dados meteorológicos foram convertidos utilizando o metpy, foram removidas as variáveis que apresentavam grande falta de dados, enquant as demais foram preenchidas utilizando o KNNImputer. 
As imagens foram coletadas e cortadas conforme estratégia pessoal, em que o aeroporto de origem era recortado, considerando sua geolocalizacao, gerando uma nova imagem de 500x500, que era por fim redimensionada para 244x244 e guardada em um diretorio.

#### Modelos 15+

Os melhores modelos que encontramos nas bases de teste e em testes na plataforma do kaggle 'Public', o modelo utilizado na submissão foram os 2 modelos XGBoost encontrados nessa pasta.

#### CNN, LightGBM, XGBoost_Loss, CatBoost...

Modelos que foram testados nos dados mas em última instância não foram os submetidos, no ranking final alguns desses modelos venceram os modelos utilizados por nós, e teriam nos colocado em segundo na competição,  consideramos que foi falta de validação cruzada (KFold) em conjunto com análises apenas superficiais dos modelos que nos levaram a escolher os modelos errados para submissão. Aprendemos com isso e erros como esses serão evitados em futuros projetos.

#### Redes Neurais 5+

A rede neural utilizada foi montada de forma personalizada, contando com uma resnet para as imagens e camadas densas para as variaveis.
Ex:

Resnet - Dense -   
.....................................\\  
....................................... Dense - SoftMax  
..................................../   
................ Dense -  

A rede foi treinada mantendo os parametros da resnet fixos. Durante o treinamento houveram variações nos otimizadores (Adam e SGBD) com diferentes taxas de aprendizagem e regularização, além de variações nas funções de loss (CrossEntropy e FocalLoss) também com diferentes parâmetos específicos.
O resultado final não foi tão satisfatório quanto o dos modelos de boosting.
