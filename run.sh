DEVICE=$1
DATASET=$2

#tringVal="train valid test"
for split in "train valid test"; do
  for strategy in "lru belady"; do
    echo "${split}"
    echo "${strategy}"
    CUDA_VISIBLE_DEVICES=${DEVICE} python3 -m cache_replacement.policy_learning.cache.main \
      --experiment_base_dir=./tb \
      --experiment_name="eval_${DATASET}_${strategy}_${split}" \
      --cache_configs=cache_replacement/policy_learning/cache/configs/default.json \
      --cache_configs="cache_replacement/policy_learning/cache/configs/eviction_policy/${strategy}.json" \
      --config_bindings="capacity=2097152" \
      --memtrace_file="cache_replacement/policy_learning/cache/traces/${DATASET}_${split}.csv"
  done
done