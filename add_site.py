import sys
import os

abbr = sys.argv[1]
url = sys.argv[2]

script_dir = os.path.dirname(os.path.realpath(__file__))
quick_search_file = os.path.join(script_dir, ".quick_search.txt")
config_py_file = os.path.join(script_dir, "quick_search_config.py")

# 1. Update .quick_search.txt
with open(quick_search_file, "a") as f:
    f.write(f"{abbr}  {url}\n")

# 2. Update quick_search_config.py
with open(config_py_file, "r") as f:
    lines = f.readlines()

output_lines = []
inside_return_dict = False
inserted = False

for line in lines:
    stripped = line.strip()

    # Start capturing once we hit return {
    if "return {" in stripped:
        inside_return_dict = True
        output_lines.append(line)
        continue

    # Insert before closing } of the dictionary
    if inside_return_dict and stripped == "}":
        new_line = f'        "{abbr}": f"{url}?{{query}}" if query else "{url}",\n'
        output_lines.append(new_line)
        inserted = True
        inside_return_dict = False

    output_lines.append(line)

# Write back only if the insertion happened
if inserted:
    with open(config_py_file, "w") as f:
        f.writelines(output_lines)
    print(f"✔ Added {abbr}: {url}")
else:
    print("❌ Failed to insert into sites_dict.")