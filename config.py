import sys

database_path = 'clientes.csv'

if 'pytest' in sys.argv[0]:
    database_path = 'Tests/clientes_test.csv'