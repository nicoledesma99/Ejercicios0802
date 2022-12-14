# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

# Recordar utilizar la ruta relativa, no la absoluta para ingestar los datos desde los CSV
# EJ: 'datasets/xxxxxxxxxx'


def Ret_Pregunta01():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe informar la cantidad de registros, sin tener en cuenta aquellos con valores faltantes, para el campo
    'Solar_Generation_TWh' y retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:
    x=5170   
    return x


def Ret_Pregunta02():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    Esta función debe eliminar las columnas 'Code' y 'Entity' y luego informar la cantidad de columnas
    retornando ese valor en un dato de tipo entero.
    '''
    #Tu código aca:

    return None

    
def Ret_Pregunta03():
    '''
    Debes utilizar Pandas para ingestar en un objeto Dataframe el contenido del archivo provisto
    "Fuentes_Consumo_Energia.csv".
    El ExaJulio es una unidad diferent al TWh, es decir, no tiene sentido sumarlos o
    buscar proporciones entre ellos. 
    La fórmula de conversión es: 277.778 Teravatios/Hora (TWh) = 1 Exajulio
    Los campos terminados en "_EJ" corresponden a mediciones en Exajulios,
    y los terminados en "_TWh" corresponden a Teravatios/Hora.
    La consigna es crear un nuevo campo, que se denomine "Consumo_Total"
    y que guarde la sumatoria de todos los consumos expresados en Teravatios/Hora
    (convirtiendo a esta medida los que están en Exajulios).
    Esta función debe informar el consumo total para la entidad 'World' y año '2019',
    redondeado a 2 decimales, retornando ese valor en un dato de tipo float.
    '''
    #Tu código aca:
   
    return None


def Ret_Pregunta04():
    '''
    Cuál curso, de la siguiente lista de cursos tuvo mayor cantidad de alumnos en el año 2021: Conversacion Guiada, Canales de Comunicacion, Mapas Mentales 
    (considerar el item con mayor cantidad de alumnos)
    Archivo para usar en el dataframe de pandas: cursos_info.csv
    La función debe retornar el nombre del curso, formato string
    '''
    #Tu código aca:
    
    return None


def Ret_Pregunta05():
    '''
    Cantidad de productos unicos pendientes en el año 2021
    Usar pandas con el archivo: transacciones-1a.csv
    La función debe devolver un valor entero que representa la cantidad
    '''
    #Tu código aca:
    
    return None


def Ret_Pregunta06():
    '''
    Retornar monto total para transacciones pendientes y el monto total para transacciones completadas en formato tupla
    Usar pandas con los archivos: transacciones-monto.csv y transacciones-estado.csv
    '''
    #Tu código aca:
    
    return None

