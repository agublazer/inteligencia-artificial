Trabajo Final: Clasificación de videos en violentos y no violentos.
Basado en: https://blog.coast.ai/five-video-classification-methods-implemented-in-keras-and-tensorflow-99cad29cc0b5
Integrantes:
- Giancarlo Andre Anco Valdivia
- Ruben Adrian Cuba Lajo
- Dany Mauro Diaz Espino
Funcionamiento:
Genera frames a partir de cada video que se encuentre en data/tests y data/train, luego genera features para cada imagen
usando inception v3, une los features en secuencias según la imagen a la que pertenecen, y luego clasifica usando una
red lstm. Los resultados fueron 0.98 de accuracy.
El trabajo original usa el dataset de UCF101, encontrado en http://crcv.ucf.edu/data/UCF101/UCF101.rar Nosotros lo adaptamos para que funcione con el dataset encontrado en http://academictorrents.com/details/70e0794e2292fc051a13f05ea6f5b6c16f3d3635
