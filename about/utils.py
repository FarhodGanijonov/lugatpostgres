
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from .models import Text, nlp


def search_texts(query):
    # Lemmatizatsiya qilingan qidiruv so'zini yaratish
    doc = nlp(query)
    lemmatized_query = " ".join([token.lemma_ for token in doc if token.lemma_])

    # Agar qidiruv so'zi bo'sh bo'lsa, hech qanday natija qaytarmang
    if not lemmatized_query.strip():
        return []

    # Izlash vektorini yaratish
    search_vector = SearchVector('lemmatized_text')

    # Izlash so'rovini yaratish
    search_query = SearchQuery(lemmatized_query)

    # Qidiruvni amalga oshirish
    results = Text.objects.annotate(
        rank=SearchRank(search_vector, search_query)
    ).filter(
        rank__gt=0.1
    ).order_by('-rank')

    return results
