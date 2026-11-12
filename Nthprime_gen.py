def is_prime(n):
    """ამოწმებს, არის თუ არა რიცხვი მარტივი"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_generator(limit):
    """გენერატორი, რომელიც თანმიმდევრობით აბრუნებს მარტივ რიცხვებს მითითებულ რაოდენობამდე"""
    current = 2
    count = 0
    while count < limit:
        if is_prime(current):
            yield current
            count += 1
        current += 1