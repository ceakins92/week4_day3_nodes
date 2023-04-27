# North, south, west, east problem:

def reduce_directions(alist):
    direction_stack = []
    opposite_directions = {
        'NORTH': 'SOUTH',
        'SOUTH': 'NORTH',
        'EAST': 'WEST',
        'WEST': 'EAST',
    }

    for direction in alist:
        if direction_stack and direction_stack[-1] == opposite_directions[direction]:
            direction_stack.pop()
        else:
            direction_stack.append(direction)
    return direction_stack


print(reduce_directions(
    ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
# determine if direction is next to direction of same value
# remove both


# HOMEWORK


# class Pokemon

#    self.evo_chain = ( < linked list > )

#    def evolve_pokemon(self):
#        LinkedList.add_node(evolved_pokemon)
