input_path = r"C:\Users\user\Desktop\meta_hacker_cup_2025\round_1_part_2\snake_scales_chapter_2_validation_input\snake_scales_chapter_2_validation_input.txt"
output_path = r"C:\Users\user\Desktop\meta_hacker_cup_2025\round_1_part_2\output.txt"

with open(input_path) as f:
    t = int(f.readline())
    result = []

    for case in range(1, t + 1):
        n = int(f.readline())
        A = list(map(int, f.readline().split()))
        ladder = A[0]  # ladder to reach first platform
        for i in range(1, n):
            if A[i] > A[i-1]:
                ladder = max(ladder, A[i] - A[i-1])
        result.append(f"Case #{case}: {ladder}")

with open(output_path, "w") as f:
    f.write("\n".join(result) + "\n")

print("\n".join(result))
