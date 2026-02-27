import MOKO
import MOSC
import MGPH
from MFRT import *
import random
from datetime import datetime
import time

MOKO.Stage("Запуск скрипта")

#Region Ход измерений
#description


Uin_PS = MOKO.Report("Uin_PS", "get", "string", "", "float")
Iin_PS = MOKO.Report("Iin_PS", "get", "string", "", "float")

MOKO.Report("Results", "clear")
MOKO.Report("Results", "info", "table", "Номер \\nзамера#60;"
                                                             "Системное \\nвремя#120;"
                                                             "Время на \\nизмерения#80;"
                                                             "Входное \\nнапряжение, В#90;"
                                                             "Входной \\nток, А#60")

#hesh Измерение
#hesh Запись

MOKO.Driver('MaynuoM9714', 'set', 'Input = ON')

MOKO.Driver('Keysight66332A', 'set', 'OUTPUT = ON')


for i in range(15000):
    #######################################################################################################
    ###################################№№№######## ИЗМЕРЕНИЕ ########№№№###################################
    #######################################################################################################

    MOKO.Program('tree', 'set', f'select = Измерение')
    MOKO.Program('tree', 'set', f'info = Номер итерации: {i+1}')
    StartTime = time.time()

    Uin = MOKO.Driver('DMM6500_04582450', 'get', 'READ')
    Uin = ConvertFloatToString(value=Uin, reference_number='0,000', round_number=3)

    Iin = MOKO.Driver('DMM6500_04625545', 'get', 'READ')
    Iin = ConvertFloatToString(value=Iin, reference_number='0,000', round_number=3)


    TimeOfCompletion = time.time() - StartTime     # Время выполнения измерения
    TimeOfCompletion= str(TimeOfCompletion).replace(".", ",")
    MOKO.Program('tree', 'set', 'chosen=passed')
    #######################################################################################################
    ########################################### ЗАПИСЬ В РЕПОРТ ###########################################
    #######################################################################################################
    MOKO.Program('tree', 'set', f'select = Запись')
    MOKO.Report("Results", "set", "table", str(i + 1) + ";" +
                                                            str(datetime.now().time()) + ";" +
                                                            str(TimeOfCompletion)[:4] + ";" +
                                                            str(Uin) + ";" +
                                                            str(Iin) + ";")

    MOKO.Program('tree', 'set', 'chosen=passed')

    #######################################################################################################
    ########################################### ОБНУЛЕНИЕ ХЭШЕЙ ###########################################
    #######################################################################################################

    MOKO.Program('tree', 'set', f'select = Ход измерений')
    MOKO.Program('tree', 'set', 'chosen=empty')



#EndRegion Ход измерений


MOKO.EndScript('passed')