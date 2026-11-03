def solve_case(tc, N, A, B, output_lines):
    for i in range(N):
        if B[i] < A[i]:
            output_lines.append(f"Case #{tc}: -1")
            return

    position = [0] * (max(max(A), max(B)) + 1)
    for i in range(len(A)):
        temp = A[i]
        if position[temp] == 0:
            position[temp] = i + 1

    for temp in B:
        if temp >= len(position) or position[temp] == 0:
            output_lines.append(f"Case #{tc}: -1")
            return

    groups = [[] for _ in range(len(position))]
    for i in range(N):
        if A[i] != B[i]:
            groups[B[i]].append(i + 1)

    operations = []
    for v in range(1, len(groups)):
        if groups[v]:
            donor = position[v]
            for idx in groups[v]:
                operations.append((donor, idx))

    output_lines.append(f"Case #{tc}: {len(operations)}")
    for donor, target in operations:
        output_lines.append(f"{donor} {target}")


def main():
    input_path = r"C:\Users\Mahnoor\Documents\meta_hacker_cup_2025\problem_1\warm_up_input.txt"
    output_path = r"C:\Users\Mahnoor\Documents\meta_hacker_cup_2025\problem_1\output.txt"

    output_lines = []
    with open(input_path, "r") as f:
        t = int(f.readline())
        for tc in range(1, t + 1):
            N = int(f.readline())
            A = list(map(int, f.readline().split()))
            B = list(map(int, f.readline().split()))
            solve_case(tc, N, A, B, output_lines)

    with open(output_path, "w") as out:
        out.write("\n".join(output_lines))

    print("\n".join(output_lines))
    print("\nOutput written to:", output_path)


if __name__ == "__main__":
    main()
