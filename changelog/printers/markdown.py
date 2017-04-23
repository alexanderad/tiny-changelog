from .printer import Printer


class MarkdownPrinter(Printer):
    def header(self):
        return '# Change Log'

    def footer(self):
        return ''

    def break_line(self):
        return '  '

    def lines(self):
        yield self.header()
        yield self.break_line()
        for tag, pull_requests in self.iteritems():
            yield u'# [{}]({}) ({})  '.format(tag.name, tag.url, tag.pretty_at)
            for pr in pull_requests:
                yield u'* [\#{}]({}) {} - @{}'.format(
                    pr.number, pr.url, pr.title, pr.author
                )
            yield self.break_line()

        yield self.footer()

    def pretty_print(self):
        for line in self.lines():
            print(line)
