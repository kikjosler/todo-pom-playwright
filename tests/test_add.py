"""Тесты ДОБАВЛЕНИЯ задач"""

def test_add_single_todo(todo_page):
    """Добавить ОДНУ задачу"""
    todo_page.add_todo("Купить молоко")
    assert todo_page.get_todo_count() == 1

@pytest.mark.parametrize("task", ["Отчет", "Звонок", "Email"])
def test_add_multiple_todos(todo_page, task):
    """Добавить задачу из списка"""
    todo_page.add_todo(task)
    assert todo_page.get_todo_count() == 1
