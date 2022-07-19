class FIFO:

    def __init__(self):
        self.mas = []

    def append_element(self, element):
        self.mas.append(element)

    def get_element(self):
        if self.mas:
            out = self.mas.pop(0)
        else:
            out = None
        print(out)
        return out

    def print_list(self):
        print (self.mas)



class QUEUE:

    def __init__(self):
        self.mas = []

    def append_element(self, element):
        self.mas.append(element)

    def get_element(self):
        if self.mas:
            out = self.mas.pop(0)
        else:
            out = None
        print(out)
        return out

    def print_list(self):
        print (self.mas)

    def is_empty(self):
        return (len(self.mas)==0)

    def tail(self):
        if len(self.mas) != 0:
            return self.mas[0]

    def front(self):
        if len(self.mas)!=0:
            return self.mas[-1]



