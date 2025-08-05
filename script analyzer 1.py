import re


def get_code_from_user():
    print("Paste Your Code:\n")
    lines=[]
    while True:
        line=input()
        if line.strip().upper()=="END":
            break
        lines.append(line)
    return lines

def explain_line(line):
    line = line.strip()
    if line.startswith("#"):
        return f"Comment:{line[1:].strip()}"
    elif line.startswith("class "):
        class_name = line.split()[1].split('(')[0].strip(':')
        return f"Defines a class named'{class_name}'."
    elif line.startswith("if"):
        return f"condition statements'{line}'."
    elif line.startswith("def "):
        func_name = line.split()[1].split('(')[0]
        return f"defines a function/method called'{func_name}()'."
    elif "import" in line:
        return f"imports module(s):{line}"
    elif "=" in line and not line.startswith("def"):
        return f"variable assignment:{line}"
    elif "print(" in line:
        return f"print statement:{line}"
    elif line == "":
        return ""
    else:
        return f"general execution:{line}"


def generate_explanations(lines):
    explanation = []
    for idx, line in enumerate(lines, 1):
        explanation.append(f"{idx:03}:{line.rstrip()}")
        explanation.append(f"{explain_line(line)}\n")
    return "\n".join(explanation)


def generate_ascii_uml(lines):
    classes = {}
    current_class = None
    for line in lines:
        line_stripped = line.strip()
        class_match = re.match(r'class\s+(\w+)', line_stripped)
        method_match = re.match(r'def\s+(\w+)', line_stripped)
        if class_match:
            current_class = class_match.group(1)
            classes[current_class] = []
        elif method_match and current_class:
            method_name=method_match.group(1)
            classes[current_class].append(method_name)
    if not classes:
        return 'no classes definition found'
    uml_output = ["\n===ASCII UML DIAGRAM===\n"]
    for cls, methods in classes.items():
         uml_output.append(f"+-------------------+")
         uml_output.append(f"|class:{cls:<13}|")
         uml_output.append(f"+-------------------+")
         for method in methods:
             uml_output.append(f"| - {method:<16}|")
         uml_output.append(f"+-------------------+\n")
    return "\n".join(uml_output)


def main():
    code_lines = get_code_from_user()
    print("\n===Code Explanation===\n")
    print(generate_explanations(code_lines))
    print(generate_ascii_uml(code_lines))
if __name__ == "__main__":
    main()
