import json
import pandas as pd


#Carregando as bases
historico = pd.read_csv('historico_atendimento.csv')
perfil = json.load(open('perfil_investidor.json'))
produtos = json.load(open('produtos_financeiros.json'))
transacoes = pd.read_csv('transacoes.csv')

#Montar contexto

contexto = f"""

CLIENTE:{perfil['nome']}, {perfil['idade']} anos, perfil{perfil['perfil_investidor']}
OBJETIVO: {perfil['objetivo_principal']}
PATRIMONIO: R$ {perfil['patrimonio_total']} | RESERVA R$ {perfil['reserva_emergencia_atual']}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONIVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

#System Prompt

system_prompt = f""" 
ESCREVER AQUI O PROMPT
"""

#Chamar o Ollama

def perguntar(msg):
    prompt = f"""
"""