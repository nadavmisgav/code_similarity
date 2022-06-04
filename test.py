from embed import embed_from_file, sim

ya = embed_from_file("python_a.py")
yb = embed_from_file("python_b.py")
yc = embed_from_file("python_c.py")
yd = embed_from_file("python_d.py")

print("Python:")
print(f"\tCompare two implementation of merge sorts: {sim(ya, yb):.2f}")
print(f"\tCompare merge sort to fibonacci:           {sim(ya, yc):.2f}")
print(f"\tCompare merge and bubble sort:             {sim(ya, yd):.2f}")

ya = embed_from_file("c_a.c")
yb = embed_from_file("c_b.c")
yc = embed_from_file("c_c.c")
yd = embed_from_file("c_d.c")

print("C:")
print(f"\tCompare two implementation of merge sorts: {sim(ya, yb):.2f}")
print(f"\tCompare merge sort to fibonacci:           {sim(ya, yc):.2f}")
print(f"\tCompare merge and bubble sort:             {sim(ya, yd):.2f}")
