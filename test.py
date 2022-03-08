import flake8
import autopep8
from logging import getLogger, StreamHandler, INFO, Formatter

logger = getLogger(__name__)

handler = StreamHandler()
handler.setLevel(INFO)
handler.setFormatter(Formatter('[%(levelname)s][%(name)s]: %(message)s'))

logger.setLevel(INFO)
logger.addHandler(handler)

logger.info(f'flake8 {flake8.__version__}')
logger.info(f'autopep8 {autopep8.__version__}')
