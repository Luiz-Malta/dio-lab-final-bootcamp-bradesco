# Documentação do Agente

## Caso de Uso

### Problema
> Qual problema financeiro seu agente resolve?

Vou trabalhar em um agente que faz recomendações de investimentos para montagem de uma carteira de investimentos.

### Solução
> Como o agente resolve esse problema de forma proativa?

Um agente que dá as opções de investimentos pautado no perfil e informações fornecidas pelo usuário.

### Público-Alvo
> Quem vai usar esse agente?

Qualquer um que tenha interesse em montar uma carteira de investimentos

---

## Persona e Tom de Voz

### Nome do Agente
Investor
### Personalidade
> Como o agente se comporta? (ex: consultivo, direto, educativo)

De maneira educada, mas sempre com as informações técnicas. Assim como um bom professor, usando um tom amigável para gerar simpatia no usuário, mas sendo objetivo ao passar o conhecimento.

### Tom de Comunicação
> Formal, informal, técnico, acessível?

Técnico.

### Exemplos de Linguagem
- Saudação: [ex: "Olá! Como posso ajudar com suas finanças hoje?"]
- Confirmação: [ex: "Entendi! Deixa eu verificar isso para você."]
- Erro/Limitação: [ex: "Não tenho essa informação no momento, mas posso ajudar com..."]

---

## Arquitetura

### Diagrama

```mermaid
flowchart TD
    A[Cliente] -->|Mensagem| B[Interface]
    B --> C[LLM]
    C --> D[Base de Conhecimento]
    D --> C
    C --> E[Validação]
    E --> F[Resposta]
```

### Componentes

| Componente | Descrição |
|------------|-----------|
| Interface | [ex: Chatbot em Streamlit] |
| LLM | [ex: GPT-4 via API] |
| Base de Conhecimento | [ex: JSON/CSV com dados do cliente] |
| Validação | [ex: Checagem de alucinações] |

---

## Segurança e Anti-Alucinação

### Estratégias Adotadas

- [ ] [ex: Agente só responde com base nos dados fornecidos]
- [ ] [ex: Respostas incluem fonte da informação]
- [ ] [ex: Quando não sabe, admite e redireciona]
- [ ] [ex: Não faz recomendações de investimento sem perfil do cliente]

### Limitações Declaradas
> O que o agente NÃO faz?

[Liste aqui as limitações explícitas do agente]
