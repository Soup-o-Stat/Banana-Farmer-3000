import subprocess
import time

def launch_game():
    steam_command = f'steam://rungameid/2923300'
    subprocess.Popen(['start', steam_command], shell=True)

def kill_game():
    try:
        subprocess.call(['taskkill', '/IM', "Banana.exe", '/F'])
    except Exception as e:
        print(f"Ошибка при завершении игры: {e}")

print("Created by Soup-o-Stat")

while True:
    launch_game()
    print("Запуск Banana")
    time.sleep(70)
    kill_game()
    print(f"+ банан")
    time.sleep(3 * 60 * 60)