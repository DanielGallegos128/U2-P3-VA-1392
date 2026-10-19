# Importamos las librerias
import cv2
import matplotlib.pyplot as plt
import os
ruta_imagen = os.path.join(
    "img-original-1392",
    "img-mercedez.jpg"
)
# Imagen
# Vamos a crear nuestra matriz principal
mercedes = cv2.imread(ruta_imagen)
# print(mercedes) muestra la matriz principal
# Convertir de BGR a RGB color azul COLOR_BGR2RGB
mrcds = cv2.cvtColor(mercedes, cv2.COLOR_BGR2RGB)
cv2.imshow("mercedes original 1392",mrcds) 
cv2.waitKey(0) # Tiempo de espera
cv2.destroyAllWindows() # Destruye todas las ventanad en memoria