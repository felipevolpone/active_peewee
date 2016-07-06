# active_peewee

[![Build Status](https://travis-ci.org/felipevolpone/active_peewee.svg?branch=master)](https://travis-ci.org/felipevolpone/active_peewee)
[![Coverage Status](https://coveralls.io/repos/github/felipevolpone/active_peewee/badge.svg?branch=master)](https://coveralls.io/github/felipevolpone/active_peewee?branch=master)
[![Code Climate](https://codeclimate.com/github/felipevolpone/active_peewee/badges/gpa.svg)](https://codeclimate.com/github/felipevolpone/active_peewee)


Improving the [Peewee ORM](https://github.com/coleifer/peewee/) with ideas from Rails ActiveRecord.

With Active Peewee you can use dynamic methods to filter result in database. Such like:
```python
User.filter_by_name_and_age('samuel l jackson', 100)
```

Instead of:
```python
User.select().where(and_(User.name == 'samuel l jackson', User.age == 100))
```

### Using ActivePeewee

Declare a Peewee model changing the metaclass of the class:
```python
from peewee import *
from active_peewee.active_peewee import ActiveMeta

class User(MySQLModel):
    __metaclass__ = ActiveMeta
    name = CharField(max_length=140, null=True)
    email = CharField(max_length=140, null=True)
    age = IntegerField()

    class Meta:
        database = db
```

It's done! Now you can use the activepeewee syntax to do simple queries:


**and using equal operator**
```python
User.by_name_and_age('samuel l jackson', 99)
```

**or using equal operator**
```python
User.by_name_or_email('samuel l jackson', 'l@jackson.com')
```

**greather than operator**
```python
User.by_age_gt(40)
```

**greather equal operator**
```python
User.by_age_ge(40)
```

**less than operator**
```python
User.by_age_lt(40)
```

**less equal operator**
```python
User.by_age_le(40)
``''
