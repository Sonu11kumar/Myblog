from rest_framework.serializers import(
            ModelSerializer,
            HyperlinkedIdentityField,
            SerializerMethodField)

from ..models import Post


class PostSerializer(ModelSerializer):
    user = SerializerMethodField()
    image = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
                  "user",
                  "id",
                  "title",
                  "image",
                  "description",
                  "draft",
                  "publish",
                  "slug"
                  ]

    def get_user(self, obj):
          try:
              user = str(obj.user.username)
          except:
              user = None
          return user

    def get_image(self, obj):
          try:
              image = obj.image.path
          except:
              image = None
          return image


class PostListAPIView(ModelSerializer):


    class Meta:
        model = Post
        fields = [
                  "url",
                  "id",
                  "title",
                  "image",
                  "description",
                  "draft",
                  "publish",
                  "slug"
                  ]



