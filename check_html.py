from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.mismatches = []
        self.line_offset = 1

    def handle_starttag(self, tag, attrs):
        if tag in ['div', 'body', 'html']:
            self.tags.append((tag, self.getpos()))

    def handle_endtag(self, tag):
        if tag in ['div', 'body', 'html']:
            if not self.tags:
                self.mismatches.append(f"Unexpected end tag <{tag}> at line {self.getpos()[0]}")
                return
            
            last_tag, pos = self.tags.pop()
            if last_tag != tag:
                self.mismatches.append(f"Mismatched end tag <{tag}> at line {self.getpos()[0]}. Expected <{last_tag}> from line {pos[0]}")
                self.tags.append((last_tag, pos))

def check_file(filepath):
    parser = MyHTMLParser()
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            parser.feed(f.read())
        print(f"--- {filepath} ---")
        for m in parser.mismatches:
            print(m)
        if parser.tags:
            print("Unclosed tags:", parser.tags)
    except Exception as e:
        print(e)

check_file('rekomendasi.html')
check_file('sumber.html')
check_file('larikelas6.html')
