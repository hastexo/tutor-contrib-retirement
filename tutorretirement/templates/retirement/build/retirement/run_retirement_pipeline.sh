cool_off_days=$1
python scripts/get_learners_to_retire.py --config_file=./pipeline_config/config.yml --output_dir=learners_to_retire --cool_off_days="$cool_off_days"
for filename in learners_to_retire/*;do
    if test ! -f "$filename";then
        echo "No users to retire"
        continue
    else
        IFS="=" read -r name username <"$filename"
        echo "Retiring $username"
        python scripts/retire_one_learner.py --config_file=./pipeline_config/config.yml --username="$username"
    fi
done
