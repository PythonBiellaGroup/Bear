#!/bin/bash

projects=(
    "base"
    "package"
)

for project in ${projects[@]}; do
    out_dir="tests/example_output/$project"
    echo "creating ${out_dir}"
    rm -rf ${out_dir}/*
    config_file="tests/config_files/${project}.yml"
    if [[ -f $config_file ]]; then
        # run with config file
        cookiecutter . \
            --config-file $config_file \
            --directory="{{cookiecutter.project_type}}/__cc_${project}" \
            -f \
            -o ${out_dir} \
            --no-input
    else
        # run with default config
        cookiecutter . \
            --directory="{{cookiecutter.project_type}}/__cc_${project}" \
            -f \
            -o ${out_dir} \
            --no-input
    fi
done