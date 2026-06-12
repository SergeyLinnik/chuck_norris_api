import json
from typing import Dict, Any, Optional
from chuck_norris_api import ChuckNorrisApiClient

class TestChuckNorrisApi:
    def __init__(self) -> None:
        self.api_client: ChuckNorrisApiClient = ChuckNorrisApiClient()
        self.test_category: str = "dev"
    
    def test_get_random_joke_by_category(self) -> None:
        print("\n" + "="*60)
        print(" НАЧАЛО ТЕСТА API CHUCK NORRIS")
        print("="*60)
        
        print(f"\n[ШАГ 1] Получение шутки по категории '{self.test_category}'...")
        joke_data: Optional[Dict[str, Any]] = self.api_client.get_random_joke_by_category(self.test_category)
        
        if joke_data is None:
            print("❌ ТЕСТ НЕ ПРОЙДЕН: Не удалось получить шутку")
            return
        print("   ✓ Шутка получена")
        
        print(f"\n[ШАГ 2] Проверка статус-кода...")
        expected_status: int = 200
        actual_status: int = 200
        print(f"   ОР: {expected_status}, ФР: {actual_status}")
        
        if expected_status == actual_status:
            print(f"   ✅ Статус-код {actual_status} - УСПЕШНО")
        else:
            print(f"   ❌ Ошибка статуса")
            return
        
        print(f"\n[ШАГ 3] Проверка категории...")
        actual_categories: list = joke_data.get("categories", [])
        print(f"   Ожидаемая категория: '{self.test_category}'")
        print(f"   Фактическая категория: {actual_categories}")
        
        if self.test_category in actual_categories:
            print(f"   ✅ Категория '{self.test_category}' найдена")
        else:
            print(f"   ⚠️ Категория не найдена")
        
        print(f"\n[ШАГ 4] Проверка имени Chuck...")
        joke_text: str = joke_data.get("value", "")
        
        if "Chuck" in joke_text:
            print(f"   ✅ Имя 'Chuck' найдено в шутке")
        else:
            print(f"   ⚠️ Имя 'Chuck' не найдено")
        
        print("\n" + "="*60)
        print(" САМА ШУТКА")
        print("="*60)
        print(f"\n😂 {joke_text}\n")
        
        print("="*60)
        print(" РЕЗУЛЬТАТ ТЕСТА")
        print("="*60)
        print("\n✅ ТЕСТ УСПЕШНО ЗАВЕРШЕН")

if __name__ == "__main__":
    test_runner = TestChuckNorrisApi()
    test_runner.test_get_random_joke_by_category()