# POO - Lista de exercicios \# 1

## Instruções
* Separe cada exercício em uma pasta separada.
* Cada classe deverá estar um arquivo com o mesmo nome (exemplo: classe Pessoa no arquivo pessoa.py)
* Para cada exercício, crie um arquivo principal (main.py) que irá importar as classes que são utilizadas
* O arquivo main.py será o único que irá receber dados de entrada do usuário (input) e imprimir dados de saída (print), chamando as classes para executar as operações quando lhe for conveniente.

## Importante:
* As respostas devem ser submetidas unicamente por intermédio deste [formulario](https://goo.gl/forms/9snCZKLJkDj9oM2g1), em que devem ser preenchidos os dados do aluno (nome, e-mail e matrícula).
* A lista deverá estar compactada (zip), contendo as pastas enumeradas correspondentes às respostas de cada exercício
* Em caso de plágio, as notas serão automaticamente zeradas. Lembrem-se: exercício é mais que uma nota, é uma forma de praticar e um caminho para aprender.
* Prazo de entrega: **11/07/2018**

## Exercícios:
1. Crie uma classe para representar um jogador de futebol, com os atributos nome, posição, data de nascimento, nacionalidade, altura e peso. Crie os métodos públicos necessários para sets e gets e também um método para imprimir todos os dados do jogador. Crie um método para calcular a idade do jogador e outro método para mostrar quanto tempo falta para o jogador se aposentar. Para isso, considere que os jogadores da posição de defesa se aposentam em média aos 40 anos, os jogadores de meio-campo aos 38 e os atacantes aos 35.

2. Considere as classes ContaCorrente e ContaPoupanca apresentadas em sala de aula. Crie uma classe ContaImposto que herda de conta e possui um atributo percentualImposto. Esta classe também possui um método calcularImposto() que subtrai do saldo, o valor do próprio saldo multiplicado pelo percentual do imposto. Crie um programa para criar as instâncias de ContaImposto e utilizar todos os métodos das 3 classes (ex.: sacar, depositar, calcularImposto).

3. Crie uma classe chamada Ingresso, que possui um valor em reais e um método imprimirValor(). Crie uma classe IngressoVIP, que herda de Ingresso e possui um valor adicional. Crie um método que retorne o valor do ingresso VIP (com o adicional incluído). Crie um programa para criar as instâncias de Ingresso e IngressoVIP, mostrando a diferença de preços.

4. Crie uma classe Elevador para armazenar as informações de um elevador de prédio. A classe deve armazenar o andar atual (térreo = 0), total de andares no prédio (desconsiderando o térreo), capacidade do elevador e quantas pessoas estão presentes nele. A classe deve também disponibilizar os seguintes métodos:
  * **Inicializar:** que deve receber como parâmetros a capacidade do elevador e o total de andares no prédio (os elevadores sempre começam no térreo e vazio);
  * **Entrar:** para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
  * **Sair:** para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
  * **Subir:** para subir um andar (não deve subir se já estiver no último andar);
  * **Descer:** para descer um andar (não deve descer se já estiver no térreo);
  - Obs.: Encapsular todos os atributos da classe (criar os métodos set e get).
