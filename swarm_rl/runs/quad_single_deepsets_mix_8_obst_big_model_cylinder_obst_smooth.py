from sample_factory.runner.run_description import RunDescription, Experiment, ParamGrid

from swarm_rl.runs.quad_multi_deepsets_obstacle_baseline import QUAD_8_OBSTACLES_PARAMETERZE_CLI, seeds

_params = ParamGrid([
    ('seed', seeds(2)),
    ('quads_obst_proximity_mode', [1]),
    ('quads_obst_penalty_fall_off', [3.0, 5.0]),
    ('quads_collision_obst_smooth_max_penalty', [10.0]),

])

SMALL_MODEL_CLI = QUAD_8_OBSTACLES_PARAMETERZE_CLI + (
    ' --hidden_size=256 --quads_neighbor_hidden_size=128 --quads_obstacle_hidden_size=128 --quads_obstacle_type=cylinder '
    '--neighbor_obs_type=none --quads_num_agents=1 --quads_local_obs=-1 --with_wandb=False '
    '--quads_neighbor_encoder_type=no_encoder --quads_collision_smooth_max_penalty=0.0 --quads_local_obst_obs=2'
)

_experiment = Experiment(
    'cylinder-small_model',
    SMALL_MODEL_CLI,
    _params.generate_params(randomize=False),
)

RUN_DESCRIPTION = RunDescription('8_obst_2_local_quads_multi_obst_mix_8a_v116', experiments=[_experiment])

# On Brain server, when you use num_workers = 72, if the system reports: Resource temporarily unavailable,
# then, try to use two commands below
# export OMP_NUM_THREADS=1
# export USE_SIMPLE_THREADED_LEVEL3=1

# Command to use this script on server:
# xvfb-run python -m runner.run --run=quad_multi_through_hole_obstacle --runner=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4
# Command to use this script on local machine:
# Please change num_workers to the physical cores of your local machine
# python -m runner.run --run=quad_multi_through_hole_obstacle --runner=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4

# Slurm
# srun --exclusive -c72 -N1 --gres=gpu:4 python -m sample_factory.runner.run --run=swarm_rl.runs.quad_multi_deepsets_through_random_obstacles --runner=processes --max_parallel=4 --pause_between=1 --experiments_per_gpu=1 --num_gpus=4