def grep(query, files):
    try:
        for file_name in files:
            with open(file_name) as file:
                for i, line in enumerate(file):
                    if query in line:
                        print(f"[{file_name}] Line {i + 1}: {line}")
    except:
        sys.exit(f"Error trying to open {sys.argv[1]}")