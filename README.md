cat > README.md << 'EOF'
# TodoMVC UI Tests (Playwright + pytest + GitHub Actions)

[![CI Tests](https://github.com/kikjosler/todo-pom-playwright/actions/workflows/test.yml/badge.svg)](https://github.com/kikjosler/todo-pom-playwright/actions)
[![Playwright](https://img.shields.io/badge/playwright-1.48-brightgreen.svg)](https://playwright.dev/python/docs/intro)
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/)

## **Что тестируем**
## **Е2Е тесты TodoMVC (React)**

| Тест | Сценарий | Время |
|------|----------|-------|
| ➕ `test_add_single_todo` | Добавить 1 задачу | ~5s |
| ➕ `test_add_multiple_todos` | Множественные задачи (Отчет/Звонок/Email) | ~8s |
| ☑️ `test_complete_single_todo` | Выполнить 1 задачу | ~6s |
| ☑️ `test_toggle_all_todos` | Выделить все галочкой | ~7s |
| 🔍 `test_filter_active_todos` | Фильтр "Active" | ~6s |
| 🔍 `test_filter_completed_todos` | Фильтр "Completed" | ~6s |

## **Как запустить**

### **Локально (браузер)**
```bash
git clone https://github.com/kikjosler/todo-pom-playwright.git
cd todo-pom-playwright

# Установка
pip install -r requirements.txt
playwright install

# Запуск всех тестов
pytest tests/ -v -s

# Headless
pytest tests/ -v -s --headed=false
