#/usr/bin/env python
def usage():
    print("Usage: {} <output_file> <input_file>",stderr)

class Parser(object):
    def __init__(self, input_filename, output_filename):
        self.input_file = open(input_filename)
        self.output_file = open(output_filename, "w")
    
    def parse(self):
        self.input_file.flush()
        self.output_file.flush()
        current_char = None;
        while True
            c = self.input_file.read(1)
            if not c:
                break
