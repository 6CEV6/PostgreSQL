import psycopg2


conn = None
cursor = None

try:
    connection = psycopg2.connect(
        host="localhost",  # lub odpowiedni adres hosta Dockera
        port="5432",  # standardowy port Postgresa
        database="postgres",  # nazwa Twojej bazy danych
        user="postgres",  # użytkownik bazy
        password="postgres"  # hasło do bazy
    )

    print("Połączenie z bazą danych nawiązane pomyślnie.")

    # Utworzenie kursora
    cursor = conn.cursor()

    # Wstawianie danych do tabeli
    insert_query = """
        INSERT INTO public.pracownicy (imie, nazwisko, stanowisko, pensja) 
        VALUES (%s, %s, %s, %s);
        """
    # Przykładowe dane do wstawienia
    data = ("Jan", "Kowalski", "Programista", 6000)

    # Wykonanie zapytania INSERT
    cursor.execute(insert_query, data)

    # Potwierdzenie zmian w bazie danych
    conn.commit()

    print("Dane zostały wstawione pomyślnie.")

except psycopg2.Error as e:
    print(f"Wystąpił błąd podczas nawiązywania połączenia: {e}")

finally:
    # Zakończenie połączenia
    if cursor:
        cursor.close()
    if conn:
        conn.close()