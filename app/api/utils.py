import logging
import logging.handlers
from logstash_formatter import LogstashFormatterV1

from config import LOGSTASH_HOST, LOGSTASH_PORT 

logstash_handler = logging.handlers.SocketHandler(LOGSTASH_HOST, LOGSTASH_PORT)
logstash_handler.setFormatter(LogstashFormatterV1())
logger = logging.getLogger()
logger.addHandler(logstash_handler)
logger.setLevel(logging.DEBUG)