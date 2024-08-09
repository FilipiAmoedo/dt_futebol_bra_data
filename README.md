# Data Futebol 

Nesse projeto eu trabalho um dataset que contém o historico dos jogos do brasileirao de 2012 ate os dias de hoje sendo atualizado toda semana a cada rodada que passa, eu baixo e coloco em um banco de dados na minha maquina.

Com isso eu faço algumas analises com eles, como gerando a a tabela de classificaçao dos anos, historico dos confrontos entre um equipe e outra, quantidades de vitorias dentro e fora de casda e quantidade de gols dentro e fora de casa

### Problemas encontrado nos dados:
* Em 2016 no ultimo jogo entre Chapecoense e Atletico-Mg, teve um WO duplo, pois ocorreu um dos acidentes mais tragicos do futebol que foi a queda do avião do time da chapecoenese, por isso o time de chapeco e o Atletico-MG resolveram não jogar o jogo, resultando em um WO para as duas equipes
    * Eu resolvi tratando esse jogo com um empate em 0 a 0 e a coluna Res com D e adicionando uma coluna WO, que caso tenha um jogo esteja vazio a coluna AG e a HG, temos um WO.\
                    
            Em classificação acabei diminuindo 1 ponto das duas equiipes e tirando o empate, pois WO duplo não é um empate e sim uma derrota para os 2 times,
            e por isso adicionei mais uma derrota para os 2 times 
  