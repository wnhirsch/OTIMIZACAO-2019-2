Mirrored Traveling Tournament Problem (mTTP)
=======

#### Definição: 
O Mirrored Traveling Tournment Problem consiste em organizar a
agenda das partidas de um torneio esportivo, decidindo quais cidades devem sedear cada um dos confrontos. Cada equipe do problema possui uma cidade-sede própria, e quando a equipe compete em sua própria cidade, diz-se que ela está “em casa”. Do contrário, a equipe está “fora de casa”. O torneio é organizado em dois turnos, cada um com exatamente (número de equipes - 1) rodadas. Como consequência, cada equipe enfrenta as demais exatamente uma vez por turno. Os dois turnos são ditos espelhados: os confrontos de cada rodada do primeiro turno são exatamente os mesmos do segundo turno, mas o status de “fora” e “em casa” das equipes são espelhados. Por exemplo, se a equipe E1 confronta a E2 “em casa” na primeira rodada do primeiro turno, ela também enfrenta E2 na primeira rodada do segundo turno e, dessa vez, é a equipe E2 que joga “em casa”. Adicionalmente, uma equipe não pode participar além de três confrontos seguidos “em casa” ou “fora de casa”, em qualquer um dos turnos do torneio.

#### Solução:
Agenda dos confrontos do torneio, com detalhes da cidade em que os confrontos ocorrem.

#### Objetivo: 
Minimizar a distância total percorrida pelas equipes para a execução do torneio esportivo.

#### Instâncias: 
As instâncias do mTTP são matrizes quadrada com as distâncias entre todos os pares de cidades do problema. O nome das instâncias inclui algum contexto de onde elas foram retiradas, bem como o número de equipes consideradas no problema. Os melhores valores de solução conhecidos (BKS) foram extraídos de [Santos e Carvalho (2018)](https://proceedings.science/sbpo/papers/algoritmo-genetico-aplicado-a-otimizacao-do-planejamento-de-torneios-esportivos) e uma formulação matemática do problema pode ser encontrada em [Carvalho e Lorena (2012)](https://www.sciencedirect.com/science/article/abs/pii/S0360835212001726).

| Instância | BKS    |
|-----------|-------:|
|[NL4](instancias/N4.txt)             | 8276   |
|[NL6](instancias/N6.txt)             | 26588  |
|[NL8](instancias/N8.txt)             | 41928  |
|[NL10](instancias/N10.txt)           | 63832  |
|[NL12](instancias/N12.txt)           | 119608 |
|[NL14](instancias/N14.txt)           | 199363 |
|[circ6](instancias/circ6.txt)        | 72     |
|[circ8](instancias/circ8.txt)        | 140    |
|[circ10](instancias/circ10.txt)      | 272    |
|[circ12](instancias/circ12.txt)      | 432    |

__Nota :__ As instâncias foram espelhadas da biblioteca [Challenge Traveling Tournament Instances](https://mat.gsia.cmu.edu/TOURN/) e para mais informações acesse o [Enunciado Completo](utils/enunciado.pdf).

__Nota2 :__ Informações sobre o algoritmo Simulated Annealing podem ser vistas na [Wikipedia](https://en.wikipedia.org/wiki/Simulated_annealing) ou nesses [Slides sobre o conteúdo](utils/SA_slides.pdf) feito pelo Prof Bruno

__Nota3 :__ Link para o repositório no [repl.it](https://repl.it/join/eqzuxvbd-wnhirsch) com o código em Python.

__Nota4 :__ Link para implementação do [Simulated Anealing](https://arxiv.org/pdf/1311.1884.pdf) baseado no mTTP
