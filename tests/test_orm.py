
import peewee
from active_peewee.active_peewee import ActiveMeta
import unittest


db = peewee.SqliteDatabase('database.db')


class User(peewee.Model):
    __metaclass__ = ActiveMeta

    name = peewee.CharField()
    age = peewee.IntegerField()

    class Meta:
        database = db


class TestORM(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        db.create_tables([User])

    def tearDown(self):
        db.drop_tables([User])

    def test_get(self):
        self.assertEqual(2, 2)
