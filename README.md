# Jogo da Forca
Versão em Python de um clássico...

## Opções de jogo
Modo para um jogador: o jogo lê um arquivo .txt com palavras e dicas;

Modo para dois jogadores: um usuário digita três palavras/dicas, o jogo sorteia uma delas cabendo ao outro adivinhar.

## Pré-requisitos
Python 3;

Para o modo de um jogador, o arquivo "palavras.txt" deve constar na mesma pasta do script.

Não testei em Linux, mas no Windows funciona bem.

## Adicionar palavras
Neste caso deve-se inserir uma palavra e uma dica por linha no palavras.txt, as quais devem estar separadas unicamente por "#".

### Características
Seis chances para errar;

As palavras podem ter letras (acentuadas ou não), números, pontuação e espaços em branco. Não se preocupe com case-sensitive pois tudo é convertido para maiúsculas;

Em cada chute deve ser tentado somente um caractere. Após cada chute será ofertada a chance de adivinhar a palavra.
