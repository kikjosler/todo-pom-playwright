"""Тесты ВЫПОЛНЕНИЯ задач"""

def test_complete_single_todo(todo_page):
    """Выполнить 1 задачу"""
    todo_page.add_todo("Купить молоко")
    todo_page.complete_todo(0)
    assert todo_page.page.locator('.completed').count() == 1

def test_toggle_all_todos(todo_page):
    """Отметить ВСЕ галочкой"""
    todo_page.add_multiple_todos(["Задача 1", "Задача 2"])
    todo_page.toggle_all()
    assert todo_page.page.locator('.completed').count() == 2
