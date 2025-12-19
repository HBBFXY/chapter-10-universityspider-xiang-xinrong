import requests
from bs4 import BeautifulSoup
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
} 

universities = []

def get_university_info(page):
    url = f"https://www.shanghairanking.cn/rankings/best-chinese-universities/{page}"
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        rows = soup.find('table', class_='rk-table').find_all('tr')[1:]
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 4:
                rank = cols[0].text.strip()
                name = cols[1].text.strip()
                score = cols[3].text.strip()
                universities.append({'rank': rank, 'name': name, 'score': score})
        time.sleep(1)
    except Exception as e:
        print(f"Page {page} error: {e}")

def main():
    for page in range(1, 11):
        get_university_info(page)
        print(f"Page {page} crawled")
    for uni in universities:
        print(uni)

if __name__ == "__main__":
    main()
