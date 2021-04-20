from sistema.wsgi import *
from core.erp.models import Type

# Create your tests here.
query = Type.objects.all()
print(query)

#Prueba de commit para github
