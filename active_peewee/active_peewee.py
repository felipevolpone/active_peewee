import peewee

# TODO
# [] arrumar readme (colocar exemplos; falar do eq; falar do agregador)
# [] gerar de fato a query no peewee
# [] publicar no PyPI


class __ParseMeta(type):

    def __getattr__(self, method_name):
        """here is where the magic happens."""

        def inner(*args, **kwargs):
            return self._parse(method_name, *args)

        inner.__name__ = method_name
        return inner

    def _parse(self, method_name, *args):
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


class ActiveMeta(__ParseMeta, peewee.BaseModel):
    pass
