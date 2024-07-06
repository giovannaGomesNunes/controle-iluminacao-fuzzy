# controle-iluminacao-fuzzy
Trabalho1 AMMCI Projeto de controle de iluminação utilizando lógica fuzzy


#Equipe: Giovanna Gomes Nunes RA 107611
#Equipe: Giovanna Gomes Nunes RA 107611
#Universidade Estadual de Maringá
#Disciplina: APRENDIZAGEM DE M.E M.DE C.INCERTO
#Título do Trabalho: Sistema de Controle de Iluminação Adaptável Utilizando Lógica Fuzzy
#Professor: Wagner Igarashi


Descrição do Problema
O problema abordado neste projeto consiste na implementação de um sistema de controle de iluminação adaptável utilizando lógica fuzzy. O objetivo é desenvolver um sistema que ajuste automaticamente a intensidade da iluminação com base em múltiplas variáveis ambientais e de preferência dos usuários. As variáveis consideradas incluem luminosidade natural, detecção de presença, temperatura ambiente e preferência dos usuários, cada uma influenciando a decisão final de ajuste da iluminação. A importância desse sistema reside na capacidade de oferecer conforto e eficiência energética em ambientes diversos, adaptando-se dinamicamente às condições do ambiente e às preferências dos usuários.

Ferramenta Utilizada
Para o desenvolvimento deste sistema de controle fuzzy, optou-se pelo uso da linguagem de programação Python devido à sua ampla adoção na área de computação científica e inteligência artificial. Python oferece uma vasta gama de bibliotecas e ferramentas especializadas em lógica fuzzy, como o scikit-fuzzy, que facilita a implementação de sistemas fuzzy de forma eficiente e intuitiva. Além disso, Python é conhecido por sua legibilidade e facilidade de prototipagem, o que é crucial para o desenvolvimento ágil e iterativo de sistemas complexos como este.

Dados do Computador
Processador	11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz   2.42 GHz
RAM instalada	8,00 GB 
Tipo de sistema	Sistema operacional de 64 bits, processador baseado em x64


Explicação do Algoritmo
O algoritmo implementado utiliza princípios avançados de lógica fuzzy para inferir a intensidade ideal de iluminação com base em diversas variáveis de entrada que capturam as nuances ambientais e as preferências dos usuários. A lógica fuzzy oferece uma abordagem flexível e intuitiva para lidar com incertezas e variações, comparada às metodologias tradicionais baseadas em lógica booleana. Abaixo, detalhamos os passos principais que compõem esse processo:

Definição das Variáveis Linguísticas:
Cada variável de entrada essencial (luminosidade natural, detecção de presença, temperatura ambiente e preferência dos usuários) é traduzida em conjuntos difusos, os quais representam termos linguísticos como "escuro", "médio" e "alto". Isso permite uma descrição mais próxima das percepções humanas e das condições ambientais variáveis.

Definição das Funções de Pertinência:
Para cada variável, são definidas funções de pertinência que especificam como os valores numéricos se relacionam com os conjuntos difusos. Por exemplo, funções como trimf (triangular) e trapmf (trapezoidal) são utilizadas para modelar faixas específicas de valores, como "médio" ou "confortável", de acordo com a interpretação subjetiva de cada variável.

Estabelecimento das Regras de Inferência:
As regras de inferência são formuladas para orientar a tomada de decisão com base nos termos linguísticos associados às variáveis de entrada. Por exemplo, uma regra poderia ser "Se a luminosidade natural é escura E a detecção de presença é ausente, então a intensidade de iluminação deve ser baixa". Essas regras capturam o conhecimento especializado e a lógica de como ajustar a iluminação com base nas condições observadas.

Execução do Sistema de Controle Fuzzy:
Utilizando um sistema de controle fuzzy, as regras definidas são aplicadas para calcular a intensidade de iluminação ideal. Esse processo inclui a etapa de defuzzificação, onde os resultados fuzzy são convertidos em valores claros e acionáveis. Isso permite que o sistema adapte dinamicamente a iluminação, otimizando tanto o conforto dos usuários quanto a eficiência energética do ambiente.

Casos de Teste

Caso de Teste 1:
Entradas:
Luminosidade natural: 70
Detecção de presença: 40
Temperatura ambiente: 25°C
Preferência de usuários: 80
Horário do dia: Tarde (1)
Nível de atividade: 60
Idade dos usuários: Adulto (1)

Caso de Teste 2:
Entradas:
Luminosidade natural: 20
Detecção de presença: 80
Temperatura ambiente: 15°C
Preferência de usuários: 30
Horário do dia: Noite (2)
Nível de atividade: 20
Idade dos usuários: Jovem (0)
