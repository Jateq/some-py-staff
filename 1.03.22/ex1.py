
import os
class File_manager():
    def __init__(self):
        pass
    def name_dir(self):
        print(os.getcwd())
    def change_dir(self, dir):
        os.chdir(dir)
        print('Changed')
        self.name_dir()
    def create_dr(self, dir):
        os.mkdir(dir)
        print('created')
    def create_wf(self, name):
        open(name, 'w').close()
        print('created')
    def list_of_dir(self):
        print(os.listdir())
    def test(self):
        print("succes")
    def dir(self):
        for file in os.listdir():
            print(f'<DIR> {file}')
    def filer(self):
        cnt_files = 0
        for file in os.listdir():
            if os.path.isfile(file):
                cnt_files+=1
    def diver(self):
        cnt_dir = 0
        for file in os.listdir():
            if os.path.isdir(file):
                cnt_dir +=1
    def rename(self, old, new):
        os.rename(old, new)
        print("succes")
    def inner(self):
        self.change_dir('..')
    def add(self, name):
        newc = input()
        with open(name, 'a') as wf:
            wf.write(newc)
    


mfm = File_manager()
while True:
    command = input()

    if command == 'test':
        mfm.test()
    if command == 'show':
        mfm.name_dir()
    if command == 'create dir':
        mfm.create_dr('Almaty')
    if command == 'change':
        mfm.change_dir('Almaty')
    if command == 'create file':
        mfm.create_wf('Almaty.py')
    if command == 'list':
        mfm.list_of_dir()
    if command == 'dir':
        mfm.dir()
    if command == 'number of files':
        mfm.filer()
    if command == 'number of dir':
        mfm.diver()
    if command == 'default':
        mfm.inner()
    elif command == 'exit':
        break



