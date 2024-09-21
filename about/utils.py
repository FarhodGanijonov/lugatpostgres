from .models import Addition

uzbek_words = ['man', 'bola', 'ota', 'ona', 'uy', 'ish', 'kitob', 'gul', 'olma', ]  # O'zbek lug'atidagi so'zlar


# So'z ildizini topadigan funksiya
def find_root_and_category(word):
    root_word = None
    max_length = 0

    # So'zning eng uzun ildizini topish
    for uzbek_word in uzbek_words:
        if word.startswith(uzbek_word) and len(uzbek_word) > max_length:
            root_word = uzbek_word
            max_length = len(uzbek_word)

    if not root_word:
        return None, None, None  # Agar ildiz topilmasa, hech narsa qaytarmaydix

    # So'z ildizidan keyingi qism qo'shimcha bo'lishi mumkin
    suffix = word[len(root_word):]

    # Qo'shimchani Addition modelidan qidirish
    try:
        # Faqat suffix qo'shimchalar ro'yxatida bo'lsa qo'shimcha deb qaraladi
        addition = Addition.objects.get(adition=suffix)
        category = addition.categ
    except Addition.DoesNotExist:
        # Agar suffix qo'shimcha bo'lmasa, hech qanday qo'shimcha qaytarmaydi
        return root_word, None, None

    return root_word, suffix, category  # Ildiz, qo'shimcha va kategoriya qaytariladi
