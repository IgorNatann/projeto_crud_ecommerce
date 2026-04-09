from sqlalchemy import create_engine

# Cria Conexão com o SQLlite em Memória
URI = 'sqlite:///:sqllite_db:'

engine = create_engine(URI, echo=True)

print('Conexão estabelecida com sucesso!')