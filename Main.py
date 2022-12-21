"""
print("Creo que así se hacen los comentarios... no la verdad falle. favor buscar y reemplazar.") ... 🥲


¿Qué contiene Reframework de UiPath?
    - Estados (Init - Get items - Process Items - End Process)


¿Qué hace cada estado?
    - Init: Inicializar el entorno con sus parametros de configuración, Aplicaciones, Productor de items
    - Get Items: Valida si existen registros con X o Y caracteristica desde una fuente en especifico y la transforma en un elemento activo para ser procesado
    - Process Item: Mediante rutinas/procedimientos (Logica de negocio) manipula cada elemento ingresado para poder ser gestionado y posteriormente actualizarlo según halla sido su comportamiento
    -End Process; Libera y limpia el espacio de trabajo de sesiones/credenciales/aplicaciones activas para culminar con la ejecución de cada proceso.


¿Cómo está compuesto cada estado?
    - Init
        . Lee archivos de configuración y los almacena en una dictionary (tabla de hash) para hacer sencilla su manipulación
        . Obtiene las credenciales/Tokens necesarios para el procesamiento de los registros
        . Cierra todos los programas definidos en el listado de programas obligatorios a cerrar (depende si es un proceso en back o front)
        . Realiza la apertura de los programas necesarios para el procesamiento (Only Front)
        . Se encarga de producir las consultas para obtener los registros y ser cargados a la cola (Productor)
            NOTA - El productor se puede ejecutar desde el init (para los PQCQ) o en el estado Get Items (Para cuando solo es PQ)
    
    - Get Items
        . Obiene el listado de registros a procesar los cuales pueden estar alojados en una cola de trabajo la cual proviene de una base de datos (Orchestrator, Hojas de calculo, BD, etc...)

    - Process Items
        . Logica de negocio
        . Actualizar el estado de cada registro procesado según su resultado (success - business rule exception - system exception - application exception )
    
    - End process
        . Liberar credenciales
        . limpiar entorno
        . Notificar a las partes interesadas
            - Reportes a funcionales
            - Correo de culinación
            - Notificación de efectividad (número de registros procesados y con sus resultados (metricas))






            productionMode: Confirma si la ejecución se hara en el ambiente productivo (Live) o en el de Pruebas (hyper-care)")
            2
"""
#--------------------     Imports
import States.init_State as init


global dictConfig
global setupDataset
global SE_Exception
global AE_Exception
global BRE_Exception
global BRU_Exception
#--------------------     Arguments 

productionMode = "Hola mundo"
executeProducer = True
executeConsumer = 150
Country = "CO"
backgroundProcess = False
PathDataDefoult = "/Users/navudzemog/Projects/Python/RPA_Framework"
configNameFile = "Data/Config.xlsx"


#------------------     Variables

dictConfig = dict()
setupDataset = dict()
SE_Exception = None
AE_Exception = None
BRE_Exception = None
BRU_Exception = None

#---------------------   Methods



def getItems_State(a, b, c):
    """acá iria toda la info"""

def processItem_State(a, b, c):
    """Acá toda la logica"""

def endProcess_State(a, b, c):
    """Aca la info necesaria"""


#----------------------------------------


    
configPathFile = PathDataDefoult+ "/" + configNameFile

dictConfig, setupDataset = init.init_State(configPathFile)      #init config and dataSet

print(dictConfig)
