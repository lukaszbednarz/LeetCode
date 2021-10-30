def fizzBuzz(n: int) -> List[str]:
    rem3 = n % 3
    rem5 = n % 5

    if rem3 == 0 and rem5 == 0:
        return "FizzBuzz"
    elif rem3 == 0:
        return "Fizz"
    elif rem5 == 0:
        return "Buzz"
    else:
        return n
