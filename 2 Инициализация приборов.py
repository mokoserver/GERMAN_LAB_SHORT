import MOKO
import MOSC
import MGPH
import MFRT
import time

MOKO.Stage("Запуск скрипта")
Uin_PS = MOKO.Report("Uin_PS", "get", "string", "", "float")
Iin_PS = MOKO.Report("Iin_PS", "get", "string", "", "float")
Uout_EL = MOKO.Report("Uout_EL", "get", "string", "", "float")
Iout_EL = MOKO.Report("Iout_EL", "get", "string", "", "float")


def InitDevice(name: str):
    MOKO.Program('tree', 'set', f'select = Инициализация {name}')
    MOKO.Driver(name, "init")
    time.sleep(3)


    MOKO.Program('tree', 'set', 'chosen=passed')

#Region Инициализация

InitDevice("MaynuoM9714")         #hash Инициализация MaynuoM9714
InitDevice("Keysight66332A")      #hash Инициализация Keysight66332A
InitDevice("DMM6500_04582450")    #hash Инициализация DMM6500_04582450
InitDevice("DMM6500_04625545")    #hash Инициализация DMM6500_04625545


#EndRegion Инициализация





#Region Настройка параметров

#hash Настройка MaynuoM9714
MOKO.Program('tree', 'set', f'select = Настройка MaynuoM9714')
time.sleep(3)
MOKO.Driver('MaynuoM9714', 'set', f'V = {Uout_EL}')
time.sleep(3)
MOKO.Driver('MaynuoM9714', 'set', f'I = {Iout_EL}')
time.sleep(3)
MOKO.Program('tree', 'set', 'chosen=passed')
###################################################################################

#hash Настройка Keysight66332A
MOKO.Program('tree', 'set', f'select = Настройка Keysight66332A')

MOKO.Driver('Keysight66332A', 'set', 'OUTPUT = OFF')
time.sleep(3)
MOKO.Driver('Keysight66332A', 'set', f'VDC = {Uin_PS}')
time.sleep(3)
MOKO.Driver('Keysight66332A', 'set', f'IDC = {Iin_PS}')
time.sleep(3)
MOKO.Program('tree', 'set', 'chosen=passed')
###################################################################################

#hash Настройка DMM6500_04582450

MOKO.Program('tree', 'set', f'select = Настройка DMM6500_04582450')

MOKO.Driver('DMM6500_04582450', 'set', 'Function = VDC')
time.sleep(3)
MOKO.Driver('DMM6500_04582450', 'set', 'Range = Auto')
time.sleep(3)

MOKO.Program('tree', 'set', 'chosen=passed')
###################################################################################

#hash Настройка DMM6500_04625545

MOKO.Program('tree', 'set', f'select = Настройка DMM6500_04625545')

MOKO.Driver('DMM6500_04625545', 'set', 'Function = IDC')
time.sleep(3)
MOKO.Driver('DMM6500_04625545', 'set', 'Range = Auto')
time.sleep(3)

MOKO.Program('tree', 'set', 'chosen=passed')
###################################################################################



#EndRegion Настройка параметров

MOKO.EndScript('passed')