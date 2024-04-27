from microdot import Microdot


userver = Microdot()


@userver.route('/test')
async def test(_):
    return 'ZEOS_SERVER_ONLINE', 200, {'Content-Type': 'text/plain'}


if __name__ == '__main__':
    userver.run(debug=True)
