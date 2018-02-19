import asyncio

g_storage = dict()

class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        self.transport.write(self._process(data.decode('utf-8').strip('\r\n')).encode('utf-8'))
        chunks = data.decode('utf-8').strip('\r\n').split(' ')
        cmd = chunks[0]

    def _process(self, command):
        chunks = command.split(' ')
        if chunks[0] == 'get':
            return self._process_get(chunks[1])
        elif chunks[0] == 'put':
            return self._process_put(chunks[1], chunks[2], chunks[3])
        else:
            return 'error\nwrong command\n\n'

    def _process_get(self, key):
        res = 'ok\n'
        if key == '*':
            for key, values in g_storage.items():
                for value in values:
                    res = res + key + ' ' + value[1] + ' ' + value[0] + '\n'
        else:
            if key in g_storage:
                for value in g_storage[key]:
                    res = res + key + ' ' + value[1] + ' ' + value[0] + '\n'

        return res + '\n'

    def _process_put(self, key, value, timestamp):
        if key == '*':
            return 'error\nkey cannot contain *\n\n'
        if not key in g_storage:
            g_storage[key] = list()
        if not (timestamp, value) in g_storage[key]:
            g_storage[key].append((timestamp, value))
            g_storage[key].sort(key=lambda tup: tup[0])
        return 'ok\n\n'

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

#run_server('127.0.0.1', 8181)

