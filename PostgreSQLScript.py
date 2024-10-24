import psycopg2
import pandas as pd

# Dane połączenia z bazą
connection = psycopg2.connect(
    host="localhost",  # lub odpowiedni adres hosta Dockera
    port="5432",       # standardowy port Postgresa
    database="postgres",  # nazwa Twojej bazy danych
    user="postgres",  # użytkownik bazy
    password="postgres"   # hasło do bazy
)

# Tworzenie kursora do wykonywania zapytań
cursor = connection.cursor()

# Przykładowe zapytanie
query = "SELECT * FROM twoja_tabela LIMIT 10;"

# Wykonaj zapytanie
cursor.execute(query)

# Pobierz wyniki i zamień na DataFrame (jeśli używasz Pandas)
rows = cursor.fetchall()
df = pd.DataFrame(rows, columns=[desc[0] for desc in cursor.description])

# Zamknij połączenie
cursor.close()
connection.close()

# Wyświetl wyniki
print(df.head())