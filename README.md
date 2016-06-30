# active_peewee

[![Build Status](https://travis-ci.org/felipevolpone/active_peewee.svg?branch=master)](https://travis-ci.org/felipevolpone/active_peewee)
[![Coverage Status](https://coveralls.io/repos/felipevolpone/active_peewee/badge.svg?branch=master&service=github)](https://coveralls.io/github/felipevolpone/active_peewee?branch=master)
[![Code Climate](https://codeclimate.com/github/felipevolpone/active_peewee/badges/gpa.svg)](https://codeclimate.com/github/felipevolpone/active_peewee)


Improving the Peewee ORM with ideas from Rails ActiveRecord

Dynamic methods to filter result in database. Such like:
```python
User.filter_by_name_and_age('samuel l jackson', 100)
```

Instead of:
```python
User.select().where(and_(User.name == 'samuel l jackson', User.age == 100))
```
