cool_off_days=$1
python scripts/user_retirement/get_learners_to_retire.py --config_file=scripts/user_retirement/pipeline_config/config.yml --output_dir=scripts/user_retirement/learners_to_retire --cool_off_days="$cool_off_days"
for filename in scripts/user_retirement/learners_to_retire/*;do
    if test ! -f "$filename";then
        echo "No users to retire"
        continue
    else
        IFS="=" read -r name username <"$filename"
        echo "Retiring $username"
        python scripts/user_retirement/retire_one_learner.py --config_file=scripts/user_retirement/pipeline_config/config.yml --username="$username"
    fi
done
