def dbg_breakpoint():
    while True:
        cmd = input('(debug)> ')
        if cmd == 'dbg_exit':
            break
        exec(cmd)


def dbg_watch():
    pass
