class HashTable:
    table = [];

    def hash(self, elem):
        count = 0;
        for c in elem:
            count += ord(c);
        return count % len(self.table);

    def insert(self, elem):
        self.table[hash(elem) % len(self.table)].append(elem);

    def init_table(self):
        for i in range(10):
            self.table.append([]);

    def display(self):
        for l in self.table:
            count = len(l);
            print(str(count) + ' ', end=' | ');
        print();


h = HashTable();
h.init_table();
h.insert('Hi');
h.insert('Hi');
h.insert('wow');
h.insert('Bye');
h.display();
