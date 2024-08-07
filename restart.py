import subprocess
import os
import time

def restart_bot():
    process = subprocess.Popen(
        ['ps', 'aux'],
        stdout=subprocess.PIPE
    )
    output, error = process.communicate()

    for line in output.decode().split('\n'):
        if 'python3' in line and 'main.py' in line:
            pid = int(line.split()[1])
            subprocess.run(
                ['kill', str(pid)]
            )
            print(
                f"Stopped bot process with PID {pid}"
            )

    script_path = os.path.join(
        os.path.dirname(__file__),
        'main.py'
    )
    subprocess.Popen(
        [
            'nohup',
            'python3',
            script_path,
            '&'
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    print("Bot restarted")

restart_bot()
