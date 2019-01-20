# Calculadora (Cliente-Servidor)

Utilize o código da Tarefa 1 como ponto de partida para esta atividade.

Crie uma aplicação cliente que consiste em um terminal de entrada de valores para uma calculadora presente no servidor. A aplicação cliente não deverá realizar nenhum cálculo, apenas receber os operandos da entrada padrão (teclado), transmiti-los ao servidor, receber os resultados e apresentá-los na tela ao usuário.

Você deve definir o protocolo da Camada de Aplicação.

# Em que consiste este protocolo?

- Qual é a sequência de mensagens trocadas para realizar um cálculo?
- De que forma o cliente informa ao servidor qual é a operação aritmética desejada?

Por exemplo, um protocolo pode definir que, antes dos operandos, uma mensagem deve ser enviada pelo cliente com o tipo de operação aritmética (ex.: uma mensagem "+", uma mensagem "2", uma mensagem "3"). Outro protocolo pode definir que os operandos são enviados primeiro e depois a operação é informada (ex.: uma mensagem "2", uma mensagem "3", uma mensagem "5"). Um terceiro protocolo pode definir que uma única mensagem contendo operandos e tipo operação é enviada (ex.: uma mensagem 2+5).

- Quantos operandos em sequência o servidor aceita?

Você pode definir que uma mensagem específica informando ao servidor o número de operandos é necessária. Você pode definir que cliente e servidor sabem que sempre serão dois operandos (neste caso nenhuma informação será necessária).

- Quantas operações em sequência o servidor aceita?

Você pode definir que uma mensagem específica informando ao servidor o número de operações a ser realizada é necessária. Você pode definir que cliente e servidor sabem que sempre será apenas uma operação (neste caso nenhuma informação será necessária).

Você define o protocolo! Você define as mensagens! Você define a aplicação! Este exercício é bastante livre e não existe uma implementação certa ou errada. 

A única coisa totalmente obrigatória é: A aplicação cliente não deverá realizar nenhum cálculo! Quem faz os cálculos é o servidor!

# Outras obrigatoriedades:

- Utilize protocolo TCP
- Utilize Python


