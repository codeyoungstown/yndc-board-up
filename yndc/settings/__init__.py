import os

from default import *


try:
    from local import *
except ImportError:
    pass

# There's probably a much better way to do this.
# FIXME nicholasserra
if os.environ.get('ENVIRONMENT') == 'production':
    try:
        from production import *
    except ImportError:
        pass

