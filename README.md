# 🏠 RentSmart — Sistema de Orçamento de Locação

## 📌 Sobre o projeto

O **RentSmart** é uma aplicação desenvolvida em Python para automatizar o cálculo de orçamentos de locação da imobiliária fictícia R.M Imóveis.

O sistema permite selecionar diferentes tipos de imóveis, aplicar adicionais e descontos, calcular a taxa contratual e gerar uma projeção financeira dos primeiros 12 meses de locação.

O projeto foi desenvolvido como parte da disciplina **Algorithmic Thinking & Introduction to Object-Oriented Programming**, com foco na aplicação do pensamento algorítmico e dos fundamentos da Programação Orientada a Objetos (POO).

## 🎯 Objetivos

- Automatizar os cálculos de aluguel.
- Aplicar as regras comerciais da imobiliária.
- Calcular adicionais e descontos.
- Permitir o parcelamento da taxa contratual.
- Apresentar um orçamento detalhado ao usuário.
- Gerar um arquivo CSV com a projeção financeira de 12 meses.
- Aplicar classes, objetos, atributos, métodos, herança e abstração.

## 💻 Tecnologias utilizadas

- **Python 3:** linguagem principal do projeto.
- **Programação Orientada a Objetos:** organização das regras de negócio.
- **CSV:** exportação da projeção financeira.
- **unittest:** testes automatizados.
- **Visual Studio Code:** ambiente utilizado no desenvolvimento.

O sistema utiliza exclusivamente bibliotecas nativas do Python, não sendo necessário instalar dependências externas.

## 🏘️ Regras de negócio

### Apartamento

- Aluguel-base: R$ 700,00.
- Adicional para dois quartos: R$ 200,00.
- Garagem: R$ 300,00 mensais.
- Desconto de 5% para clientes que não possuem crianças, aplicado após os adicionais.

### Casa

- Aluguel-base: R$ 900,00.
- Adicional para dois quartos: R$ 250,00.
- Garagem: R$ 300,00 mensais.

### Estúdio

- Aluguel-base: R$ 1.200,00.
- Pacote inicial de duas vagas de estacionamento: R$ 250,00.
- Cada vaga adicional: R$ 60,00.

Na implementação, o estacionamento do estúdio pode ser dispensado ou contratado a partir do pacote de duas vagas.

### Taxa contratual

Todos os imóveis possuem uma taxa contratual de R$ 2.000,00, que pode ser parcelada de uma a cinco vezes.

O sistema utiliza cálculos decimais para garantir a precisão dos valores monetários e ajustar eventuais diferenças de arredondamento na última parcela.

## 📂 Estrutura do projeto

**RentSmart/**

- `main.py` — Interface de terminal, menu e interação com o usuário.
- `imoveis.py` — Classes e regras de cálculo dos imóveis.
- `contrato.py` — Classe responsável pela taxa contratual e pelo parcelamento.
- `projecao.py` — Geração da projeção financeira em CSV.
- `test_rentsmart.py` — Testes automatizados.
- `projecao_12_meses.csv` — Arquivo de projeção gerado pelo programa.
- `README.md` — Documentação do projeto.

## ⚙️ Como executar

**1. Requisitos**

Ter o Python 3 instalado no computador.

**2. Abrir o projeto**

Abra a pasta `RentSmart` no Visual Studio Code ou em outro editor de sua preferência.

**3. Iniciar a aplicação**

Abra o terminal na pasta do projeto e execute:

`python main.py`

**4. Utilizar o sistema**

O programa apresentará um menu com as seguintes opções:

- 1 — Apartamento
- 2 — Casa
- 3 — Estúdio
- 0 — Sair

Após selecionar o imóvel, informe as características solicitadas e escolha o parcelamento da taxa contratual.

O sistema calculará os valores e exibirá um orçamento detalhado.

## 📊 Geração do arquivo CSV

Após a realização de um orçamento, o programa gera automaticamente o arquivo `projecao_12_meses.csv`.

O arquivo apresenta:

- Mês da locação.
- Valor do aluguel mensal.
- Parcela da taxa contratual.
- Total previsto para pagamento no mês.

A projeção contempla os 12 primeiros meses do contrato.

O arquivo é salvo na pasta do projeto, utiliza ponto e vírgula como separador e pode ser aberto em programas como Microsoft Excel.

**Observação:** um novo orçamento substitui a projeção CSV anterior.

## 🧪 Testes automatizados

O projeto possui testes automatizados utilizando a biblioteca `unittest`.

Para executá-los, utilize o comando:

`python -m unittest test_rentsmart.py -v`

Os testes verificam:

- Cálculo de apartamentos com e sem adicionais.
- Aplicação do desconto.
- Cálculo de casas.
- Estacionamento de estúdios.
- Parcelamento da taxa contratual.
- Tratamento de entradas inválidas.

Os nove testes automatizados foram executados com sucesso durante o desenvolvimento.

## 🧩 Programação Orientada a Objetos

O RentSmart foi estruturado utilizando os conceitos de Orientação a Objetos.

A classe abstrata `Imovel` estabelece uma estrutura comum para os diferentes tipos de imóveis.

As classes `Apartamento`, `Casa` e `Estudio` herdam dessa estrutura e implementam suas regras específicas.

A classe `Contrato` gerencia o parcelamento da taxa contratual, enquanto `ProjecaoLocacao` é responsável pela geração do arquivo CSV.

Essa organização facilita a manutenção, a reutilização de código, a separação de responsabilidades e a implementação de novas funcionalidades.

## ✅ Funcionalidades implementadas

- [x] Menu interativo.
- [x] Seleção do tipo de imóvel.
- [x] Validação das principais entradas.
- [x] Cálculo dos adicionais de quartos.
- [x] Cálculo de garagem e estacionamento.
- [x] Aplicação de descontos.
- [x] Parcelamento da taxa contratual.
- [x] Orçamento detalhado.
- [x] Projeção financeira de 12 meses.
- [x] Exportação para CSV.
- [x] Testes automatizados.

## 🎓 Informações acadêmicas

**Projeto:** RentSmart — Sistema de Orçamento de Locação com Python e Orientação a Objetos

**Disciplina:** Algorithmic Thinking & Introduction to Object-Oriented Programming

**Instituição:** UniFECAF

**Finalidade:** Trabalho acadêmico para demonstrar o desenvolvimento de algoritmos e a aplicação de Programação Orientada a Objetos em Python.