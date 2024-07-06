from skfuzzy import control as ctrl
import funcoes_pertinencia
import universo_variaveis as universo

# Regras de Luminosidade Natural
regra1 = ctrl.Rule((universo.luminosidade_natural['escuro'] | universo.luminosidade_natural['medio'] | universo.luminosidade_natural['claro']) 
                   & universo.deteccao_presenca['ausente'], universo.intensidade_iluminacao['baixo'])

regra2 = ctrl.Rule(universo.luminosidade_natural['medio'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['medio'])
regra3 = ctrl.Rule(universo.luminosidade_natural['claro'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['baixo'])

# Regras de Preferência de Usuários
regra4 = ctrl.Rule((universo.preferencia_usuarios['baixo'] | universo.preferencia_usuarios['medio'] | universo.preferencia_usuarios['alto']) 
                   & universo.deteccao_presenca['ausente'], universo.intensidade_iluminacao['baixo'])

regra5 = ctrl.Rule(universo.preferencia_usuarios['baixo'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['baixo'])
regra6 = ctrl.Rule(universo.preferencia_usuarios['medio'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['medio'])
regra7 = ctrl.Rule(universo.preferencia_usuarios['alto'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])

regra8 = ctrl.Rule(universo.preferencia_usuarios['baixo'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['baixo'])
regra9 = ctrl.Rule(universo.preferencia_usuarios['medio'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['medio'])
regra10 = ctrl.Rule(universo.preferencia_usuarios['alto'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

# Regras de Temperatura Ambiente
regra11 = ctrl.Rule((universo.temperatura_ambiente['quente'] | universo.temperatura_ambiente['confortavel'] | universo.temperatura_ambiente['frio']) 
                    & universo.deteccao_presenca['ausente'], universo.intensidade_iluminacao['baixo'])

regra12 = ctrl.Rule(universo.temperatura_ambiente['quente'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])
regra13 = ctrl.Rule(universo.temperatura_ambiente['quente'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

regra14 = ctrl.Rule(universo.temperatura_ambiente['confortavel'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])
regra15 = ctrl.Rule(universo.temperatura_ambiente['confortavel'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

regra16 = ctrl.Rule(universo.temperatura_ambiente['frio'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])
regra17 = ctrl.Rule(universo.temperatura_ambiente['frio'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

# Regras para Horário do Dia
regra18 = ctrl.Rule(universo.horario_dia['manha'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['baixo'])
regra19 = ctrl.Rule(universo.horario_dia['tarde'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['medio'])
regra20 = ctrl.Rule(universo.horario_dia['noite'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

# Regras para Nível de Atividade
regra21 = ctrl.Rule(universo.nivel_atividade['baixo'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['baixo'])
regra22 = ctrl.Rule(universo.nivel_atividade['medio'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['medio'])
regra23 = ctrl.Rule(universo.nivel_atividade['alto'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['alto'])

regra24 = ctrl.Rule(universo.nivel_atividade['baixo'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['baixo'])
regra25 = ctrl.Rule(universo.nivel_atividade['medio'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['medio'])
regra26 = ctrl.Rule(universo.nivel_atividade['alto'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

# Regras para Idade dos Usuários
regra27 = ctrl.Rule(universo.idade_usuarios['jovem'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['medio'])
regra28 = ctrl.Rule(universo.idade_usuarios['jovem'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

regra29 = ctrl.Rule(universo.idade_usuarios['adulto'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['medio'])
regra30 = ctrl.Rule(universo.idade_usuarios['adulto'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['alto'])

regra31 = ctrl.Rule(universo.idade_usuarios['idoso'] & universo.deteccao_presenca['baixo'], universo.intensidade_iluminacao['baixo'])
regra32 = ctrl.Rule(universo.idade_usuarios['idoso'] & universo.deteccao_presenca['alto'], universo.intensidade_iluminacao['medio'])

# Realizando inferências das regras
iluminacao = ctrl.ControlSystem([
    regra1, regra2, regra3, regra4, regra5, regra6, regra7, regra8, regra9, regra10,
    regra11, regra12, regra13, regra14, regra15, regra16, regra17, regra18, regra19,
    regra20, regra21, regra22, regra23, regra24, regra25, regra26, regra27, regra28,
    regra29, regra30, regra31, regra32
])

valores = ctrl.ControlSystemSimulation(iluminacao)

