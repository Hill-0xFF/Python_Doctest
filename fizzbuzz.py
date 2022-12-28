def fizzbuzz(numbers: int) -> list[str]:
    results: list[str] = []
    for num in numbers:
        if num % 15 == 0:
            results.append('fizzbuzz')
        
        elif num % 3 == 0:
            results.append('fizz')

        elif num % 5 == 0:
            results.append('buzz')
        
        else:
            results.append(num)
    return results