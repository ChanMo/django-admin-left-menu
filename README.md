# Django Admin Left Menu

A left menu for django admin

## Tutorials

1. Install
```
$ pip install django-admin-left-menu
```

2. Add xadmin to Installed Apps
```python
INSTALLED_APPS = [
...
xadmin,
...
]
```

3. Copy base_site.html of django admin
```
$ mkdir templates/admin -p
$ copy /path/to/django/admin/templates/admin/base_site.html templates/admin
```

4. Add left menu code
```
$ vim templates/admin/base_site.html
```
