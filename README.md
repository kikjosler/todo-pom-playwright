# 🏗️ TodoMVC + Playwright + **POM** (Page Object Model)

[![CI](https://github.com/$(git config user.name)/todo-pom-playwright/actions/workflows/test.yml/badge.svg)](https://github.com/$(git config user.name)/todo-pom-playwright/actions)
[![Tests](https://img.shields.io/badge/tests-6%2F6-brightgreen.svg)]()
[![POM](https://img.shields.io/badge/POM-100%25-blue.svg)]()

## ✨ **6 тест-кейсов TodoMVC (React)**

| Тест | Сценарий | POM метод |
|------|----------|-----------|
| ➕ `test_add_single` | Добавить 1 задачу | `todo_page.add_todo()` |
| ➕ `test_add_multiple` | Добавить несколько | `todo_page.add_multiple_todos()` |
| ✅ `test_complete_single` | Выполнить задачу | `todo_page.complete_todo()` |
| ✅ `test_toggle_all` | Отметить все | `todo_page.toggle_all()` |
| 🔍 `test_filter_active` | Фильтр "Активные" | `todo_page.filter_active()` |
| 🔍 `test_filter_completed` | Фильтр "Выполненные" | `todo_page.filter_completed()` |

## 🏗️ **POM Архитектура (100%)**

cat > requirements.txt << 'EOF'
playwright
pytest
