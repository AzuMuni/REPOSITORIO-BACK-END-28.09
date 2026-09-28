from django.db import models

# Create your models here.

# ---------- Clase Categoría -----------
class categoria(models.Model):
    name = models.CharField(max_length=80, unique = True)

    class Meta:
        verbose_name_plural = 'categorias'
        ordering = ['name'] # Por defecto, los datos que se llamen serán ordenador por categoria


    def __str__(self):
        return self.name


# ---------- Clase Producto ------------

class Producto (models.Model):
    nombre = models.CharField(max_length= 120)


    descripcion = models.TextField(null = True)
    # descripcion = models.TextField()  # La diferencia de text y varchar | Text: hecho para textos largos.
    # Un cambio en la descripción, ya no es obligatoria. Ahora puede ser nula
    # Para indicar que es nula: null = True



    precio = models.PositiveIntegerField(default = 0)
    # Para trabajar con decimales es: .DecimalField, en este caso es entero (Integer) y solo positivo (Positive)
    # Si quisieramos que un producto fuese de valor 0, el default de integer es 0, entonces: default = 0

    stock = models.PositiveIntegerField()
    # Al no añadir, ni null ni alguna otra cosa, el sistema lo toma automaticamente como obligatorio.


    activo = models.BooleanField(default = False, null = True)
    # al no ser obligatorio, se debe poner null

    creado = models.DateTimeField(auto_now_add=True) # Se activa la creacion automatica con True
    # default=now  --> Automatiza la fecha/creacion al insertarse en la BD | Tomará la fecha de apenas se inserte.



    codigo = models.CharField(max_length = 20)


    # Añadiremos la clase Meta

    class Meta:
        verbose_name_plural = 'Productos' # Nombre en plural de nuestra clase
        ordering = ['nombre']


# Para retornar, debe ser especifico para devolver ya sea nombre y/o precio

    def __str__(self):
        return f"{self.name} ${self.precio}" # De esta forma se concatenan para que puedan ir ambos.


# ------------- Clase Cliente --------------


class cliente (models.Model):
    name = models.CharField(max_length=120)

    correo = models.EmailField( unique = True)
# No se pone la maxima de caracteres (como indica la tabla) en correo ya que djngo el maximo por default es 254.


    class Meta:
        verbose_name_plural = 'Clientes'
        ordering = ['name']


    def __str__(self):
        return f"{self.name} {self.correo}"

