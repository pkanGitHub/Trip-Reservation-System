from re import I


class TotalSales:
    def __init__(self, sales_data):
        self.total_sales = 0
        self.sales_data = sales_data
    def getseat_price(self, row, seat):
        cost_matrix = self.get_cost_matrix()
        return cost_matrix[row][seat]
    ##method to get the total sales
    def get_total_prices(self):
        ##open the text file
        with open(self.sales_data, 'r') as f:
            for line in f:
                line = line.strip()
                line = line.split(',')
                current_row = int(line[1])
                current_seat = int(line[2])
                current_price = self.getseat_price(current_row, current_seat)
                self.total_sales += current_price
        return self.total_sales

    def get_cost_matrix(self):
        cost_matrix = [[100, 75, 50, 100] for row in range(12)]
        return cost_matrix
sales = TotalSales('reservations.txt')
print(sales.get_total_prices())
