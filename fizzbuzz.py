def fizzbuzz(numbers: int) -> list[str]:
    results: list[str] = []
    for num in numbers:
        if num % 15 == 0:
            results.append('fizzbuzz')
        else:
            results.append(num)
    return results