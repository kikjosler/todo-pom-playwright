"""Тесты ФИЛЬТРОВ"""

def test_filter_active_todos(todo_page):
    """Фильтр 'АКТИВНЫЕ'"""
    todo_page.add_todo("Активная")
    todo_page.add_todo("Выполненная")
    todo_page.complete_todo(1)  # 2-я задача = выполненная
    
    todo_page.filter_active()
    assert todo_page.page.locator('.todo-list li').count() == 1

def test_filter_completed_todos(todo_page):
    """Фильтр 'ВЫПОЛНЕННЫЕ'"""
    todo_page.add_todo("Задача")
    todo_page.complete_todo(0)
    todo_page.filter_completed()
    assert todo_page.page.locator('.todo-list li').count() == 1
