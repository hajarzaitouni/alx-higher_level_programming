#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    content = dir(hidden_4)
    for name in content:
        if name[:2] != "__":
            print(name)
