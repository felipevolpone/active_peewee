
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

    maxDiff = None

    def setUp(self):
        db.create_tables([Person])

    def tearDown(self):
        db.drop_tables([Person])

    def test_eq(self):
        query = Person.filter_by_name_and_age('felipe', 30)

        query_expected = {
            'name': {'operator': 'eq', 'value': 'felipe'},
            'age': {'operator': 'eq', 'value': 30},
            'agregate': 'and'
        }
        self.assertEqual(query_expected, query)

        # testing with just one field
        query = Person.filter_by_name('felipe')

        query_expected = {
            'name': {'operator': 'eq', 'value': 'felipe'}
        }

        self.assertEqual(query_expected, query)

    def test_gt(self):
        query = Person.filter_by_age_gt(30)

        query_expected = {'age': {'operator': 'gt', 'value': 30}}
        self.assertEqual(query_expected, query)

    def test_ge(self):
        query = Person.filter_by_age_ge(30)

        query_expected = {'age': {'operator': 'ge', 'value': 30}}
        self.assertEqual(query_expected, query)

    def test_lt(self):
        query = Person.filter_by_age_lt(30)

        query_expected = {'age': {'operator': 'lt', 'value': 30}}
        self.assertEqual(query_expected, query)

    def test_le(self):
        query = Person.filter_by_age_le(30)

        query_expected = {'age': {'operator': 'le', 'value': 30}}
        self.assertEqual(query_expected, query)

    def test_or(self):
        query = Person.filter_by_name_or_age('felipe', 30)

        query_expected = {
            'name': {'operator': 'eq', 'value': 'felipe'},
            'age': {'operator': 'eq', 'value': 30},
            'agregate': 'or'
        }

        self.assertEqual(query_expected, query)
