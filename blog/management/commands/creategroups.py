from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

perm_1 = ["add_comments", "view_comments", "view_post"]
perm_2 = ["add_post", "view_post", "change_post", "add_tags", "change_tags", "view_tags", "active_post"]
perm_3 = ["active_comment", "confirm_post", "confirm_comment", "delete_comments", "delete_tags"]

groups = {1: "کاربران ساده", 2: "نویسندگان", 3: "ویراستاران"}


# craete groups and set base permissions
# def create_group_part_1():
#     perm_part_1 = [Permission.objects.filter(codename=perm)[0] for perm in perm_1]
#     for group in groups:
#         new_group, created = Group.objects.get_or_create(name=groups[group])
#         new_group.permissions.set(perm_part_1)


# set permissions of wirters and editors
def create_group():
    perm_part_1=[Permission.objects.filter(codename=perm)[0] for perm in perm_1]
    perm_part_2 = [Permission.objects.filter(codename=perm)[0] for perm in perm_2]
    perm_part_3 = [Permission.objects.filter(codename=perm)[0] for perm in perm_3]
    simple_user,wirter, editor = groups[1],groups[2], groups[3]
    simple_user=Group.objects.create(name=simple_user)
    wirter = Group.objects.create(name=wirter)
    editor = Group.objects.create(name=editor)
    simple_user.permissions.set(perm_part_1)
    wirter.permissions.set(perm_part_1+perm_part_2)
    editor.permissions.set(perm_part_1+perm_part_2 + perm_part_3)


class Command(BaseCommand):
    help = 'Create groups for this system'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            create_group()
        except Exception as ex:
            self.stdout.write(self.style.SUCCESS(ex))

        self.stdout.write(self.style.SUCCESS("Group were created"))
