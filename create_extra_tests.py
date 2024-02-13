import os
# List of expressions to be evaluated
expressions = [
    "1 * (1 - 2 * 3) // 3",
    "(True or False) and not True",
    "1 if 2 < 3 else 4",
    "[1, 2, 3][0] * 2",
    "1 + 2 if 3 > 2 else 4 + 5",
    "((1 + 2) * 3) // 4 % 5",
    "1 * -2",
    "1 - -2",
    "not (True or False)",
    "1 if 2 else 3 if 4 else 5",
    "[1, 2][1 if True else 0]",
    "[1] + [2]",
    "len([1, 2, 3])",
    "\"hello\" + \" world\"",
    "\"hi\"[0]",
    "1 and 2 or 3 and 4",
    "(1 + 2) * (3 if 4 > 5 else 6)",
    "1 if (2 if 3 else 4) else 5",
    "not True or False and True",
    "1 if not True else 2",
    "1 // 2 * 3 % 4",
    "1 * 2 + 3 - 4 // 5",
    "-1 * -2",
    "1 * ((2 + 3) * 4)",
    "1 * - (2 + 3)",
    "[1, 2, 3][-1]",
    "1 + 2 - (3 * 4 // 5)",
    "(1 + 2) - [3, 4][0]",
    "len(\"hello\") + len(\"world\")",
    "1 * 2 if 3 == 4 else 5",
    "1 + (2 if True else 3) * 4",
    "not (1 < 2) and (3 > 4)",
    "1 if 2 == 2 else 3 if 4 != 4 else 5",
    "[1, 2, 3][1:2][0]",
    "1 + 2 * 3 % 4 // 5 - 6",
    "True if False else False if True else True",
    "[1, 2, 3][1 if 1 < 2 else 2]",
    "1 * (2 if 3 < 4 else 5) + 6",
    "1 + 2 - 3 * 4 // (5 if 6 > 7 else 8)",
    "1 and 2 or 3 and (4 if 5 < 6 else 7)",
    "((1 + 2) if 3 else (4 - 5)) * 6",
    "-1 if not True else -2",
    "[1, 2, 3][0] + (4 if 5 else 6)",
    "\"string\"[1 if True else 2]",
    "1 + 2 * (3 if \"a\" == \"a\" else 4)",
    "(1 * 2) if (3 + 4) > 5 else 6",
    "1 if (2 if (3 if True else False) else 4) else 5",
    "not True if False else not False",
    "1 * -2 if 3 // 4 else 5 % 6",
    "1 + (2 if [1, 2][0] == 1 else 3)",
    "[1, 2, 3][0 if True else 1] * 2",
    "1 if True else 2 if False else 3 if True else 4",
    "1 * 2 + (3 // 4) - 5 % 6",
    "1 and (2 or 3) and 4",
    "1 if 2 < 3 else 4 if 5 > 6 else 7",
    "def f():\n  pass",  # Minimal function
    "x: int = 10",  # Variable declaration with initialization
    "def f(x: int) -> bool:\n  return x > 0",  # Function with parameters and return type
    "if True:\n  pass",  # Simple if statement
    "while False:\n  pass",  # Simple while loop
    "for i in [1, 2, 3]:\n  pass",  # Simple for loop
    "x: [int] = [1, 2, 3]",  # List type annotation
    "def f(x: [int]):\n  pass",  # Function with list parameter
    "x: int = 1 + 2 * 3",  # Expression with operators of different precedence
    "x: bool = not True or False and True",  # Logical operators with precedence
    "if x > 0 and x < 10:\n  pass",  # Compound condition in if
    "x: int = 1\nx = x + 1",  # Variable reassignment
    "def f():\n  x: int = 0\n  x = x + 1\n  return x",  # Local variable scope
    "x: int = 0\ndef f():\n  global x\n  x = x + 1",  # Global variable modification
    "def f():\n  y: int = 0\n  def g():\n    nonlocal y\n    y = y + 1",  # Nonlocal variable modification
    "if x > 0:\n  pass\nelif x < 0:\n  pass\nelse:\n  pass",  # If-elif-else chain
    "x: [int] = [1, 2, 3]\ny: int = x[1]",  # List indexing
    "x: [int] = [1]\nx.append(2)",  # List method call (assuming .append is allowed)
    "def f(x: int) -> int:\n  if x <= 1:\n    return x\n  else:\n    return f(x-1) + f(x-2)",  # Recursive function
    "x: int = 0\nwhile x < 10:\n  x = x + 1",  # While loop with increment
    "for i in range(10):\n  pass",  # For loop with range (assuming range is allowed)
    "x: bool = True if 1 > 0 else False",  # Conditional expression
    "def f(x: int) -> [int]:\n  return [x, x+1]",  # Function returning a list
    "x: [[int]] = [[1, 2], [3, 4]]",  # Nested list
    "def f() -> [[int]]:\n  return [[1, 2], [3, 4]]",  # Function returning a nested list
    "def f(x: [[int]]):\n  pass",  # Function with nested list parameter
    "x: int = 1 // 2",  # Integer division
    "x: int = 10 % 3",  # Modulus operator
    "x: int = -1",  # Unary minus
    "x: bool = 1 == 1",  # Equality comparison
    "x: bool = 1 != 1",  # Inequality comparison
    "x: bool = 1 < 2",  # Less than comparison
    "x: bool = 1 <= 1",  # Less than or equal comparison
    "x: bool = 2 > 1",  # Greater than comparison
    "x: bool = 2 >= 2"
]

# Directory to store the files
directory = "tests/extra_test/tests/"
if not os.path.exists(directory):
    # Create the directory, including any necessary parent directories
    os.makedirs(directory)
    print(f"Directory '{directory}' was created.")
else:
    print(f"Directory '{directory}' already exists.")
import subprocess



for index, expr in enumerate(expressions, start=1):
    # Filename based on the index
    filename = f"{directory}test_{index}.choc"
    
    # Content to be written in the file
    content = f"""# RUN: choco-opt %s | filecheck %s

{expr}
"""
    
    # Writing the content to the file
    with open(filename, 'w') as file:
        file.write(content)

    print(f"File '{filename}' has been created.")
    
for index, expr in enumerate(expressions, start=1):
    filename = f"{directory}test_{index}.choc"
    
    # The command to run choco-opt on a file
    command = ["choco-opt", filename]

    # Running the command and capturing the output
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout  # This variable contains the stdout of the command
        error = result.stderr  # This variable contains the stderr of the command, if any
        # Transforming the output to the specified format
        # Transforming the output with the first line as "CHECK" and the rest as "CHECK-NEXT"
        lines = output.strip().split('\n')
        transformed_lines = [''] * len(lines)
        transformed_lines[0] = '# CHECK:' + lines[0].strip("\n") + "\n"
        for i in range(1, len(lines)):
            transformed_lines[i] = '# CHECK-NEXT:' + lines[i].strip("\n") + "\n"
        
        with open(filename, 'r') as file:
            initial_content = file.readlines()
        final_content = initial_content + ['\n'] + transformed_lines


        # # Writing the transformed content to the file
        print(final_content)
        with open(filename, 'w') as file:
            file.write(''.join(final_content))

        # transformed_filename
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {e}")
        output = e.output
        error = e.stderr