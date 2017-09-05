def flatten(nested_list): ## type hinting here can be interesting
    def helper():
        for item in nested_list:
            if isinstance(item, (list, tuple)):
                for subitem in flatten(item):
                    yield subitem
            elif item is not None:
                yield item
    return list(helper())
