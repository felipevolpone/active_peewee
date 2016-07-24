
import peewee
from active_peewee.active_peewee import ActiveMeta
import unittest


db = peewee.SqliteDatabase('database.db')


class User(ActiveMeta):

    name = peewee.CharField()
    age = peewee.IntegerField()

    class Meta:
        database = db


class TestORM(unittest.TestCase):

    maxDiff = None

    def setUp(self):
        db.create_tables([User])

        for name, age in [('felipe', 10), ('john', 20), ('max', 30)]:
            User(name=name, age=10).save()

    def tearDown(self):
        db.drop_tables([User])

    def test_get(self):
        result = User.by_name_and_age('felipe', 10)
        user = result[0]
        self.assertEqual(user.name, 'felipe')
        self.assertEqual(user.age, 10)
