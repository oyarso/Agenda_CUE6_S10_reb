from django.db import models 
class BoardsModel(models.Model): 

    titulo = models.CharField(max_length = 150) 
    descripcion = models.TextField()     
    valor = models.FloatField() 
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now = True)  

    class Meta: 
        verbose_name = "libro" 
        verbose_name_plural = "libros" 
        ordering = ["-creado"]         
        permissions = ( 
            ("es_miembro_1", "Es miembro con prioridad 1"), 
        )             

def __str__(self): 
    return self.descripcion 