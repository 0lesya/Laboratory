class Shannon_fano:
    __encode_list = []

    def get_encode_list(self):
        return self.__encode_list

    encode_list = property(get_encode_list)

    def encript(self, weights, str):
        if len(weights) == 1:
            self.encode_list.append(str)
            return
        middle = self.__count_separation_index(weights)
        self.encript(self.__create_subset(weights, 0, middle), str + "1")
        self.encript(self.__create_subset(weights, middle, len(weights)), str + "0")

    def __count_separation_index(self, weights):
        l = 0
        r = len(weights)
        m = int((l + r) / 2)
        while True:
            left_sum = self.__count_sum(self.__create_subset(weights, l, m))
            right_sum = self.__count_sum(self.__create_subset(weights, m, len(weights)))
            if left_sum <= right_sum or m == 1:
                return m
            else:
                r = m
                m -= 1

    def __create_subset(self, set, start_index, last_index):
        subset = []
        for i in range(start_index, len(set)):
            if i == last_index:
                break
            subset.append(set[i])
        return subset

    def __count_sum(self, list):
        sum_elements = 0
        for element in list:
            sum_elements += element
        return sum_elements
