# POO - Lista de exercicios \# 2

**1. Crie uma classe chamada Fatura que possa ser utilizado por uma loja de suprimentos de informática para representar uma fatura de um item vendido na loja. Uma fatura deve incluir as seguintes informações como atributos:**
  * o número do item faturado,
  * a descrição do item,
  * a quantidade comprada do item e
  * o preço unitário do item.

  Sua classe deve ter um construtor que inicialize os quatro atributos. Se a quantidade não for positiva, ela deve ser configurada como 0. Se o preço por item não for positivo ele deve ser configurado como 0.0. Forneça os métodos get/set para cada variável de instância. Além disso, forneça um método chamado calcularValorDaFatura que calcula o valor da fatura (isso é, multiplica a quantidade pelo preço por item) e depois retorna o valor. Escreva também um programa de teste (main) que demonstra as capacidades da classe Fatura.

**2. A fim de representar empregados em uma empresa, crie uma classe chamada Empregado que inclui as três informações a seguir como atributos:**
  * um primeiro nome,
  * um sobrenome, e
  * um salário mensal.

  Sua classe deve ter um construtor que inicializa os três atributos. Forneça os métodos método get/set para cada atributo. Se o salário mensal não for positivo, configure-o como 0.0. Escreva um aplicativo de teste que demonstra as capacidades da classe. Crie duas instâncias da classe e exiba o salário anual de cada instância (soma dos salários mensais). Então dê a cada empregado um aumento de 10% e exiba novamente o salário anual de cada empregado.

**3. Crie uma classe para representar datas. Represente uma data usando três atributos: o dia, o mês, e o ano.**
  * Sua classe deve ter um construtor que inicializa os três atributos e verifica a validade dos valores fornecidos.
  * Caso as datas não sejam passadas no construtor (devem ser parâmetros opcionais), inicialize a data com a data atual fornecida pelo sistema operacional.
  * Forneça os métodos get/set para cada atributo.
  * Forneça o método \__str__ para retornar uma representação da data como string. Considere que a data deve ser formatada mostrando o dia, o mês e o ano separados por barra (/).
  * Forneça uma operação para avançar uma data para o dia seguinte.
  * Escreva um programa de teste que demonstra as capacidades da classe.


**4. Crie uma classe abstrata chamada CartaoMensagem. Essa classe representa todos os tipos de cartões de mensagem contendo apenas um atributo: destinatario. Nessa classe você deverá também declarar o método retornarMensagem(remetente).**
  * Crie três classes filhas (sub-classes) da classe CartaoMensagem:
      1. MensagemDiaDosNamorados
      2. MensagemNatal
      3. MensagemAniversario.
  * Cada uma dessas classes deve conter um método construtor que receba o nome do destinatário do cartão. Cada classe também deve implementar o método retornarMensagem(remetente), retornando uma mensagem ao usuário com o nome do destinatário, um texto que seja específico para a data de comemorativa do cartão, acrescido do remetente ao final da mensagem. Por exemplo, essa poderia ser uma mensagem de um cartão de dia dos namorados:
    “Querida Maria,
    Feliz Dia dos Namorados!
    Espero que esse tenha gostado do meu cartão de dia dos namorados! De todo meu coração, João”
  * Crie um programa para demonstrar o uso das classes criadas. Para isso, crie um array (ex.: listaMsg = []) e insira de forma alternada instâncias dos 3 tipos de cartões (ex.: listaMsg.append(cartao)). Em seguida, use um laço de repetição (ex.: for msg in listMsg:) para exibir as mensagens dos cartões. Chame o método mostrarMensagem(String remetente) dos objetos, utilizando como argumento o seu nome para remetente. Utilize o método input para receber dados do usuário.
