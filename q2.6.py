import ll as lib

linked = lib.ll([2, 1]);

def palindrome(ll):
    stack = [];
    curr = ll.root;

    while curr:
        stack.insert(0, curr.get_val());
        curr = curr.nxt;

    curr = ll.root;

    idx = 0;
    while curr:
        if curr.get_val() != stack[idx]:
            return False;
        else:
            curr = curr.nxt;
            idx += 1;
    return True;


print(palindrome(linked));
