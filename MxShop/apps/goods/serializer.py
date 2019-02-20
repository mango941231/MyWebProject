from rest_framework import serializers
from .models import Goods,GoodsCategory

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodsCategory
        fields="__all__"#将整个表的所有字段都序列化

class GoodsSerializer(serializers.ModelSerializer):
    category = CategoryModelSerializer()
    class Meta:
        model = Goods
        fields = "__all__"


'''
class GoodsSerializer(serializers.Serializer):#Serializer方式序列化
    name = serializers.CharField(required=True,max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()
    # 用于post
    def create(self, validated_data):
        return Goods.objects.create(**validated_data)


class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=GoodsCategory
        fields="__all__"#将整个表的所有字段都序列化


class GoodsModelSerializer(serializers.ModelSerializer):#ModelSerializer方式序列化
    category=CategoryModelSerializer()#外键信息嵌入
    class Meta:
        model=Goods
        # fields="__all__"#将整个表的所有字段都序列化
        fields=('name','goods_front_image','category')#指定序列化某些字段
'''