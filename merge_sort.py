def merge_sort(items):
    comparisons = 0
    def merge(left, right):
        nonlocal comparisons
        
        sorted_list = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            try:
                comparisons += 1
                if left[i] < right[j]:
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            except ValueError as e:
                raise ValueError(f"Merge Sort failed after {comparisons} comparisons due to incomparable items. {e}")
        
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        
        return sorted_list, comparisons
    
    if len(items) <= 1:
        return items, comparisons
    
    mid = len(items) // 2
    left, sub_comps_l = merge_sort(items[:mid])
    right, sub_comps_r = merge_sort(items[mid:])
    comparisons += sub_comps_l + sub_comps_r
    
    return merge(left, right)
