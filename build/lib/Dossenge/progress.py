def progress(start, end, timer, progresses):
    progresses += [''] * 2147483647 
    progresses = progresses[start:end+1]
    for i in range(start,end+1):
        exec(progresses)
        print('■' * i + ' ' * (end - i) + f'| {i} / {end}', end='\r')
        __import__('time').sleep(timer)
