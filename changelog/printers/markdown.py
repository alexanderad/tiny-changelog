from .printer import Printer


class MarkdownPrinter(Printer):
    def header(self):
        return '# Change Log'

    def footer(self):
        return ''

    def break_line(self):
        return '  '

    def tag_line(self, tag):
        return u'# [{name}]({url})'.format(**tag.as_dict)

    def pr_line(self, pr):
        return u'* [\#{number}]({url}) {title} (@{author})'.format(
            **pr.as_dict)

    def lines(self):
        yield self.header()
        yield self.break_line()

        for tag, pull_requests in self.iteritems():
            yield self.tag_line(tag)
            for pr in pull_requests:
                yield self.pr_line(pr)
            yield self.break_line()

        yield self.footer()

    def pretty_print(self):
        for line in self.lines():
            print(line)
