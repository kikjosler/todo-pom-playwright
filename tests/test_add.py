import pytest

def test_add_single_todo(todo_page):
    """Добавить ОДНУ задачу"""
    todo_page.add_todo("Купить молоко")
    assert todo_page.get_todos_count() == 1  # get_todos_count()!

@pytest.mark.parametrize("task", ["Отчет", "Звонок", "Email"])
def test_add_multiple_todos(todo_page, task):
    """Добавить задачу из списка"""
    todo_page.add_todo(task)
    assert todo_page.get_todos_count() == 1  # get_todos_count()!
