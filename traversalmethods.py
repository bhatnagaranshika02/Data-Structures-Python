def in_order(self):
    if self.left_child:
        self.left_child.in_order()
    print(self.value)
    if self.right_child:
        self.right_child.in_order()


def post_order(self):
    if self.left():
        return self.left.post_order()
    if self.right:
        return self.right.post_order()
    print(self.data)


def pre_order(self):
    print(self.data)

    if self.left():
        return self.left.post_order()
    if self.right:
        return self.right.post_order()
    
