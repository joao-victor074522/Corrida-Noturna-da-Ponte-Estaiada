# Corrida Noturna da Ponte Estaiada
Sistema de inscrições e resultados desenvolvido em Python
para a disciplina de Programação I (UNIFSA).
## Como executar
python corrida.py
## Funcionalidades
• Etapa 1:  Inscrição e resultado de um corredor
  
- Inscrição de corredores com idade mínima de 16 anos;
- Escolha da distância (5 ou 10 km) e do lote (1 ou 2);
- Cálculo do valor da inscrição e descontos;
- Geração do código do corredor utilizando nome e idade;
- Classificação dos corredores por categoria;
- Conversão do tempo em segundos;
- Cálculo do pace e verificação de premiação;
- Validação das entradas do usuário;
- Resumo da quantidade de inscrições e total arrecadado.
  
• Etapa 2: A corrida inteira

- Armazenamento dos corredores em uma lista de dicionários.
- Cadastro e listagem de inscritos.
- Busca de corredores pelo código.
- Registro do tempo de prova de corredores cadastrados.
- Tratamento de buscas por códigos inexistentes.
- Armazenamento das categorias e dos tempos-limite em tuplas.
- Utilização de set para controlar códigos já cadastrados.
- Tratamento de códigos repetidos.
- Contagem dos inscritos por categoria utilizando dicionário.
- Utilização de comprehensions para filtrar corredores com tempo registrado e corredores premiados.
- Classificação geral dos corredores por distância e tempo.
- Pódio com os três melhores corredores de cada categoria e distância.
- Relatório final com total de inscritos e arrecadação.
- Cálculo do tempo médio de cada distância.
- Identificação do corredor mais rápido de cada distância.

## Exemplo de uso:
- Exemplo de cadastro:
<img width="394" height="404" alt="image" src="https://github.com/user-attachments/assets/a3031d07-154b-4508-98b2-4c2a3d769dc6" />

- Exemplo de registro de tempo:
  <img width="423" height="349" alt="image" src="https://github.com/user-attachments/assets/6e7a5229-554f-4763-90b5-4e62b15bbf8c" />

## Decisões da dupla
-Utilizamos slicing para separar horas, minutos e segundos.
-Cada corredor é armazenado em um dicionário, e todos os corredores ficam em uma lista durante a execução.
-Para evitar códigos repetidos, utilizamos um set. Quando ocorre uma repetição, acrescentamos um número ao código, como MARSOU34-2 e MARSOU34-3.
-Utilizamos comprehensions para filtrar corredores com tempo registrado e corredores premiados.
-A classificação e o pódio consideram somente corredores com tempos registrados, organizados do menor para o maior tempo.
-Mantivemos uma interface simples pelo terminal.

## Autores
- João Victor Santos Carneiro (github.com/joao-victor074522)
- João Pedro Silva Maciel (github.com/jotapsm027-create)
