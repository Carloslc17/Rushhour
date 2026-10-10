class Node:

    def __init__(self, id, parent, action, state, cost, depth, heuristic):
        self.__id = id
        self.__parent = parent
        self.__action = action
        self.__state = state
        self.__cost = cost
        self.__depth = depth
        self.__heuristic = heuristic
        self.__value = None

    def get_id(self):
        return self.__id

    def get_parent(self):
        return self.__parent

    def get_action(self):
        return self.__action

    def get_state(self):
        return self.__state

    def get_cost(self):
        return self.__cost

    def get_depth(self):
        return self.__depth

    def get_heuristic(self):
        return self.__heuristic

    def get_value(self):
        return self.__value

    def set_value(self, value):
        self.__value = value

    def __str__(self):
        if not self.__parent:
            x = None
        else:
            x = self.__parent.get_id()

        
        return f"[{self.__id},{x},{self.__action},{self.__state},{self.__cost},{self.__depth},{self.__heuristic},{self.__value}]"

    
    