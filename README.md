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
$ wget https://raw.githubusercontent.com/django/django/master/django/contrib/admin/templates/admin/base.html templates/admin/base.html
```

4. Add left menu code to base.html
```
...
<link rel="stylesheet" type="text/css" href="{% block stylesheet %}{% static "admin/css/base.css" %}{% endblock %}">
<link rel="stylesheet" type="text/css" href="{% static "xadmin/app.css" %}">
...
    <!-- END Header -->

    <div class="xadmin_container">
        {% if request.path != "/admin/login/" and request.path != "/admin/logout/" %}
        {% include "xadmin/left_menu.html" %}
        {% endif %}
        <div class="xadmin_container_right">
...
    <!-- END Content -->
    </div>
...

```
