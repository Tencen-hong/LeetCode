class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        tables = {}
        food_kinds = set()
        res = []
        for (customerName, tableNumber, foodItem) in orders:
            tableNumber = int(tableNumber)
            food_kinds.add(foodItem)
            tables[tableNumber] = tables.get(tableNumber, {})
            tables[tableNumber][foodItem] = tables[tableNumber].get(
                foodItem, 0) + 1

        #print(['Table'] + food_kinds)
        food_kinds = sorted(list(food_kinds))
        res.append(['Table'] + food_kinds)
        tableNo = sorted(list(tables.keys()))

        for tableNumber in tableNo:
            data = [tableNumber]
            for food in food_kinds:
                data.append(tables[tableNumber].get(food, 0))
            # print(data)
            data = list(map(str, data))
            res.append(data)

        return res
