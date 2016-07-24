import peewee

# TODO
# [] publish at PyPI


class ActiveMeta(peewee.Model):

    def __getattr__(self, method_name):
        """here is where the magic happens."""

        def inner(*args, **kwargs):
            json_query = self._parse(method_name, *args)
            return self._to_query(json_query)

        inner.__name__ = method_name
        return inner

    @classmethod
    def _parse(cls, method_name, *args):
        fields_to_parse = method_name.replace('by_', '').split('_')

        operators = ['gt', 'ge', 'lt', 'le', 'df']
        agregators = ['and', 'or']

        query = {}
        last_word = None
        args_ordered = []

        for word in fields_to_parse:
            if word not in operators and word not in agregators:  # its a field name
                query[word] = {}
                last_word = word
                args_ordered.append(word)
                continue

            if word in operators:
                query[last_word]['operator'] = word

            if word in agregators:
                query['agregate'] = word
                last_word = word

        for idx, argument_value in enumerate(args):
            query[args_ordered[idx]]['value'] = argument_value

        for field, options in query.iteritems():
            if 'operator' not in options and field != 'agregate':
                query[field]['operator'] = 'eq'

        return query

    @classmethod
    def _to_query(cls, json_query):
        filter = cls.select()

        for field, details in json_query.keys():

            if field == 'agregate':
                continue

            if details['operator'] == 'eq':
                filter = filter.where(field == details['value'])

            elif details['operator'] == 'ge':
                filter = filter.where(field >= details['value'])

            elif details['operator'] == 'gt':
                filter = filter.where(field > details['value'])

            elif details['operator'] == 'lt':
                filter = filter.where(field < details['value'])

            elif details['operator'] == 'le':
                filter = filter.where(field <= details['value'])

            elif details['operator'] == 'df':
                filter = filter.where(field != details['value'])

        return filter
