# OpenCV face recognition

Para rodar a aplicação basta executar o arquivo proccess_video.py:

python3 proccess_video.py


# Implementação

Utilizei a propria biblioteca do opencv já importada no projeto além dos demais códigos já implementado no exemplo, adicionei as linhas:

Importei do opencv o cascade classifier para carregar o modelo de classificar os rostos, e em seguida chamei a função paradetecção passando o frame, e os valores para seleção.

Por fim, com o array de de rostos identificados, desenhei um contorno rentagular no que foi selecionado.

Obs: Por algum motivo o autocomplete e algumas funções do opencv no mac não estava funcionando, mas tentei implementar conforme seria o correto.
