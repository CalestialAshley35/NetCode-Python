import io
import sys

def code_editor():
    print("Simple Python Code Editor (line-by-line execution; type 'exit' to quit)")
    
    while True:
        # Read a line of input
        line = input(">>> ")
        
        # Exit if the user types 'exit'
        if line.strip().lower() == 'exit':
            print("Exiting code editor.")
            break
        
        # Capture stdout output
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        
        try:
            # Execute the current line of code
            exec(line)
            output = sys.stdout.getvalue()  # Get output from the buffer
        except Exception as e:
            output = f"Error: {e}"
        finally:
            sys.stdout = old_stdout  # Restore original stdout

        # Print the output if any
        if output.strip():
            print(output)

# Run the code editor
code_editor()
