from gym_unity.envs import UnityEnv

env_name = "./env/SoccerTwos"
multi_env = UnityEnv(env_name, worker_id=1, 
                     use_visual=False, multiagent=True)