import csv


class dataset:
    def __init__(self):
        self.vals = list()
    def __getitem__(self, ind):
        return self.vals[ind]
    def __len__(self):
        return len(self.vals)
    def append_data(self, val):
        self.vals.append(val)
    def load_data(self, list_of_datapoints):
        for val in list_of_datapoints:
            self.append_data(val)


class txt_dataset(dataset):
    def __init__(self, fname, splitter):
        super(txt_dataset, self).__init__()
        self.file = open(fname)
        for self.line in self.file:
            self.append_data(tuple(self.line.split(splitter)))

class csv_dataset(dataset):
    def __init__(self, fname, splitter):
        super(csv_dataset, self).__init__()
        with open(fname) as self.file:
            self.reader = csv.reader(self.file, delimiter=splitter)
            for row in self.reader:
                self.append_data(tuple(row))

