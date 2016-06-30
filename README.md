# active_peewee
Improving the Peewee ORM with ideas from Rails ActiveRecord

Dynamic methods to filter result in database. Such like:
```python
User.filter_by_name_and_age('samuel l jackson', 100)
```

Instead of:
```python
User.select().where(and_(User.name == 'samuel l jackson', User.age == 100))
```
