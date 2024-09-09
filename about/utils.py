import spacy
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Text

# spaCy modelini yuklash
nlp = spacy.load("en_core_web_sm")

def lemmatize_text(text):
    doc = nlp(text)
    lemmatized_text = " ".join([token.lemma_ for token in doc])
    return lemmatized_text

def search_texts(query):
    # Lemmatizatsiya
    lemmatized_query = lemmatize_text(query)

    # Izlash vektorini yaratish
    search_vector = SearchVector('text')

    # Izlash so'rovini yaratish
    search_query = SearchQuery(lemmatized_query)

    # Matnlarni izlash va ularni natijalarda qaytarish
    results = Text.objects.annotate(
        rank=SearchRank(search_vector, search_query)
    ).filter(
        rank__gt=0.1  # 0.1 - bu izlash natijalarining darajasini belgilaydi, kerak bo'lsa o'zgartiring
    ).order_by('-rank')

    return results
