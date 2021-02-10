from django.db.models import Count


def prolific_user(Post, User):
    user = Post.objects.values("user").annotate(post_count=Count("id"))[:3]
    most_prolific_user = [{"user": User.objects.get(pk=i["user"]), "count_post": i["post_count"]} for i in user]
    return most_prolific_user


def popular_user(User):
    wirters = [user for user in User.objects.all() if user.has_perm('blog.add_post')]
    popular_user = [{"user": wirter, "like": sum([post.like.count() for post in wirter.user_post.all()])}
                    for wirter in wirters]
    popular_user = list(sorted(popular_user, key=lambda item: -item["like"]))[:3]
    return popular_user
