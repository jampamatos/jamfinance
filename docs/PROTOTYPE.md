# To-Do List Detalhada para o MVP do Jamfinance

## 1. Configuração do Ambiente de Desenvolvimento
- [X] Configurar o WSL 2 e Docker no Windows para desenvolvimento e teste.
- [X] Estabelecer um repositório Git para controle de versão e colaboração.
- [X] Instalar e configurar todas as bibliotecas e frameworks necessários (Python, React, Flask, etc.).
- [X] Criar scripts de autoinstalação para facilitar a configuração do ambiente em novas máquinas.

## 2. Microsserviço de Coleta de Dados
- [X] Criar um container em Docker para esse Microsserviço.
- [X] Desenvolver scripts Python para coleta de dados em tempo real e históricos usando APIs financeiras selecionadas.
- [X] Explorar e implementar soluções de armazenamento apropriadas para os dados coletados.
- [X] **API de Comunicação**: Criar uma API RESTful para disponibilizar os dados coletados para outros microsserviços.

## 3. Microsserviço de Decisão de Trading
- [X] Criar um container em Docker para esse Microsserviço.
- [ ] Elaborar um algoritmo completo de trading que priorize a segurança e minimização de riscos.
    - **Estratégias de Trading para Minimização de Riscos**
        - **1. Médias Móveis Crossover:** Esta é uma das estratégias mais comuns e eficazes em trading algorítmico para identificar tendências. Você pode usar duas médias móveis: uma curta (por exemplo, 10 dias) e uma longa (por exemplo, 50 dias). A ideia é:
            - Comprar quando a média móvel curta cruza acima da média móvel longa, indicando uma tendência de alta.
            - Vender quando a média móvel curta cruza abaixo da média móvel longa, indicando uma tendência de baixa.
        - **2. Relative Strength Index (RSI):** O RSI é um indicador de momentum que mede a velocidade e mudança dos movimentos de preços. Geralmente, um RSI abaixo de 30 sugere que o ativo está sobrevendido (uma potencial oportunidade de compra), enquanto um RSI acima de 70 sugere que o ativo está sobrecomprado (uma potencial oportunidade de venda).
        - **3. Stop-Loss e Take-Profit:** Para cada ordem de compra, defina um preço de stop-loss para minimizar as perdas caso o mercado se mova contra sua previsão. Similarmente, defina um preço de take-profit para garantir lucros quando o mercado se mover a favor da sua previsão. Esses limites devem ser baseados em uma porcentagem do preço de compra ou em um nível de preço que reflita uma reversão anterior do mercado.
        - **4. Volatilidade:** Avalie a volatilidade do mercado para ajustar suas estratégias. Em mercados mais voláteis, amplie os parâmetros de stop-loss e take-profit para acomodar maiores flutuações de preço.
        - **5. Backtesting:** Antes de colocar sua estratégia em uso real, é crucial realizar um backtesting extensivo usando dados históricos. Isso ajudará a identificar como sua estratégia teria se comportado no passado e ajustar os parâmetros conforme necessário.
    - **Implementação Técnica**
        - **Estruturação do Código:** Organize o código de modo que cada estratégia de trading seja modular, permitindo fácil ajuste e expansão. Por exemplo, cada estratégia poderia ser uma função ou classe separada.
        - **Integração com Dados em Tempo Real e Históricos:** Assegure que o microsserviço de decisão de trading possa acessar dados em tempo real e históricos fornecidos pelo microsserviço de coleta de dados. Use esses dados para calcular indicadores e tomar decisões de trading.
        - **API para Decisões de Trading:** Implemente uma API que receba solicitações do microsserviço de execução de trades. A API deveria processar os dados, aplicar a lógica de trading e retornar decisões de compra ou venda.
- [ ] **API de Comunicação**: Desenvolver uma API que receba dados do microsserviço de coleta e envie decisões de trading ao microsserviço de execução de trades.
- [ ] Testar a integração das APIS de Decisão e Coleta.

## 4. Microsserviço de Execução de Trades
- [ ] Implementar funcionalidades para a execução de ordens de compra e venda nas plataformas de corretagem.
- [ ] **API de Comunicação**: Implementar uma API para receber decisões de trading e interagir com as corretoras.

## 5. Interface de Usuário
- [ ] Desenvolver uma dashboard funcional em React para visualização interativa dos dados e monitoramento das decisões de trading.
- [ ] **API de Comunicação**: Estabelecer APIs para comunicar com os microsserviços de coleta e decisão de trading, além de enviar comandos do usuário.

## 6. Integração e Comunicação
- [ ] Utilizar REST API para a comunicação inicial entre microsserviços.
- [ ] Garantir que os dados sejam passados eficientemente entre os serviços.

## 7. Testes e Desenvolvimento Guiado por Testes (TDD)
- [ ] Desenvolver testes unitários para cada componente antes de sua implementação.
- [ ] Implementar testes de integração para validar a comunicação entre microsserviços.

## 8. Documentação
- [ ] Documentar o processo de instalação e configuração do ambiente.
- [ ] Documentar detalhadamente cada funcionalidade desenvolvida, cada API usada, e as interações entre os microsserviços.
- [ ] Criar documentação de usuário inicial para a interface, incluindo guias de uso.

## 9. Revisão e Feedback
- [ ] Testar o MVP internamente e com um grupo selecionado de usuários externos.
- [ ] Coletar e analisar feedback para entender necessidades de melhorias.

## 10. Planejamento para Próximas Iterações
- [ ] Identificar funcionalidades adicionais e ajustes necessários com base no feedback.
- [ ] Priorizar desenvolvimentos futuros para expandir e aprimorar o sistema.
