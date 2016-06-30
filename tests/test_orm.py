
import peewee
from active_peewee.active_peewee import ActiveMeta
import unittest

db = peewee.SqliteDatabase('database.db')


class Person(peewee.Model):
    __metaclass__ = ActiveMeta

    name = peewee.CharField()
    age = peewee.IntegerField()

    class Meta:
        database = db


class TestActivePeeewee(unittest.TestCase):

    def setUp(self):
        db.create_tables([Person])

    def tearDown(self):
        db.drop_tables([Person])

    def test_parse(self):
        print 'asdauidhsaui', type(Person)
        query = Person.filter_by_name_and_age('felipe', 30)

        query_expected = {
            'name': {'operator': 'eq', 'value': 'felipe'},
            'age': {'operator': 'eq', 'value': 30},
            'agregate': 'and'
        }

        self.assertEqual(query_expected, query)
