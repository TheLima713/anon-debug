# 🧠 Anonimizador de Texto

Um **Anonimizador de Texto** interativo que identifica e substitui informações pessoais e sensíveis em textos com base na **Lei Geral de Proteção de Dados (LGPD)**.  
O objetivo é proteger a **privacidade do usuário** ao processar prompts ou textos que possam conter dados identificáveis.
O projeto utiliza Flask e SpaCy para que o usuário possa ter um prompt sem conter dados sensíveis ou pessoais. Tal projeto faz parte da divulgação científica na matéria de projeto dirigido na UFABC, cujo objetivo é conscientizar usuários de chatbots acerca de proteção de dados e privacidade.
---

## 🛡️ Sobre o Projeto

Este projeto foi criado para **demonstrar boas práticas de privacidade e segurança de dados**, especialmente em contextos onde o texto inserido em **prompts de IA** pode conter informações pessoais.  

Ele permite que o usuário insira um texto e visualize o resultado **anonimizado**, com cada tipo de dado destacado em **cores diferentes**, facilitando a compreensão sobre **que tipo de dado foi identificado** e **como a anonimização protege a privacidade**.

---

## 📘 Tipos de Dados Detectados

O sistema identifica automaticamente padrões comuns de dados e substitui-os por marcadores padronizados.  
Cada marcador possui uma **cor e uma classificação legal** conforme a LGPD:

| Marcador | Tipo de Dado | Classificação LGPD | Descrição |
|-----------|--------------|--------------------|------------|
| `[NOME]` | Nome de pessoa | **Dado pessoal direto** | Identifica uma pessoa natural. |
| `[CPF]` | CPF | **Dado pessoal sensível** | Identificador nacional único. |
| `[RG]` | RG | **Dado pessoal sensível** | Documento de identidade. |
| `[CNPJ]` | CNPJ | **Dado de pessoa jurídica** | Identifica empresas. |
| `[TELEFONE]` | Telefone | **Dado pessoal** | Permite contato direto. |
| `[EMAIL]` | E-mail | **Dado pessoal** | Identifica e permite contato digital. |
| `[DATA]` | Datas | **Dado pessoal indireto** | Pode revelar idade ou histórico. |
| `[ENDEREÇO]` | Endereço | **Dado pessoal** | Localização física do titular. |
| `[ORG]` | Organização | **Dado pessoal indireto** | Pode identificar vínculos com o titular. |
| `[LOC]` | Localização | **Dado pessoal indireto** | Indica local associado ao titular. |
| `[IP]` | Endereço IP | **Dado pessoal (não sensível)** | Identificador técnico de rede. |

---

## 🧩 Exemplo de Uso

**Entrada:**
Trabalho na Google e meu CPF é 123.321.123-00. Meu IP é 192.168.0.1.
**Saída Anonimizada:**
Trabalho na [ORG] e meu CPF é [CPF]. Meu IP é [IP].
