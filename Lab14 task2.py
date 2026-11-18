file_path = "links.txt"
import requests
import bs4
url = input("Введіть URL-адресу веб-сторінки: ")
get_url = requests.get(url)
if get_url.status_code == 200:
    print("Веб-сторінка доступна.")
    soup = bs4.BeautifulSoup(get_url.text, "html.parser")
    links = soup.find_all("a")
    file_path = "C:\\Users\\Nazar\\OneDrive\\Desktop\\links.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        for link in links:
            link_text = link.get_text(strip=True)
            f.write(f"{link_text}\n")