import time
import importlib.util
import requests
from arenachess.api import post_move


def load_make_move(path):
    """
    Загружает пользовательскую функцию make_move из указанного файла.
    
    Args:
        path (str): Путь к файлу make_move.py.
    
    Returns:
        function: Функция make_move из модуля.
    """
    spec = importlib.util.spec_from_file_location("make_move", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.make_move


def fetch_task(user_token):
    """
    Запрашивает следующую задачу у сервера.
    
    Args:
        user_token (str): Токен пользователя для аутентификации.
    
    Returns:
        dict: Данные задачи, если доступна, иначе None.
    """
    try:
        response = requests.get(
            "https://arenachess.com/engines/next_task", 
            params={"user_token": user_token},
            timeout=10
        )
        if response.status_code == 200:
            task = response.json()
            if task.get("task_available"):
                return task
    except Exception as e:
        print(f"Error fetching task: {e}")
    return None


def start_engine(user_token, path_to_make_move):
    """
    Запускает шахматный движок для обработки задач от сервера.
    
    Args:
        user_token (str): Токен пользователя для аутентификации.
        path_to_make_move (str): Путь к файлу make_move.py.
    """
    make_move = load_make_move(path_to_make_move)
    print("Engine started. Waiting for tasks...")

    while True:
        task = fetch_task(user_token)  # Запрашиваем задачу у сервера
        if task is None:
            time.sleep(0.5)  # Если задач нет, подождать немного перед следующим запросом
            continue

        try:
            match_id = task["match_id"]
            board_fen = task["board_fen"]
            current_color = task["current_color"]

            # Вызываем пользовательскую функцию make_move
            move = make_move(board=board_fen, match_id=match_id, user_color=current_color)

            # Отправляем ход на сервер
            post_move(user_token, match_id, move)
            print(f"Move {move} submitted for match {match_id}")

        except Exception as e:
            print(f"Error processing task: {e}")
            time.sleep(0.5)  # Подождать немного при ошибке перед следующей попыткой
