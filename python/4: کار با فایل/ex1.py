def count_executable_lines(path: str) -> int:
    count = 0
    with open(path, "r") as f:

        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#"):
                count = count + 1
    return count
