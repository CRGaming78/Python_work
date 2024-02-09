def print_truth_table(operator):
    print(f"Truth table for {operator}:")
    print(f"|  A |  B | {operator}  |")
    print("|----|----|----|")
    for a in range(2):
        for b in range(2):
          result = eval(f"{a} {operator} {b}")
          print(f"| {a:2d} | {b:2d} | {result:2d} |")
    print("\n")#for space btw :/
for operator in ['&', '|', '^']:#you can add more
  print_truth_table(operator)
