import requests
import json
from typing import Dict, Any, Optional, List


class TestAllCategories:
    """Класс для тестирования всех категорий API Chuck Norris"""
    
    def __init__(self) -> None:
        """Инициализация базового URL API"""
        self.base_url: str = "https://api.chucknorris.io"
    
    def get_full_url(self, endpoint: str) -> str:
        """Формирование полного URL для запроса"""
        return self.base_url + endpoint
    
    def send_get_request(self, url: str) -> requests.Response:
        """Отправка GET запроса"""
        return requests.get(url)
    
    def get_all_categories(self) -> Optional[List[str]]:
        """Получение списка всех категорий"""
        endpoint: str = "/jokes/categories"
        full_url: str = self.get_full_url(endpoint)
        
        print(f"\n📡 Запрос списка категорий...")
        print(f"   URL: {full_url}")
        
        response = self.send_get_request(full_url)
        
        if response.status_code == 200:
            categories: List[str] = response.json()
            print(f"   ✅ Получено категорий: {len(categories)}")
            return categories
        else:
            print(f"   ❌ Ошибка: статус-код {response.status_code}")
            return None
    
    def get_joke_by_category(self, category: str) -> Optional[Dict[str, Any]]:
        """Получение случайной шутки по категории"""
        endpoint: str = f"/jokes/random?category={category}"
        full_url: str = self.get_full_url(endpoint)
        
        response = self.send_get_request(full_url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"   ❌ Ошибка для категории '{category}': {response.status_code}")
            return None
    
    def print_joke_info(self, category: str, joke_data: Dict[str, Any]) -> None:
        """Вывод информации о шутке"""
        joke_text: str = joke_data.get("value", "Шутка не найдена")
        joke_id: str = joke_data.get("id", "ID не найден")
        
        print(f"\n   📍 Категория: {category}")
        print(f"   🆔 ID: {joke_id}")
        if len(joke_text) > 80:
            print(f"   💬 Шутка: {joke_text[:80]}...")
        else:
            print(f"   💬 Шутка: {joke_text}")
    
    def test_all_categories_get_jokes(self) -> None:
        """Тест: получить все категории и по 1 шутке из каждой"""
        
        print("\n" + "="*70)
        print(" ТЕСТ: ПОЛУЧЕНИЕ ШУТОК ПО ВСЕМ КАТЕГОРИЯМ")
        print("="*70)
        
        # ШАГ 1: Получение всех категорий
        print("\n[1] Отправка запроса для получения всех категорий...")
        
        categories: Optional[List[str]] = self.get_all_categories()
        
        if categories is None:
            print("\n❌ ТЕСТ НЕ ПРОЙДЕН: Не удалось получить категории")
            return
        
        if len(categories) == 0:
            print("\n❌ ТЕСТ НЕ ПРОЙДЕН: Список категорий пуст")
            return
        
        print(f"\n   📋 Все категории ({len(categories)}):")
        print(f"   {', '.join(categories)}")
        
        # ШАГ 2: Получение шутки по каждой категории
        print("\n[2] Получение 1 шутки по каждой категории...")
        
        success_count: int = 0
        fail_count: int = 0
        
        for category in categories:
            print(f"\n   --- Категория: {category} ---")
            
            joke_data: Optional[Dict[str, Any]] = self.get_joke_by_category(category)
            
            if joke_data is not None:
                self.print_joke_info(category, joke_data)
                success_count += 1
            else:
                print(f"   ❌ Не удалось получить шутку")
                fail_count += 1
        
        # РЕЗУЛЬТАТЫ
        print("\n" + "="*70)
        print(" РЕЗУЛЬТАТЫ ТЕСТА")
        print("="*70)
        
        print(f"\n📊 Статистика:")
        print(f"   Всего категорий: {len(categories)}")
        print(f"   ✅ Успешно получено шуток: {success_count}")
        print(f"   ❌ Не удалось получить: {fail_count}")
        
        if success_count == len(categories):
            print("\n✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")
        else:
            print(f"\n⚠️ ТЕСТ ПРОЙДЕН ЧАСТИЧНО")


if __name__ == "__main__":
    test_runner = TestAllCategories()
    test_runner.test_all_categories_get_jokes()