from django.db import models

class Groups(models.Model):
    Id = models.AutoField(primary_key=True)
    GroupGuid = models.UUIDField()
    Name = models.CharField(max_length=100)
    Description = models.CharField(max_length=600, blank=True)
    Link = models.CharField(max_length=200, blank=True)
    class Meta:
        db_table = "Groups"

class UserRoles(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    class Meta:
        db_table = "UserRoles"

class Users(models.Model):
    Id = models.AutoField(primary_key=True)
    UserGuid = models.UUIDField()
    Name = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    DateOfBirth = models.DateField()
    Login = models.CharField(max_length=100)
    PasswordHash = models.CharField(max_length=500)
    RoleId = models.ForeignKey(UserRoles, on_delete=models.DO_NOTHING, db_column='RoleId')
    class Meta:
        db_table = "Users"

class UserGroups(models.Model):
    Id = models.AutoField(primary_key=True)
    UserId = models.ForeignKey(Users, on_delete=models.DO_NOTHING, db_column='UserId')
    GroupId = models.ForeignKey(Groups, on_delete=models.DO_NOTHING, db_column='GroupId')
    class Meta:
        db_table = "UserGroups"

