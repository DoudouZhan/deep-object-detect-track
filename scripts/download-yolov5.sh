if [ ! -f "scripts/base.sh" ]; then
    echo "scripts/base.sh not found"
    exit 1
fi
source scripts/base.sh

tag_name=v7.0
all_model_list=(
    yolov5n
    yolov5s
    yolov5m
    yolov5l
    yolov5x
    yolov5n
)

weights_dir=$CACHE_DIR/yolov5
mkdir -p ${weights_dir}

model_list=($1)

if [ ${#model_list[@]} -eq 0 ]; then
    model_list=(${all_model_list[@]})
fi

print_info "Downloading YOLOv5 (${model_list}) weights..."
echo ""

for model_name in ${model_list[@]}; do
    url=https://github.com/ultralytics/yolov5/releases/download/${tag_name}/${model_name}.pt
    print_info "Downloading ${url} ..."
    wget -c ${url} -P ${weights_dir} #--no-verbose
    print_success "Downloaded successfully: ${weights_dir}/${model_name}.pt"
    echo
done
