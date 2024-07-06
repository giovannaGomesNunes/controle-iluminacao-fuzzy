import skfuzzy as fuzzy
import universo_variaveis as universo

# funções de pertinência para as variáveis
universo.luminosidade_natural['escuro'] = fuzzy.trimf(universo.luminosidade_natural.universe, [0, 0, 45])
universo.luminosidade_natural['medio'] = fuzzy.trapmf(universo.luminosidade_natural.universe, [10, 50, 60, 90])
universo.luminosidade_natural['claro'] = fuzzy.trimf(universo.luminosidade_natural.universe, [65, 100, 100])

universo.deteccao_presenca['ausente'] = fuzzy.trimf(universo.deteccao_presenca.universe, [0, 0, 40])
universo.deteccao_presenca['baixo'] = fuzzy.trapmf(universo.deteccao_presenca.universe, [5, 30, 50, 90])
universo.deteccao_presenca['alto'] = fuzzy.trimf(universo.deteccao_presenca.universe, [60, 100, 100])

universo.temperatura_ambiente['frio'] = fuzzy.trimf(universo.temperatura_ambiente.universe, [0, 0, 25])
universo.temperatura_ambiente['confortavel'] = fuzzy.trapmf(universo.temperatura_ambiente.universe, [10, 20, 30, 40])
universo.temperatura_ambiente['quente'] =  fuzzy.trimf(universo.temperatura_ambiente.universe, [30, 50, 50])

universo.preferencia_usuarios['baixo'] = fuzzy.trimf(universo.preferencia_usuarios.universe, [0, 0, 30])
universo.preferencia_usuarios['medio'] = fuzzy.trapmf(universo.preferencia_usuarios.universe, [10, 40, 60, 90])
universo.preferencia_usuarios['alto'] = fuzzy.trimf(universo.preferencia_usuarios.universe, [70, 100, 100])

universo.horario_dia['manha'] = fuzzy.trimf(universo.horario_dia.universe, [0, 0, 12])
universo.horario_dia['tarde'] = fuzzy.trapmf(universo.horario_dia.universe, [6, 12, 18, 24])
universo.horario_dia['noite'] = fuzzy.trimf(universo.horario_dia.universe, [18, 24, 24])

universo.nivel_atividade['baixo'] = fuzzy.trimf(universo.nivel_atividade.universe, [0, 0, 30])
universo.nivel_atividade['medio'] = fuzzy.trapmf(universo.nivel_atividade.universe, [20, 50, 50, 80])
universo.nivel_atividade['alto'] = fuzzy.trimf(universo.nivel_atividade.universe, [70, 100, 100])

universo.idade_usuarios['jovem'] = fuzzy.trimf(universo.idade_usuarios.universe, [0, 0, 40])
universo.idade_usuarios['adulto'] = fuzzy.trapmf(universo.idade_usuarios.universe, [20, 40, 60, 80])
universo.idade_usuarios['idoso'] = fuzzy.trimf(universo.idade_usuarios.universe, [60, 100, 100])

universo.intensidade_iluminacao['baixo'] = fuzzy.trimf(universo.intensidade_iluminacao.universe, [0, 0, 40])
universo.intensidade_iluminacao['medio'] = fuzzy.trapmf(universo.intensidade_iluminacao.universe, [10, 45, 55, 90])
universo.intensidade_iluminacao['alto'] = fuzzy.trimf(universo.intensidade_iluminacao.universe, [60, 100, 100])
