# The grep and sed exercises done in Python.
import re
import subprocess
import sys
from pathlib import Path


def browser_processes(name):
    """ps aux | grep -i <name>"""
    output = subprocess.run(["ps", "aux"], capture_output=True, text=True, check=True).stdout
    return [line for line in output.splitlines() if name.lower() in line.lower()]


def replace_package(text):
    """sed 's/package/PACKAGE/Ig'"""
    return re.sub("package", "PACKAGE", text, flags=re.IGNORECASE)


def delete_package_lines(text):
    """sed '/PACKAGE/d'"""
    return "".join(line for line in text.splitlines(keepends=True) if "PACKAGE" not in line)


sample = "This Package is free.\nNo match here.\nsee package.json\n"
assert replace_package(sample) == "This PACKAGE is free.\nNo match here.\nsee PACKAGE.json\n"
assert delete_package_lines(replace_package(sample)) == "No match here.\n"


def process_licenses(source, destination):
    # writes edited copies; /usr/share is read-only for normal users, like sed without -i
    destination.mkdir(exist_ok=True)
    for file in sorted(source.iterdir()):
        if file.is_file():
            text = file.read_text(encoding="utf-8", errors="replace")
            replaced = replace_package(text)
            (destination / f"{file.name}.replaced").write_text(replaced, encoding="utf-8")
            (destination / f"{file.name}.deleted").write_text(delete_package_lines(replaced), encoding="utf-8")
            print("Processed", file.name)


if __name__ == "__main__":
    browser = sys.argv[1] if len(sys.argv) > 1 else "firefox"
    for line in browser_processes(browser):
        print(line)
    licenses = Path("/usr/share/common-licenses")
    if licenses.is_dir():
        process_licenses(licenses, Path("common-licenses-edited"))
    else:
        print(licenses, "not found (Debian/Ubuntu only)")
