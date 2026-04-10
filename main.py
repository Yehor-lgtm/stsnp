import subprocess 
import sys

IGNORE = {
        'bare',
        'core20',
        'core22',
        'core24',
        'gaming-graphics-core24',
        'gnome-42-2204',
        'gtk-common-themes',
}
def get_apps():
    result = subprocess.run(["snap", "list"], capture_output=True, text=True)
    lines = result.stdout.splitlines()

    apps=[]
    for line in lines[1:]:
        parts = line.split()
        if parts and parts[0] not in IGNORE:
            apps.append(parts[0])
    return apps

def show_apps(apps):
    for i, app in enumerate(apps, start=1):
        print(f"{i}. {app}")

def ask():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        return None
    
def run(app):
    subprocess.run(["snap", "run", app])

def main():
    apps = get_apps()

    if len(sys.argv) > 1:
        command = sys.argv[1]
        app = sys.argv[2] if len(sys.argv) > 2 else None
        
        if command == "show":
            show_apps(apps)

        elif command == "run":
            if not app:
                print("Specify app")
                return
            run(app)

        elif command == "help":
            print("commands: \nshow:  show apps\nrun <app>: run app")

        else:
            print("Usage: python3 main.py <command> <app(only if you use run)>")
    else:
        try:
            show_apps(apps)
            choice = ask()
            run(apps[choice-1])
        except IndexError:
            print("Invalid number")

if __name__ == '__main__':
    main()
