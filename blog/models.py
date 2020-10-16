from django.db import models

# Create your models here.

GROUPS = (
    (0, "User"),
    (1, "Author"),
    (2, "Editor"),
    (3, "Admin"),
)

LIKE_TYPES = ((1, "Like"),
              (-1, "Dislike"),
              )


class Genre(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=10000, null=True)
    image = models.ImageField(upload_to='genre_images', null=True, blank=True)

    def __str__(self):
        return self.title


class Tag(models.Model):
    tag = models.CharField(max_length=120)

    def __str__(self):
        return f'#{self.tag}'


class User(models.Model):
    email = models.EmailField(max_length=120)
    username = models.CharField(max_length=120)
    image = models.ImageField(upload_to='user_images', null=True, blank=True)
    group = models.IntegerField(choices=GROUPS, default=0)

    def __str__(self):
        return f'{self.username}  [{self.group}]'


class Article(models.Model):
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    # updated_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=120)
    text = models.TextField(max_length=10000, null=True)
    # genres =
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.title}  [{self.author} / {self.genre}]'


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    text = models.CharField(max_length=1000)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    comment = models.ForeignKey('blog.Comment', related_name='comments_comment', null=True, blank=True,
                                on_delete=models.DO_NOTHING)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.user.username}]: {self.text}"


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
    type = models.IntegerField(choices=LIKE_TYPES, default=1)

    def __str__(self):
        return f"[{self.user.username}]: {self.type}"
