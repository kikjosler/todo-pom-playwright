from playwright.sync_api import Page

class TodoPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_todo_input = page.locator('input.new-todo')
        self.todo_list = page.locator('.todo-list li')
        self.toggle_all_checkbox = page.locator('.toggle-all')  # ✅ Имя с _checkbox
        self.filter_links = page.locator('.filters a')
        
    def add_todo(self, task: str):
        self.new_todo_input.fill(task)
        self.new_todo_input.press("Enter")
        
    def add_multiple_todos(self, tasks):
        for task in tasks:
            self.add_todo(task)
            
    def get_todos_count(self):
        return self.todo_list.count()
        
    def complete_todo(self, index):
        self.todo_list.nth(index).locator('.toggle').click()
        
    def toggle_all(self):
        self.toggle_all_checkbox.click()
        
    def filter_active(self):
        self.filter_links.nth(1).click()
        
    def filter_completed(self):
        self.filter_links.nth(2).click()
