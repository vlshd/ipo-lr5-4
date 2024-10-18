def words(sentence): # функция
    word = sentence.split()  # разделяем строку на слова
    reversed_words = ' '.join(reversed(word))  # разворачиваем порядок слов и объединяем их обратно
    return reversed_words
user_input = input("Введите строку: ") # ввод 
print("Результат:", words(user_input)) # вывод