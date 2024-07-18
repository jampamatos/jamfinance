# To-Do List Detalhada para o MVP do Jamfinance

## 1. Configuração do Ambiente de Desenvolvimento
- [ ] Configurar o WSL 2 e Docker no Windows para desenvolvimento e teste.
- [ ] Estabelecer um repositório Git para controle de versão e colaboração.
- [ ] Instalar e configurar todas as bibliotecas e frameworks necessários (Python, React, Flask, etc.).
- [ ] Criar scripts de autoinstalação para facilitar a configuração do ambiente em novas máquinas.

## 2. Microsserviço de Coleta de Dados
- [ ] Desenvolver scripts Python para coleta de dados em tempo real e históricos usando APIs financeiras selecionadas.
- [ ] Explorar e implementar soluções de armazenamento apropriadas para os dados coletados.
- [ ] **API de Comunicação**: Criar uma API RESTful para disponibilizar os dados coletados para outros microsserviços.

## 3. Microsserviço de Decisão de Trading
- [ ] Elaborar um algoritmo completo de trading que priorize a segurança e minimização de riscos.
- [ ] **API de Comunicação**: Desenvolver uma API que receba dados do microsserviço de coleta e envie decisões de trading ao microsserviço de execução de trades.

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
