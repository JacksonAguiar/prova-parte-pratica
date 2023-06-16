import cv2


# Abre o arquivo de video
input_video = cv2.VideoCapture('./assets/arsene.mp4')

# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
    
# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))   # float `width`
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video

output_video = cv2.VideoWriter( './output/arsene_faces.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))

# Loop de leitura frame por frame
while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = input_video.read()
    

    classifier = cv2.CascadeClassifier("haarcascade")
    faces = classifier.detect(frame, 1.1,4)
  

    for (x,y,w,h) in faces:
        cv2.rectangle(
            img=frame,
            pt1=(x, y),
            pt2=(w, h),
            color=(0,0,255),
            thickness=4
        )
  # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break
    
    # Vamos editar o frame com um retangulo
 

    # Exibe o frame
    cv2.imshow('Faces detection', frame)
    
    # Escreve o frame no output
    output_video.write(frame)

    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
    
# Fecha tudo
output_video.release()
input_video.release()
cv2.destroyAllWindows()