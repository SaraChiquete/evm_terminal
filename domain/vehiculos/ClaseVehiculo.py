class Vehiculo:
    def __init__(self, id,num_serie, matricula, marca, modelo,
                 fecha_adquision,disponibilidad, tipo_licencia, proposito):
        self.__id = id
        self.__num_serie = num_serie
        self.__fecha_adquision = fecha_adquision
        self.__matricula = matricula
        self.__marca = marca
        self.__modelo = modelo
        self.__tipo_licencia = tipo_licencia
        self.__capacidad_pasajeros = capacidad_pasajeros
        self.__utilidad = utilidad
        self.__comentarios = comentarios

    def __str__(self):
        return f"ID Vehiculo: {self.__id}  Num serie: {self.__num_serie}  Matricula: {self.__matricula}  Marca: {self.__marca}  Modelo: {self.__modelo}  Fecha Adquision: {self.__fecha_adquision} Diponibilidad: {self.__disponibilidad}  Tipo Licencia: {self.__tipo_licencia}"
        

    #gets
    def get_id(self, ):
        return self.__id
    def get_num_serie(self): 
        return self.__num_serie
    def get_marca(self): 
        return self.__marca
    def get_modelo(self): 
        return self.__modelo
    def get_fecha_adquision(self): 
        return self.__fecha_adquision
    def get_matricula(self):
        return self.__matricula
    def get_tipo_licencia(self):
        return self.__tipo_licencia
    def get_proposito(self):
        return self.__proposito
    def get_disponibilidad(self):
        return self.__disponibilidad
    
    #sets
    def set_id(self, id):
        self.__id = id
    def set_num_serie(self, num_serie):
        self.__num_serie = num_serie
    def set_marca(self, marca): 
        self.__marca = marca
    def set_modelo(self, modelo): 
        self.__modelo = modelo
    def set_fecha_adquision(self, fecha_adquision): 
        self.__fecha_adquision = fecha_adquision
    def set_matricula(self, matricula):
        self.__matricula = matricula
    def set_tipo_licencia(self, tipo_licencia):
        self.__tipo_licencia = tipo_licencia
    def set_proposito(self, proposito):
        self.__proposito = proposito
    def set_disponibilidad(self, disponibilidad):
        self.__disponibilidad=disponibilidad




