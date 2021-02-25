from django.db.models import Count


def prolific_user(Post, User):
    """
    Return the most prolific writer in my site .
    Use this func in my index view.

    """
    user = Post.objects.filter(confirm=True, active=True).values("user").annotate(post_count=Count("id"))[:3]
    most_prolific_user = [{"user": User.objects.get(pk=i["user"]), "count_post": i["post_count"]} for i in user]
    return most_prolific_user


def popular_user(User):
    """
    Return the most popular writer in my site .
    Use this func in my index view.

    """
    wirters = [user for user in User.objects.all() if user.has_perm('blog.add_post')]
    popular_user = [
        {"user": wirter, "like": sum([post.like.count() for post in wirter.post.all() if post.confirm == True])}
        for wirter in wirters]
    popular_user = list(sorted(popular_user, key=lambda item: -item["like"]))[:3]
    return popular_user
