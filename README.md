# TechRac-E-Arduino-Python
Grupo: RICARDO FERNANDES DE AQUINO (RM554597);   KAUÃ SOARES GUIMARÃES (RM559044);   DAYANA TICONA QUISPE (RM558023);

Projeto TechRac-E

Este projeto simula o controle de velocidade de um carro usando um potenciômetro, substituindo um sensor EEG que será adicionado posteriormente no projeto. O código consiste em duas partes: um script Arduino para ler valores do potenciômetro e um script Python para visualizar esses valores e simular a velocidade do carro (a visualização funcionará melhor com as ondas captadas no EEG).

Requisitos:

- Arduino Uno
- Potenciômetro
- Cabos de conexão
- Python 3.11.7
- Biblioteca matplotlib para Python
- Biblioteca pyserial para Python

Dependências:
- matplotlib
- pyserial

Código Arduino>:
int potPin = A0;  // pin connected to the potentiometer

void setup() {
  Serial.begin(9600);
}

void loop() {
  int potValue = analogRead(potPin);  
  Serial.println(potValue);           
  delay(100);                         
}

Como Executar:
Conecte o Arduino ao computador e faça o upload do código Arduino.
Certifique-se de que as dependências do Python estejam instaladas.
Execute o script Python no seu computador utilizando o bash ou o play do VSCode
Observe a simulação da velocidade do carro em tempo real no gráfico gerado.
