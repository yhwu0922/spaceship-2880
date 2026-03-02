import re

with open('tmp_map.json', 'r', encoding='utf-8') as f:
    map_str = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

new_text = re.sub(r'const MAP_DATA = \[\s*(?:\[.*?\]\s*,\s*)*\[.*?\]\s*\];', f"const MAP_DATA = {map_str};", text)

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("done")
