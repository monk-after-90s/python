def generator():
    n = 0
    while True:
        recv = yield n
        print(f'recv:{recv}')
        n += 1


gen = generator()
# gen.send(None)
