from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product, Category, Review
from product.serializers import ProductSerializer, CategorySerializer, ReviewSerializer
from django.db.models import Avg


@api_view(['GET'])
def products_list_api_view(request):
    products = Product.objects.all()
    products_json = ProductSerializer(products, many=True).data

    return Response(data=products_json)


@api_view(['GET'])
def product_detail_api_view(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        return Response(data={'message': 'Product not found!'},
                        status=404)
    product_json = ProductSerializer(product, many=False).data
    return Response(data=product_json)


@api_view(['GET'])
def category_list_api_view(request):
    categories = Category.objects.all()
    categories_json = CategorySerializer(categories, many=True).data

    return Response(data=categories_json)


@api_view(['GET'])
def category_detail_api_view(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist:
        return Response(data={'message': 'Category not found!'},
                        status=404)
    category_json = CategorySerializer(category, many=False).data
    return Response(data=category_json)


@api_view(['GET'])
def review_list_api_view(request):
    reviews = Review.objects.all()
    reviews_json = ReviewSerializer(reviews, many=True).data

    return Response(data=reviews_json)


@api_view(['GET'])
def review_detail_api_view(request, review_id):
    try:
        review = Review.objects.get(id=review_id)
    except Review.DoesNotExist:
        return Response(data={'message': 'Review not found!'},
                        status=404)
    review_json = ReviewSerializer(review, many=False).data
    return Response(data=review_json)


@api_view(['GET'])
def product_reviews_api_view(request):
    reviews = Review.objects.all()
    reviews_json = ReviewSerializer(reviews, many=True).data

    return Response(data=reviews_json)


@api_view(['GET'])
def average_rating_api_view(request):
    average_rating = Review.objects.aggregate(avg_rating=Avg('stars'))
    return Response({'avg_rating': average_rating['avg_rating']})
