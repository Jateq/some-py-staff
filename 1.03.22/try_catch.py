
import os
print(os.getcwd())
try:
    os.chdir('Test')
except FileNotFoundError as fe:
    print('File not found')
except Exception as e: # отлавливет все ошибки
    print(e)
print('Succes')