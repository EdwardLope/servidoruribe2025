from sqlalchemy import Column,Integer,String,Date
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#LLamar a la base de datos
Base = declarative_base()
#Definir las tablas del API 
class Proveedor():
    __tablename__='proveedores'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombres=Column(String(50))
    documento=Column(String(50))
    Direccion=Column(String(50))
    Ciudad=Column(String(50))
    Representante=Column(String(50))
    telefonoContacto=Column(String(50))
    Correo=Column(String(50))
    fechaDeEnvio=Column(Date)
    costoDeEnvio=Column(Integer)
    Descripcion=Column(String(50))

    