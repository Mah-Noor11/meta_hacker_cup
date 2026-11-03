def solve_case(t, N, A, horizontal_lines):
    if N <= 1:
        horizontal_lines.append(f"Case #{t}: 0")
        return
    max_diff = 0
    for i in range(N - 1):
        diff = abs(A[i + 1] - A[i])
        if diff > max_diff:
            max_diff = diff

    horizontal_lines.append(f"Case #{t}: {max_diff}")


def main():
    input_path = r"C:\Users\user\Desktop\meta_hacker_cup_2025\Round_1\snake_scales_chapter_1_input.txt"
    output_path = r"C:\Users\user\Desktop\meta_hacker_cup_2025\Round_1\output.txt"

    vertical_lines = []

    with open(input_path, "r") as f:
        t = int(f.readline().strip())
        for t in range(1, t + 1):
            N = int(f.readline().strip())
            A = list(map(int, f.readline().strip().split()))
            solve_case(t, N, A, vertical_lines)

    with open(output_path, "w") as out:
        out.write("\n".join(vertical_lines))

    print(f"Output: {output_path}")


if __name__ == "__main__":
    main()
