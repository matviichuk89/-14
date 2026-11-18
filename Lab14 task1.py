file_path = "result.json"
import requests
import json
import bs4
tag = input("Введіть тег: ")
url = input("Введіть URL-адресу веб-сторінки: ")
get_url = requests.get(url)
if get_url.status_code == 200:
    print("Веб-сторінка доступна.")
    soup = bs4.BeautifulSoup(get_url.text, "html.parser")
    found_tags = soup.find_all(tag)
    if found_tags:
        print(f"Тег '{tag}' знайдено на веб-сторінці.")
    else:
        print(f"Тег '{tag}' не знайдено на веб-сторінці.")
    print(f"Кількість знайдених тегів '{tag}': {len(found_tags)}")
    result = {
        "url": url,
        "tag": tag,
        "count": len(found_tags)
    }
    try:
        with open(file_path, "r") as f:
            results = json.load(f)
    except FileNotFoundError:
        results = []
results.append(result)
with open(r"C:\Users\Nazar\OneDrive\Desktop\result.json", "w") as f:
    json.dump(results, f, ensure_ascii=False, indent=4)