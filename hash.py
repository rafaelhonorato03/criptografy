import hashlib
import hmac

# Texto para ser "hasheado"
texto = "Aprendendo funções hash!"

# Criando um hash SHA-256
hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()

print(f"Texto original: {texto}")
print(f"Hash SHA-256: {hash_sha256}")

# MD5
hash_md5 = hashlib.md5(texto.encode()).hexdigest()

# SHA-1
hash_sha1 = hashlib.sha1(texto.encode()).hexdigest()

# SHA-256
hash_sha256 = hashlib.sha256(texto.encode()).hexdigest()

print(f"MD5: {hash_md5}")
print(f"SHA-1: {hash_sha1}")
print(f"SHA-256: {hash_sha256}")

def hash_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Armazenando uma senha
senha = "minha_senha_segura"
senha_hasheada = hash_senha(senha)
print(f"Senha hasheada: {senha_hasheada}")

# Verificando a senha
senha_tentativa = "minha_senha_segura"
if hash_senha(senha_tentativa) == senha_hasheada:
    print("Senha correta!")
else:
    print("Senha incorreta!")

# HMAC
mensagem = "Mensagem importante"
chave_secreta = b"minha_chave_secreta"

hash_hmac = hmac.new(chave_secreta, mensagem.encode(), hashlib.sha256).hexdigest()
print(f"HMAC SHA-256: {hash_hmac}")