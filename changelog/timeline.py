import sortedcontainers


class Timeline(object):
    def __init__(self):
        self.events = sortedcontainers.SortedListWithKey(key=lambda e: e.at)

    def add(self, event):
        self.events.add(event)


class Event(object):
    DATETIME_FORMAT = '%Y-%m-%d'

    def __init__(self, at):
        self.at = at

    @property
    def pretty_at(self):
        if not self.at:
            return 'N/A'
        return self.at.strftime(self.DATETIME_FORMAT)


class Tag(Event):
    def __init__(self, name, url=None, at=None):
        self.name = name
        self.url = url
        super(Tag, self).__init__(at)

    def __repr__(self):
        return 'Tag {} ({})'.format(self.name, self.pretty_at)

UnreleasedTag = Tag('Unreleased')


class PullRequest(Event):
    def __init__(self, number, author, title, url, at):
        self.number = number
        self.author = author
        self.title = title
        self.url = url
        super(PullRequest, self).__init__(at)

    def __repr__(self):
        return 'PR #{}: ({})'.format(self.number, self.title, self.pretty_at)
