doc = {"a":2,"b":4}
out = []


def navigate(struct, ignore_red):
    if str(type(struct)) == '<class \'dict\'>':
        if "red" not in struct.values() or ignore_red:
            for key in struct:
                navigate(struct[key], ignore_red)
    elif str(type(struct)) == '<class \'list\'>':
        for item in struct:
            navigate(item, ignore_red)
    else:
        try:
            x = 1 + struct
            out.append(struct)
        except:
            pass

# Pass True in to this method for Part 1, and False for part 2
navigate(doc, True)
print(sum(out))

