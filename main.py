def is_palindrome(s):
    return s == s[::-1]

# Пример использования
input_str = input("Введите строку: ")
result = is_palindrome(input_str)
print(result)
