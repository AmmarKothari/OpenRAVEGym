import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='OpenRAVE-v0',
    entry_point='gym_OpenRAVE.envs:OpenRAVE_Env',
)