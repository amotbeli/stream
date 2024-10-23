from datetime import datetime
import os

def main():
    folder = "stream-entries"
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    existing_entry = ""

    while True:
        new_entry = input()
        existing_entry += f"\n\n{new_entry}"
        submit = input("press enter to continue (or type 'f' to finish): ").lower().strip()
        if submit == "f":
            break
    
    now = datetime.now()
    time = now.time().replace(microsecond=0)
    title = now.date()
    entry = f"\n{time}{existing_entry}\n"

    file_path = os.path.join(folder, f"{title}.md")
    
    with open(file_path, "a", encoding="utf8") as file:
        file.write(entry)

if __name__ == "__main__":
    main()