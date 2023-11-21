from django.shortcuts import render

# Create your views here.
# from .utils import build_recommender, get_recommendations
# from .models import Rating

def index(request):
    return render(request, 'index2.html')

def recommend(request):
    if request.method == 'POST':
        company = int(request.POST.get('company'))
        # model = build_recommender()
        # items_to_recommend = get_recommendations(user_id, model)
        # recommended_items = Rating.objects.filter(item__in=items_to_recommend).values_list('item', flat=True).distinct()
        recommended_items = ['new', 'very_new']

        return render(request, 'recommendation.html', {'company': company, 'recommended_items': recommended_items})

    return render(request, 'index.html')