from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Product
from .serializers import ProductSerializer

#  All products (you already have this)
class ProductList(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


#  Category filter
class ProductByCategory(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category)


#  Top rated
class TopRatedProducts(ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.filter(rating__gte=4)


#  Single product
class ProductDetail(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer