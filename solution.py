import re
with open('text.txt', 'r', encoding='utf-8') as f:
    text = f.read()
def word_counts(text):
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    unique_words = len(set(words)) 
    return total_words, unique_words

def frequency_dict(text):
    words = re.findall(r'\b\w+\b', text.lower())
    total_words = len(words)
    if total_words == 0:
        return {}
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    freq_percent = {word: (count / total_words) * 100 for word, count in freq.items()}
    return freq_percent

def shortest_words(text):
    words = list(set(re.findall(r'\b\w+\b', text.lower())))
    if not words:
        return []
    min_len = min(len(w) for w in words)
    return [w for w in words if len(w) == min_len]

def longest_words(text):
    words = list(set(re.findall(r'\b\w+\b', text.lower())))
    if not words:
        return []
    max_len = max(len(w) for w in words)
    return [w for w in words if len(w) == max_len]

def letter_statistics(text):
    letters = re.findall(r'[а-яіїєґ]', text.lower())
    
    freq = {}
    for l in letters:
        freq[l] = freq.get(l, 0) + 1
        
    if not freq:
        return [], []
        
    max_count = max(freq.values())
    most_frequent = [l for l, count in freq.items() if count == max_count]
    
    return list(freq.keys()), most_frequent

print("--- Результати виконання завдання ---")

total, unique = word_counts(text)
print(f"1. Загальна кількість слів: {total}")
print(f"2. Кількість унікальних слів: {unique}")

print("\n3. Найкоротші слова у тексті:", shortest_words(text))
print("4. Найдовші слова у тексті:", longest_words(text))

letters_used, top_letters = letter_statistics(text)
print(f"\n5. Літера(и), що зустрічалася(ись) найчастіше: {top_letters}")

freq_d = frequency_dict(text)
print("\n6. Приклад частотного словника у % (перші 10 слів):")
items_list = list(freq_d.items()) 
for word, percent in items_list[:10]:  
  print(f"{word}: {percent}%")