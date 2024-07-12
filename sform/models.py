from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class StudentManager(BaseUserManager):
    def create_user(self, s_code, password=None, **extra_fields):
        if not s_code:
            raise ValueError("The Student code must be set")
        student = self.model(s_code=s_code, **extra_fields)
        student.set_password(password)
        student.save(using=self._db)
        return student

    def create_superuser(self, s_code, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(s_code, password, **extra_fields)

class Student(AbstractBaseUser, PermissionsMixin):
    s_code = models.BigIntegerField(primary_key=True)
    s_name = models.CharField(max_length=200, blank=True, null=True)
    sex = models.CharField(max_length=1, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    edu_year = models.IntegerField(blank=True, null=True)
    f_m_name = models.CharField(max_length=200, blank=True, null=True)
    community = models.CharField(max_length=10, blank=True, null=True)
    p_income = models.IntegerField(blank=True, null=True)
    ca_name = models.CharField(max_length=200, blank=True, null=True)
    community_attach = models.BinaryField(blank=True, null=True)
    ia_name = models.CharField(max_length=200, blank=True, null=True)
    income_attach = models.BinaryField(blank=True, null=True)
    password = models.CharField(max_length=200)
    last_login = models.DateTimeField(blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='student_set',
        blank=True,
        help_text=('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        verbose_name=('groups')
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='student_permissions',
        blank=True,
        help_text=('Specific permissions for this user.'),
        verbose_name=('user permissions')
    )

    objects = StudentManager()

    USERNAME_FIELD = 's_code'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.s_code)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

    class Meta:
        managed = False
        db_table = 'student'

class Location(models.Model):
    s_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='s_code', primary_key=True)
    r_u = models.CharField(max_length=1, blank=True, null=True)
    addr1 = models.CharField(max_length=100, blank=True, null=True)
    addr2 = models.CharField(max_length=200, blank=True, null=True)
    p_name = models.CharField(max_length=100, blank=True, null=True)
    d_name = models.CharField(max_length=100, blank=True, null=True)
    states = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'location'

class College(models.Model):
    s_code = models.OneToOneField('Student', models.DO_NOTHING, db_column='s_code', primary_key=True)
    c_code = models.IntegerField(blank=True, null=True)
    c_name = models.CharField(max_length=200, blank=True, null=True)
    l_name = models.CharField(max_length=100,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'college'

class Bank(models.Model):
    acc_no = models.BigIntegerField(primary_key=True)
    s_code = models.ForeignKey('Student', models.DO_NOTHING, db_column='s_code', blank=True, null=True)
    ifsc = models.CharField(max_length=11, blank=True, null=True)
    b_name = models.CharField(max_length=200, blank=True, null=True)
    b_loc = models.CharField(max_length=100, blank=True, null=True)
    b_addr = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bank'