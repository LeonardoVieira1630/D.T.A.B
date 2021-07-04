
<h1>
  :fire: D.T.A.B  :fire:
</h1>

&nbsp;
<p align="center">
  <img alt="GitHub language count" src=https://img.shields.io/github/languages/count/LeonardoVieira1630/D.T.A.B>

   <a href="https://github.com/LeonardoVieira1630/">
    <img alt="Author" src="https://img.shields.io/badge/author-Leonardo%20Vieira-red">
  </a>
  
   <a href="https://github.com/LeonardoVieira1630/">
    <img alt="Author" src="https://img.shields.io/badge/author-Julio%20Milani-red">
  </a>
  
  <img alt="GitHub language count" src="https://img.shields.io/github/languages/top/LeonardoVieira1630/D.T.A.B.svg">
  
 
</p>

<p align="center">
  <a>Descrição</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a>Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a>Objetivos</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a>Instalação</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a>Resultados</a>&nbsp;&nbsp;&nbsp;

</p>

<br>


## :robot: Descrição  

D.T.A.B (Day Trade Asynchronous Bot) é um software desenvolvido em JavaScript para ser capaz de fazer operações de compra e venda de criptomoedas. Alem disso, ele tem autonomia de decisão nas transações pois é capaz de jugar o melhor momento de faze-las.

Para montar a lógica do robô e torna-lo realmente eficiente, levamos em consideração os conceitos apresentados em:

- **The Axioms of Zurich** – Max Gunther.

- **Technical Analysis of the Financial Markets: A Comprehensive Guide to Trading Methods and Applications** - John J. Murphy.

&nbsp;
## :rocket: Tecnologias 

Esse projeto foi desenvolvido com:

- **JavaScript**

- **Node.js**



O node é onde o bot irá rodar. Para baixar o programa use esse link aqui: 

https://nodejs.org/pt-br/download/



Para o perfeito funcionamento do código é necessários os frameworks :
- **Axios**
- **dotenv**

&nbsp;
## :ghost: Objetivos 

O D.T.A.B foi construído como projeto final da disciplina de Projeto de Eletrônica 1 do curso de Engenharia eletrônica da Universidade federal de Santa Catarina.

A finalidade do projeto era fazer um software totalmente autônomo que gerencie e faça investimento. Para o funcionamento dele, tivemos que estudar e aprender vários tópicos importantes como:

- Funcionamento e uso da Raspberry pi 3.

- Comunicação entre diferentes APIs.

- Conceitos e técnicas de mercado financeiro e criptomoedas.



&nbsp;
## :computer: Instalação 

Para usar o Bot, voce deve clonar esse repositório. Vá até seu terminal e use:
```bash
 git clone https://github.com/Ffquenome/D.T.A.B.git
```
Depois disso, faça o download das dependências usadas com os seguinte comando:
```bash
 npm i
```
Agora, você deve criar um arquivo .env com as seguintes informações:
```javaScript
API_URL = 'https://api.binance.com/api'
API_KEY = XXXX
SECRET_KEY = XXXX
CRAWLER_INTERNAL = 3000
PROFITABILITY = 1.1
```

Por ultimo, é necessário criar uma conta na Binance e pegar seu API_KEY e sua SECRET_KEY. Assim que você tiver essas informações preencha no arquivo .env que criou. Com esses dados, o bot usára sua conta para fazer as transações para você.

Para fazer a conta recomendo seguir esses passos: 

https://www.binance.com/pt-BR/support/faq/360002502072

Et voilà mon ami!! Tudo pronto.



&nbsp;
## :coffee: :ballot_box_with_check: Resultados: 
Esse tópico é reservado para os resultados e testes feito com o D.T.A.B.. Estás pensando em usa-lo para optimizar seus investimentos e ganhos? Então da uma olhada ai nos resultados que ele ja fez.
