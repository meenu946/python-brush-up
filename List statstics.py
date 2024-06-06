def analyze_list(numbers):
    min_value = min(numbers)
    max_value = max(numbers)
    average_value = sum(numbers) / len(numbers)
    
    stats = {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }
    
    return stats

numbers = [10, 20, 30, 40, 50]
stats = analyze_list(numbers)
print(f"List statistics: {stats}")