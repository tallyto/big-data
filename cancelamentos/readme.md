# Sistema de Gerenciamento de Cancelamentos

O Sistema de Gerenciamento de Cancelamentos é uma aplicação em Python que oferece uma abordagem abrangente para analisar e compreender dados relacionados ao cancelamento de serviços. Ao extrair, processar e interpretar informações de clientes, o sistema fornece insights valiosos, permitindo uma compreensão mais profunda dos padrões de cancelamento.

## Funcionalidades

- **Análise de Dados:** O sistema realiza uma análise detalhada dos dados dos clientes, incluindo características como idade, sexo, tempo como cliente, frequência de uso, ligações ao call center, e outros fatores relevantes.

- **Identificação de Padrões:** Utilizando técnicas avançadas de análise de dados, o sistema identifica padrões e tendências que podem influenciar os cancelamentos de serviços. Essa funcionalidade é essencial para antecipar e reagir a comportamentos de clientes que indicam uma possível intenção de cancelamento.

- **Visualizações Interativas:** Gerando gráficos interativos e estatísticas visuais, o sistema facilita a interpretação dos dados. Essas visualizações dinâmicas são úteis para apresentar de forma clara e acessível as informações obtidas durante a análise.

## Pré-requisitos

- Python 3.12.2
- Bibliotecas Python (verifique o arquivo `requirements.txt` para obter a lista completa)

## Instalação

1. **Clone o Repositório:**

   ```bash
   git clone https://github.com/big-data/cancelamentos.git
   cd cancelamentos
   ```

2. **Instale as Dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configuração do Ambiente:**

   Antes de iniciar, assegure-se de ter o [Visual Studio Code](https://code.visualstudio.com/) instalado com a extensão Jupyter habilitada.

## Uso

1. **Abra o Projeto no Visual Studio Code:**

2. **Execute o Jupyter Notebook:**

    ```bash
    jupyter notebook
    ```

3. **Abra o Notebook `main.ipynb` no Ambiente do Jupyter Notebook:**

    Explore as funcionalidades do sistema, execute células e analise os resultados diretamente no notebook.

## Estrutura do Projeto

```
cancelamentos/
│
├── notebooks/
│   ├── main.ipynb
│   └── ...
│
├── data/
│   ├── cancelamentos.csv
│   └── ...
│
├── tests/
│   ├── test_analise.py
│   └── ...
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Contribuição

1. **Faça o Fork do Projeto:** [https://github.com/big-data/cancelamentos/fork](https://github.com/big-data/cancelamentos/fork)
2. **Crie uma Branch para sua Modificação:** `git checkout -b feature/sua-feature`
3. **Faça o Commit das Mudanças:** `git commit -am 'Adicionando nova funcionalidade'`
4. **Faça o Push para a Branch:** `git push origin feature/sua-feature`
5. **Crie um Novo Pull Request**

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes.

## Contato

- Autor: Tállyto Rodrigues  
- E-mail: rodrigues.tallyto@hotmail.com

