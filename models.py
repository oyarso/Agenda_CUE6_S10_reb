from django.db import models 
class BoardsModel(models.Model): 

    titulo = models.CharField(max_length = 150) 
    descripcion = models.TextField()     
    valor = models.FloatField() 
    creado = models.DateTimeField(auto_now_add=True) 
    modificado = models.DateTimeField(auto_now = True)  

    class Meta: 
        verbose_name = "tablero" 
        verbose_name_plural = "tableros" 
        ordering = ["-creado"]         
        permissions = ( 
            ("es_miembro_1", "Es miembro con prioridad 1"), 
        )             

def __str__(self): 
    return self.descripcion 