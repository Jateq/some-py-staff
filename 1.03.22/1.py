import os
print(os.getcwd()) # возвращает текущую директорию
# cd means change directory
# cd - chdir()
os.chdir("..") #перемещаетфайл к другой папке 
print(os.getcwd())
# os.chdir('01.03.22')
# print(os.getcwd())
# os.mkdir('Test dir') создание
# os.rmdir('Test dir')
# open("test file").close()
# os.rename('Test dir', 'Test file') меняет файл
# print(os.listdir()) # list of files in out directory
for file in os.listdir():
    print(f'<DIR> {file}')
print(os.path.isdir('1.03.22')) # for directory
print(os.path.isfile('18.02')) # for files