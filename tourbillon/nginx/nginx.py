import aiohttp
import asyncio
import logging
import re
import time

logger = logging.getLogger(__name__)


@asyncio.coroutine
def get_nginx_status(agent):
    yield from agent.run_event.wait()
    config = agent.pluginconfig['nginx']
    db_config = config['database']
    try:
        logger.debug('try to create the database...')
        agent.create_database(db_config['name'])
        agent.create_retention_policy('{}_rp'.format(db_config['name']),
                                      db_config['duration'],
                                      db_config['replication'],
                                      db_config['name'])
        logger.info('database "%s" created successfully', 'nginx')
    except:
        pass

    while agent.run_event.is_set():
        yield from asyncio.sleep(config['frequency'])
        url = config['url']

        logger.debug('obtaining status from {}'.format(config['host']))

        res = yield from aiohttp.get(url)
        if res.status == 200:
            text = yield from res.text()

            logger.debug
            logger.debug(text)

            status = text.strip().split('\n')
            conn = status[0].strip().split(': ')[-1]
            # accepts, handled, num_req = status[2].strip().split(' ')
            reading, writing, waiting = re.split(r'[:\s]\s*',
                                                 status[-1].strip())[1::2]
            logger.debug(', '.join(conn + reading + writing + waiting))
            data = [{
                'measurement': 'status',
                'tags': {
                    'hostname': config['host']
                },
                'fields': {
                    'connections': int(conn),
                    'reading': int(reading),
                    'writing': int(writing),
                    'waiting': int(waiting)
                }
            }]
            yield from agent.async_push(data, db_config['name'])

    logger.info('get_nginx_status terminated')
