import numpy as nmp
from skfuzzy import control as ctrl

#universo de todas as variáveis são de  0 a 100 
luminosidade_natural = ctrl.Antecedent(nmp.arange(0, 101, 1), 'luminosidade_natural') #universo de valores de 0 a 100
deteccao_presenca = ctrl.Antecedent(nmp.arange(0, 101, 1), 'deteccao_presenca') 
temperatura_ambiente = ctrl.Antecedent(nmp.arange(0, 51, 1), 'temperatura_ambiente') 
preferencia_usuarios = ctrl.Antecedent(nmp.arange(0, 101, 1), 'preferencia_usuarios') 
intensidade_iluminacao = ctrl.Consequent(nmp.arange(0, 101, 1), 'intensidade_iluminacao', 'centroid') #define o método de deffuzificação como centróide

# novas variáveis
horario_dia = ctrl.Antecedent(nmp.arange(0, 24, 1), 'horario_dia')  # intervalo de 0 a 24 horas
nivel_atividade = ctrl.Antecedent(nmp.arange(0, 101, 1), 'nivel_atividade')
idade_usuarios = ctrl.Antecedent(nmp.arange(0, 101, 1), 'idade_usuarios')