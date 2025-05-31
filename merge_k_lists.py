def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        # Порівнюємо елементи з обох списків і додаємо менший до результату
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            # Якщо елемент з правого списку менший, додаємо його
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])
    return merged


def merge_k_lists(lists: list[list[int]]) -> list[int]:
    """Зливає k відсортованих списків у один відсортований список."""
    if not lists:
        return []

    while len(lists) > 1:
        merged_lists = []

        for i in range(0, len(lists), 2):
            # Зливаємо кожну пару списків
            if i + 1 < len(lists):
                merged = merge(lists[i], lists[i + 1])
                merged_lists.append(merged)
            else:
                # Якщо непарна кількість — додаємо останній список без злиття
                merged_lists.append(lists[i])

        lists = merged_lists

    return lists[0]

lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
