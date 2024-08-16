<div align="center">


# ALGORITMOS PSO E AG PARA ENCONTRAR MÍNIMOS GLOBAIS DE FUNÇÕES COMPLEXAS

TRABALHO DA DISCIPLINA DE OMTIZAÇÃO DE SISTEMAS (DCA0115)</br>
POR MINNAEL CAMPELO DE OLIVEIRA 

</div>



## 1. PROBLEMÁTICA
<div style="text-align: justify;">
No contexto da otimização matemática, encontrar o mínimo global de uma função complexa e não linear é uma tarefa desafiadora e de grande importância em diversas áreas, como engenharia, economia e ciência de dados. O problema em questão é a minimização da seguinte função: </br></br> 

<div align="center">

<img src="Imagens/figura1.png" width="550" height="70" alt="Descrição da Imagem" /></br> 
Figura 1 - Função objetivo a ser minimizada.
</div></br> 



Vale salientar que essa função apresenta características de múltiplos mínimos locais devido à sua natureza oscilatória e a presença de termos envolvendo seno e raiz quadrada, o que faz com que seja difícil localizar o mínimo global utilizando métodos de otimização clássicos devido à possibilidade de convergência para mínimos locais. Nesse cenário, surge a necessidade de empregar algoritmos de otimização estocásticos e bioinspirados, como o Algoritmo de Otimização por Enxame de Partículas (PSO) ou Algoritmos Genéticos (AG), que possuem maior potencial para escapar de mínimos locais e localizar a solução global. Dessa forma, para melhor compreensão do comportamento da função segue abaixo uma imagem representativa:

<div align="center">
<img src="Imagens/figura2.png" width="550" height="400" alt="Descrição da Imagem" /></br> 
Figura 2 - Esboço da função com a melhor qualidade possível.
</div></br> 

Obs: Os intervalos grandes foram definidos com objetivo de deixar a melhor qualidade de imagem possível.
</div>



## 2 DESENVOLVIMENTO
Para comprir com o objetivo desejado que é de encontrar o mínimo global da função mostrada anteriormente foram utilizados dois tipos de algoritmos: o algoritmo de PSO(Particle Swarm Optimization) e um algoritmo genético. 

### 2.1 PSO (PARTICLE SWARM OPTIMIZATION)
<div style="text-align: justify;">
O Algoritmo de Otimização por Enxame de Partículas (PSO) é uma técnica de otimização inspirada no comportamento social de pássaros e peixes. Desenvolvido por James Kennedy e Russell Eberhart em 1995, o PSO é utilizado para encontrar a melhor solução em problemas complexos de otimização. No PSO, um conjunto de partículas é distribuído por um espaço de solução. Cada partícula representa uma possível solução e move-se pelo espaço baseado em sua própria experiência e na de suas vizinhas. As partículas atualizam suas posições com base em duas informações principais: a melhor solução já encontrada por ela mesma (melhor posição pessoal) e a melhor solução encontrada pelo grupo (melhor posição global). O processo é iterativo, com partículas ajustando suas velocidades e posições a cada iteração para explorar e refinar o espaço de soluções. O objetivo é encontrar a solução ótima global, maximizando ou minimizando a função objetivo. O PSO é eficiente em encontrar soluções próximas do ótimo global para uma ampla gama de problemas, incluindo aqueles com múltiplos mínimos locais e espaços de solução complexos.
</div></br>
<strong>Parâmetros utilizados dentro do algoritmo PSO:</strong> </br></br><blockquote>
-> Limites: [-500, 500];</br>
-> Quantidade de partículas: 15; </br>
-> Número de iterações: 40; </br>
-> Cognitivo (C1): 2; </br>
-> Social (C2): 2; </br>
</blockquote></br>


Para o fator de inércia foi utilizada a técnica de redução linear da ponderação da inércia dado por:

<div align="center">
<img src="Imagens/figura3.png" width="550" height="100" alt="Descrição da Imagem" /></br> 
Figura 3 - Redução linear da ponderação da inércia.
</div></br> 

Sendo <strong>Wmax = 0.9</strong> e  <strong>Wmin = 0.4</strong> 


### 2.2 ALGORITMOS GENÉTICOS
<div style="text-align: justify;">
Os Algoritmos Genéticos (AG) são técnicas de otimização inspiradas na evolução biológica e na seleção natural. Desenvolvidos por John Holland na década de 1960, eles são usados para encontrar soluções para problemas complexos que podem ser difíceis de resolver por métodos tradicionais. Em um Algoritmo Genético, uma população de soluções possíveis, representadas como "indivíduos" ou "cromossomos", evolui ao longo de várias gerações. Cada indivíduo é avaliado com base em uma função de aptidão, que determina sua qualidade ou adequação para resolver o problema em questão.
Os algoritmos genéticos aplicam operações de seleção, cruzamento (crossover) e mutação para gerar novas soluções. A seleção escolhe os melhores indivíduos para reproduzir, o cruzamento combina características de pares de indivíduos para criar novos candidatos, e a mutação introduz variações aleatórias para explorar novas partes do espaço de solução. Esse processo iterativo permite que o algoritmo converja para soluções ótimas ou quase ótimas, mesmo em problemas com grandes espaços de busca e muitos mínimos locais. Os algoritmos genéticos são amplamente aplicados em áreas como engenharia, otimização de processos e inteligência artificial, oferecendo uma abordagem robusta para a resolução de problemas complexos.
</div></br>
<Strong>Parâmetros utilizados dentro do algoritmo genético:</Strong></br></br>
<blockquote>
-> Limites: [-500, 500];</br>
-> População: 250; </br>
-> Número de gerações: 250;; </br>
-> Taxa de mutação: 1% </br>
-> Taxa de cruzamento (crossover): 70%; </br>
</blockquote></br>

## 3. RESULTADOS
<div style="text-align: justify;">
Para fazer uma comparação dos algoritmos foram realizadas 20 tentativas em cada, visando o nível avaliar o tempo de resposta, a complexidade, a precisão e a consistência. Dado os parâmetros avaliados acima ambos os algoritmos tiveram um desempenho excelente, no entanto o que chegou a diferenciar os dois foi a consistência e precisão. O algoritmo PSO teve uma precisão de excelência porém em alguns momentos se perdeu em um mínimo local e acabou não dando um resultado tão satisfatório. O algoritmo genético sempre deu resultados consistentes e bem próximos do mínimo global, no entanto não chegou ao valor exato em quase nenhuma das tentativas e ainda chegou a dar um valor intermediário em uma tentativa.
Para uma definição melhor dos resultados obtidos a nível de artigo, seria necessário fazer um gráfico de resultados obtidos para cada algoritmo possibilitando assim um comparativo, no entanto não se faz necessário dado que os códigos para teste práticos se encontram no seguinte repositório da plataforma GitHub que também irá possuir um passo a passo de como fazer a execução do código e as ferramentas necessárias, além disso a discussão/comprovação dos resultados pode ficar para a apresentação.
</div>


## 4. CONCLUSÃO
<div style="text-align: justify;">
O trabalho foi realizado com excelência e conseguiu obter resultados satisfatórios e esperados pela literatura dos algoritmos genéticos e do algoritmo PSO tendo em vista que seguiu todas as regras descritas no princípio de funcionamento de ambos os algoritmos e também a função e os limites definidos pela tarefa. A nível de avaliação individual do trabalho é possível definir como uma tarefa extremamente importante no que tange aos conhecimentos descritos na disciplina de otimização de sistemas.
