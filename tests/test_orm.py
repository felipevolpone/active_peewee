
from active_peewee.active_peewee import ActivePeewee
import unittest


class TestActivePeeewee(unittest.TestCase):

    def test(self):
        self.assertEqual('bla', ActivePeewee.bla())
