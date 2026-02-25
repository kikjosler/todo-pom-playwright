from playwright.sync_api import Page, expect

class TodoPage:
    """TodoMVC - Page Object Model"""
    
    def __init__(self, page: Page):
        self.page = page
        
        # ЛОКАТОРЫ (ВСЕ В ОДНОМ МЕСТЕ!)
        self.new_todo_input = page.locator('.new-todo')           # Поле ввода
        self.todo_items = page.locator('.todo-list li')           # Список задач
        self.toggle_all_checkbox = page.locator('.toggle-all')    # "Отметить все"
        self.todo_count = page.locator('.todo-count strong')      # Счетчик
        self.filters = page.locator('.filters a')                 # Фильтры
    
    def add_todo(self, text: str):
        """Добавить задачу"""
        self.new_todo_input.fill(text)
        self.new_todo_input.press('Enter')
        expect(self.todo_items).to_have_count(1)
    
    def add_multiple_todos(self, todos: list):
        """Добавить много задач"""
        for todo in todos:
            self.add_todo(todo)
    
    def complete_todo(self, index: int = 0):
        """Выполнить задачу №index"""
        self.todo_items.nth(index).locator('.toggle').click()
    
    def toggle_all(self):
        """Отметить ВСЕ галочкой"""
        self.toggle_all_checkbox.click()
    
    def get_todo_count(self) -> int:
        """Количество задач"""
        count_text = self.todo_count.text_content()
        return int(count_text.split()[0]) if count_text else 0
    
    def filter_active(self):
        """Показать АКТИВНЫЕ"""
        self.filters.locator('href="#/active"').click()
    
    def filter_completed(self):
        """Показать ВЫПОЛНЕННЫЕ"""
        self.filters.locator('href="#/completed"').click()
