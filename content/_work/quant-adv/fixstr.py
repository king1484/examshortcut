import sys

def fix(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        L = lines[i]
        st = L.lstrip()
        if st.startswith('r"') and not L.rstrip().endswith(('"', '",', '"):')):
            j = i
            while j < len(lines) and not lines[j].rstrip().endswith(('"', '",', '"):')):
                j += 1
            end = lines[j].rstrip()
            if end.endswith('",'):
                lines[j] = end[:-2] + '""",'
            elif end.endswith('"):'):
                lines[j] = end[:-3] + '"""):'
            else:
                lines[j] = end[:-1] + '"""'
            out.append(L.replace('r"', 'r"""', 1))
            n += 1
            i += 1
            continue
        out.append(L)
        i += 1
    open(path, "w", encoding="utf-8").write("\n".join(out))
    print(path, "fixed", n)

for p in sys.argv[1:]:
    fix(p)
