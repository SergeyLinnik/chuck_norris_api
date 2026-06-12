# ============================================================================
# ЗАДАЧА 1: ДОБАВИТЬ В ПРОЕКТ НОВЫЙ ФАЙЛ ДЛЯ ТЕСТОВ
# ЗАДАЧА 2: ИМПОРТИРОВАТЬ НЕОБХОДИМУЮ БИБЛИОТЕКУ
# ============================================================================

import requests
import json
from typing import Dict, Any, Optional, List



# ============================================================================
# ЗАДАЧА 3: СОЗДАТЬ ОБЩИЙ КЛАСС, КОТОРЫЙ БУДЕТ СОДЕРЖАТЬ МЕТОД
# ЗАДАЧА 4: СОЗДАТЬ МЕТОД ДЛЯ ТЕСТА (ПРИНЦИП SOLID)
# ============================================================================

class TestUserCategory:
    """
    Класс для тестирования API Chuck Norris по категории, выбранной пользователем
    Каждый метод отвечает за одну задачу (принцип SOLID)
    """
    
    def __init__(self) -> None:
        """Инициализация базового URL API"""
        self.base_url: str = "https://api.chucknorris.io"
    
    def get_full_url(self, endpoint: str) -> str:
        """
        Формирование полного URL для запроса
        
        Args:
            endpoint: Эндпоинт API
        
        Returns:
            Полный URL
        """
        return self.base_url + endpoint
    
    def send_get_request(self, url: str) -> requests.Response:
        """
        Отправка GET запроса
        
        Args:
            url: URL для запроса
        
        Returns:
            Response объект
        """
        return requests.get(url)
    
    def get_user_category(self) -> str:
        """
        Запрос категории у пользователя
        
        Returns:
            Введенная пользователем категория
        """
        print("\n" + "="*60)
        print(" ВЫБОР КАТЕГОРИИ")
        print("="*60)
        
        category: str = input("\nВведите категорию для получения шутки: ")
        print(f"   ✅ Вы выбрали категорию: '{category}'")
        
        return category.strip().lower()
    
    def get_all_categories(self) -> Optional[List[str]]:
        """
        Получение списка всех категорий
        
        Returns:
            Список категорий или None при ошибке
        """
        endpoint: str = "/jokes/categories"
        full_url: str = self.get_full_url(endpoint)
        
        print(f"\n📡 Отправка запроса для получения всех категорий...")
        print(f"   URL: {full_url}")
        
        response = self.send_get_request(full_url)
        
        if response.status_code == 200:
            categories: List[str] = response.json()
            print(f"   ✅ Получено категорий: {len(categories)}")
            print(f"   📋 Список: {', '.join(categories)}")
            return categories
        else:
            print(f"   ❌ Ошибка: статус-код {response.status_code}")
            return None
    
    def check_category_exists(self, user_category: str, all_categories: List[str]) -> bool:
        """
        Проверка существования категории в списке
        
        Args:
            user_category: Категория, выбранная пользователем
            all_categories: Список всех категорий
        
        Returns:
            True если категория существует, False если нет
        """
        print(f"\n🔍 Проверка наличия категории '{user_category}' в списке...")
        
        if user_category in all_categories:
            print(f"   ✅ Категория '{user_category}' найдена!")
            return True
        else:
            print(f"   ❌ Категория '{user_category}' не найдена в списке")
            print(f"   Доступные категории: {', '.join(all_categories)}")
            return False
    
    def get_joke_by_category(self, category: str) -> Optional[Dict[str, Any]]:
        """
        Отправка запроса для получения шутки по категории
        
        Args:
            category: Название категории
        
        Returns:
            Dictionary с данными шутки или None при ошибке
        """
        endpoint: str = f"/jokes/random?category={category}"
        full_url: str = self.get_full_url(endpoint)
        
        print(f"\n📡 Отправка запроса для получения шутки по категории '{category}'...")
        print(f"   URL: {full_url}")
        
        response = self.send_get_request(full_url)
        
        if response.status_code == 200:
            joke_data: Dict[str, Any] = response.json()
            print(f"   ✅ Шутка получена! Статус-код: {response.status_code}")
            return joke_data
        else:
            print(f"   ❌ Ошибка: статус-код {response.status_code}")
            return None
    
    def print_joke(self, joke_data: Dict[str, Any]) -> None:
        """
        Вывод шутки на печать
        
        Args:
            joke_data: Данные шутки
        """
        print("\n" + "="*60)
        print(" САМА ШУТКА")
        print("="*60)
        
        joke_text: str = joke_data.get("value", "Шутка не найдена")
        joke_id: str = joke_data.get("id", "ID не найден")
        categories: list = joke_data.get("categories", [])
        
        print(f"\n🆔 ID шутки: {joke_id}")
        print(f"📂 Категории: {categories}")
        print(f"\n😂 {joke_text}\n")
    
    def run_user_category_test(self) -> None:
        """
        ЗАДАЧА 5: СОЗДАТЬ ТЕСТ, КОТОРЫЙ ВКЛЮЧАЕТ:
        1. Запросить у пользователя категорию
        2. Отправить запрос для получения всех категорий
        3. Убедиться что данная категория есть в ответе
        4. Отправить запрос для получения шутки
        """
        
        print("\n" + "="*60)
        print(" ТЕСТ: ШУТКА ПО ВЫБОРУ ПОЛЬЗОВАТЕЛЯ")
        print("="*60)
        
        # --------------------------------------------------------------------
        # ШАГ 1: Запросить у пользователя категорию
        # --------------------------------------------------------------------
        print("\n[ШАГ 1] Запрос категории у пользователя...")
        user_category: str = self.get_user_category()
        
        # --------------------------------------------------------------------
        # ШАГ 2: Отправить запрос для получения всех категорий
        # --------------------------------------------------------------------
        print("\n[ШАГ 2] Отправка запроса для получения всех категорий...")
        all_categories: Optional[List[str]] = self.get_all_categories()
        
        if all_categories is None:
            print("\n❌ ТЕСТ НЕ ПРОЙДЕН: Не удалось получить список категорий")
            return
        
        # --------------------------------------------------------------------
        # ШАГ 3: Убедиться что данная категория есть в ответе
        # --------------------------------------------------------------------
        print("\n[ШАГ 3] Проверка наличия категории в списке...")
        
        category_exists: bool = self.check_category_exists(user_category, all_categories)
        
        if not category_exists:
            print(f"\n❌ ТЕСТ НЕ ПРОЙДЕН: Категория '{user_category}' не существует")
            print("Пожалуйста, выберите одну из доступных категорий и запустите тест заново.")
            return
        
        # --------------------------------------------------------------------
        # ШАГ 4: Отправить запрос для получения шутки
        # --------------------------------------------------------------------
        print("\n[ШАГ 4] Отправка запроса для получения шутки...")
        joke_data: Optional[Dict[str, Any]] = self.get_joke_by_category(user_category)
        
        if joke_data is None:
            print("\n❌ ТЕСТ НЕ ПРОЙДЕН: Не удалось получить шутку")
            return
        
        # --------------------------------------------------------------------
        # ВЫВОД ШУТКИ
        # --------------------------------------------------------------------
        self.print_joke(joke_data)
        
        # --------------------------------------------------------------------
        # РЕЗУЛЬТАТ ТЕСТА
        # --------------------------------------------------------------------
        print("="*60)
        print(" РЕЗУЛЬТАТ ТЕСТА")
        print("="*60)
        print("\n✅ ТЕСТ ПРОЙДЕН УСПЕШНО!")
        print(f"   Получена шутка по категории '{user_category}'")


# ============================================================================
# СОЗДАНИЕ ЭКЗЕМПЛЯРА КЛАССА И ВЫЗОВ МЕТОДА
# ============================================================================

if __name__ == "__main__":
    # Создание экземпляра класса
    test_runner = TestUserCategory()
    
    # Вызов метода теста
    test_runner.run_user_category_test()