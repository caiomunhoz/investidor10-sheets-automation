# Investidor10 Sheets Automation
  
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![uv](https://img.shields.io/badge/uv-%23DE5FE9.svg?style=for-the-badge&logo=uv&logoColor=white)
![Selenium](https://img.shields.io/badge/selenium-%2343B02A.svg?style=for-the-badge&logo=selenium&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## 🔍 Sobre o Projeto

Este projeto automatiza o processo de lançamento de compras de ativos financeiros de uma planilha do Google Sheets para a carteira do site [Investidor10](https://investidor10.com.br/).

A automação lê as transações da planilha, filtra as que foram realizadas no mês corrente e as adiciona na sua carteira do Investidor10, economizando tempo e evitando erros de digitação manual.

## 📋 Pré-requisitos

- **Python 3.14**.
- **uv:** Este projeto utiliza `uv` para gerenciamento de dependências.
- **Service Account do Google Cloud:** É necessário ter uma Service Account com a API do Google Sheets ativada e as credenciais (arquivo JSON) baixadas.
- **Planilha do Google Sheets:** Planilha estruturada conforme especificações abaixo.
- **Navegador Firefox**: Necessário para execução local da automação.

### Estrutura da Planilha

A automação espera que a planilha possua uma aba `LANÇAMENTOS` seguindo **exatamente** a estrutura abaixo. Cada linha representa uma operação de compra ou venda de um ativo.

| **Coluna** | **Descrição** |
|:-----------|:--------------|
| **Data** | Data da transação (`DD/MM/YYYY`). |
| **Ativo** | Ticker do ativo (ex: PETR4, BTC, MXRF11). |
| **Tipo de Ativo** | Categoria do ativo (Ações, FIIs, ETFs, Criptomoedas). |
| **Quantidade** | Quantidade negociada do ativo. |
| **Custo** | Custo total da operação (ex: taxas de corretagem). |
| **Preço Unitário** | Preço por unidade do ativo no momento da transação. |
| **Total** | Valor total da operação (`Quantidade * Preço Unitário`). |
| **Tipo** | Tipo da operação: `BUY` para compra ou `SELL` para venda. |
| **Id** | Identificador interno do ativo utilizado pela API do Investidor10. |
| **Ticker Type** | Tipo de ativo conforme padrão esperado pela API do Investidor10 (`Ticker`, `Fii`, `Crypto`, `Etf`). |
| **Fonte** | Origem da informação (ex: MANUAL, BONUS, etc.). |

⚠️ **Importante:** Os campos **Id** e **Ticker Type** são valores internos da API do Investidor10 e não são documentados oficialmente. Para obter esses valores para cada ativo é necessário interceptar manualmente as requisições feitas pelo site no momento do lançamento de uma operação.

## 💻 Executando localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/investidor10-sheets-automation.git
   cd investidor10-sheets-automation
   ```

2. **Crie um ambiente virtual e instale as dependências:**
   ```bash
   uv sync
   ```

3. **Configure as variáveis de ambiente:**
   - Crie um arquivo chamado `.env` na raiz do projeto.
   - Adicione as variáveis conforme o modelo abaixo.

    <br>
    
    ```env
    # ID da sua planilha do Google Sheets
    SPREADSHEET_ID=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
    
    # Email e senha da sua conta do Investidor10
    INVESTIDOR10_EMAIL=seu-email@exemplo.com
    INVESTIDOR10_PASSWORD=sua-senha
    
    # Chave JSON da sua Service Account em plain text
    GOOGLE_CLOUD_CREDENTIALS_JSON={...}
    ```

    Substitua os valores de exemplo pelas suas informações reais.

4. **Execute o projeto:**
```bash
uv run src/main.py
```

O script irá iniciar um navegador Firefox em modo headless, fazer login no Investidor10, ler a planilha e adicionar as transações encontradas.

## 🔄 Executando com GitHub Actions

O projeto inclui um workflow do GitHub Actions localizado em `.github/workflows/run-automation.yaml`. 

Este workflow é configurado para executar a automação automaticamente no dia 15 de cada mês, à meia-noite (UTC), garantindo que suas transações sejam sempre atualizadas de forma recorrente sem intervenção manual.

Além da execução agendada, o workflow também pode ser disparado manualmente por meio do evento `workflow_dispatch`, permitindo executar a automação sob demanda diretamente pela interface do GitHub.

### **Como configurar**

1. Fork este repositório.
  
2. Configure os secrets do seu repositório seguindo o mesmo padrão definido no arquivo `.env`