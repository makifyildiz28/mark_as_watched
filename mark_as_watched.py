import requests

# Trakt API ayarları
client_id = '3c63462cb8aa0937b24461110f0feafa5717197e8535e1ce1d18f78480b89a0b'
client_secret = 'dce0c9524cd08e67291772dd056189a2ee32bc1550cb9d90c878b1a1082d06d2'
access_token = 'urn:ietf:wg:oauth:2.0:oob'  # OAuth ile edinilen erişim tokeni
api_url = 'https://api.trakt.tv'
list_name = 'Watched'  # İşlem yapmak istediğiniz listenin adı
username = 'akif28'  # Trakt kullanıcı adınız

headers = {
    'Content-Type': 'application/json',
    'trakt-api-version': '2',
    'trakt-api-key': client_id,
    'Authorization': f'Bearer {access_token}'
}

# Listeyi getir
response = requests.get(f"{api_url}/users/{username}/lists/{list_name}/items", headers=headers)
list_items = response.json()

# İzlenen olarak işaretleme yapılacak filmlerin listesini hazırla
watched_movies = {
    "movies": [{"ids": {"trakt": movie['movie']['ids']['trakt']}} for movie in list_items if movie['type'] == 'movie']
}

# Filmleri izlenen olarak işaretle
response = requests.post(f"{api_url}/sync/history", json=watched_movies, headers=headers)

if response.status_code == 201:
    print("Filmler başarıyla izlenen olarak işaretlendi.")
else:
    print("Bir hata oluştu:", response.status_code, response.text)
