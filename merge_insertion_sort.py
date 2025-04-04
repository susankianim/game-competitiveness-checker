def jacobsthal_sequence(n):
    seq = [1, 3]
    while seq[-1] < n:
        seq.append(seq[-2] * 2 + seq[-1])
    return seq

def build_insertion_order(n):
    if n <= 0:
        return []
    j_seq = jacobsthal_sequence(n)
    order = []
    prev = 0
    for j in j_seq:
        order.extend(range(prev + 1, j + 1)[::-1])
        prev = j
    # Subtract 1 from all to get 0-based indices
    return [x - 1 for x in order if x - 1 < n]

def merge_insertion_sort(arr):
    comparisons = 0

    def binary_insert(arr, val, end):
        nonlocal comparisons
        left, right = 0, end
        while left < right:
            mid = (left + right) // 2
            comparisons += 1
            try:
                if arr[mid] < val:
                    left = mid + 1
                else:
                    right = mid
            except ValueError as e:
                raise ValueError(f"Merge Insertion Sort failed after {comparisons} comparisons due to incomparable items. {e}")
        arr.insert(left, val)

    if len(arr) <= 1:
        return arr, comparisons

    # Create sorted [a, b] pairs
    pairs = []
    unpaired = None
    for i in range(0, len(arr) - 1, 2):
        comparisons += 1
        a, b = arr[i], arr[i+1]
        try:
            if b < a:
                pairs.append([a, b])
            else:
                pairs.append([b, a])
        except ValueError as e:
                raise ValueError(f"Merge Insertion Sort failed after {comparisons} comparisons due to incomparable items. {e}")
    if len(arr) % 2 == 1:
        unpaired = arr[-1]

    # Recursively sort pairs (Python compares [a, b]s naturally)
    if len(pairs) > 1:
        pairs, sub_comps = merge_insertion_sort(pairs)
        comparisons += sub_comps

    main_chain = [p[0] for p in pairs]

    # Collect 'b' elements
    b_elements = [p[1] for p in pairs]
    if unpaired is not None:
        b_elements.append(unpaired)

    # Jacobsthal insertion order
    insertion_order = build_insertion_order(len(b_elements))

    # Insert 'b' elements into main chain
    for b_idx in insertion_order:
        b = b_elements[b_idx]
        if b_idx < len(pairs):
            limit = main_chain.index(pairs[b_idx][0])
        else:
            limit = len(main_chain)  # Unpaired element goes to end
        binary_insert(main_chain, b, limit)

    return main_chain, comparisons

