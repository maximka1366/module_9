def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        try:
            results[i.__name__] = i(int_list)
        except Exception as exc:

            results[i.__name__] = str(exc)
    return results

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))