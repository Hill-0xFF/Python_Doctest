def fizzbuzz(numbers: int) -> list[str]:
    results: list[str] = []
    for num in numbers:
        if num % 15 == 0:
            results.append('fizzbuzz')
        
        elif num % 3 == 0:
            results.append('fizz')
            
        else:
            results.append(num)
    return results