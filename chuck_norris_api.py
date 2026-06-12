import requests
from typing import Dict, Any, Optional, List

class ChuckNorrisApiClient:
    def __init__(self) -> None:
        self.base_url: str = "https://api.chucknorris.io"
    
    def get_full_url(self, endpoint: str) -> str:
        return self.base_url + endpoint
    
    def send_get_request(self, url: str) -> requests.Response:
        return requests.get(url)
    
    def get_random_joke_by_category(self, category: str) -> Optional[Dict[str, Any]]:
        endpoint: str = f"/jokes/random?category={category}"
        full_url: str = self.get_full_url(endpoint)
        print(f"\nURL запроса: {full_url}")
        response = self.send_get_request(full_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка: статус-код {response.status_code}")
            return None
    
    def get_categories_list(self) -> Optional[List[str]]:
        endpoint: str = "/jokes/categories"
        full_url: str = self.get_full_url(endpoint)
        response = self.send_get_request(full_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Ошибка получения категорий: {response.status_code}")
            return None