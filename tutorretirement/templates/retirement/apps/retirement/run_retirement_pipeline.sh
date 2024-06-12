cool_off_days=$1
python /openedx/edx-platform/scripts/user_retirement/get_learners_to_retire.py --config_file=./openedx/edx-platform/scripts/user_retirement/config.yml --output_dir=learners_to_retire --cool_off_days="$cool_off_days"
for filename in learners_to_retire/*;do
    if test ! -f "$filename";then
        echo "No users to retire"
        continue
    else
        IFS="=" read -r name username <"$filename"
        echo "Retiring $username"
        python /openedx/edx-platform/scripts/user_retirement/retire_one_learner.py --config_file=./openedx/edx-platform/scripts/user_retirement/config.yml --username="$username"
    fi
done
