 #!/bin/sh
# ref https://qiita.com/b4b4r07/items/dcd6be0bb9c9185475bb

PROGNAME=$(basename $0)

usage() {
echo "Usage: $PROGNAME [OPTIONS] FILE"
echo
echo "Options:"
echo "  -h, --help"
echo "      --data      : choose from {lattice, matern, circle, torus}"
echo "      --path      : path where you want to save data"
echo "      --num_pd    : number of persistence diagrams"
echo "      --dim_pcd   : dimension of point cloud data"
echo "      --side      : number of side of lattice"
echo "      --intensity : for Poisson point process"
echo "      --radius    : for Matern point process"
echo "      --sample    : sampling number from torus"
echo "      --dim_pd    : dimension of persistence diagrams"
echo "      --num_plot  : number of png for persistence diagrams"
echo
exit 1
}

name_sh=`pwd`
name_dir="$HOME/Desktop/data_tda"
name_data="torus"
dim_pcd=2
num_side=20
num_intensity=200
val_radius=0.03
num_sample=500
dim_pd=1
num_plot=10

for OPT in "$@"
    do
    case "$OPT" in
        '-h'|'--help' )
        usage
        exit 1
        ;;
        '--data' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
            echo "$PROGNAME: option requires a name of data $1" 1>&2
            exit 1
        else
            name_data="$2"
        fi

        if [ ${name_data} = "circle" ]; then
            num_pd=200
            dim_pcd=3
        elif [ ${name_data} = "torus" ]; then
            num_pd=40
            dim_pcd=3
            num_plot=40
        else
            num_pd=100
        fi

        shift 2
        ;;
        '--path' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
            echo "$PROGNAME: option requires an argument -- $1" 1>&2
            exit 1
        else
            name_dir="$2"
        fi
        shift 2
        ;;
        '--num_pd' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
        echo "$PROGNAME: option requires an argument -- $1" 1>&2
        exit 1
        else
        num_pd="$2"
        fi
        shift 2
        ;;
        '--dim_pcd' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
            echo "$PROGNAME: option requires an argument -- $1" 1>&2
            exit 1
        else
            dim_pcd="$2"
        fi
        shift 2
        ;;
        '--side' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
            echo "$PROGNAME: option requires an argument -- $1" 1>&2
            exit 1
        else
            num_side="$2"
        fi
        shift 2
        ;;
        '--intensity' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
            echo "$PROGNAME: option requires an argument -- $1" 1>&2
            exit 1
        else
            num_intensity="$2"
        fi
        shift 2
        ;;
        '--radius' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
            echo "$PROGNAME: option requires an argument -- $1" 1>&2
            exit 1
        else
            val_radius="$2"
        fi
        shift 2
        ;;
        '--sample' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
            echo "$PROGNAME: option requires an argument -- $1" 1>&2
            exit 1
        else
            num_sample="$2"
        fi
        shift 2
        ;;
        '--dim_pd' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
        echo "$PROGNAME: option requires an argument -- $1" 1>&2
        exit 1
        else
        dim_pd="$2"
        fi
        shift 2
        ;;
        '--num_plot' )
        if [[ -z "$2" ]] || [[ "$2" =~ ^-+ ]]; then
        echo "$PROGNAME: option requires an argument -- $1" 1>&2
        exit 1
        else
        num_plot="$2"
        fi
        shift 2
        ;;
        '--'|'-' )
        shift 1
        param+=( "$@" )
        break
        ;;
        -*)
        echo "$PROGNAME: illegal option -- '$(echo $1 | sed 's/^-*//')'" 1>&2
        exit 1
        ;;
        *)

        if [[ ! -z "$1" ]] && [[ ! "$1" =~ ^-+ ]]; then
            #param=( ${param[@]} "$1" )
            param+=( "$1" )
            shift 1
        fi
        ;;
    esac
    done

temp_pcd=`expr $dim_pcd - 1`
temp_pd=`expr $num_pd - 1`

echo "data     : ${name_data}"
echo "creating point cloud data"
python3 make_pcd.py --path ${name_dir} --data ${name_data} --num_pd ${num_pd} --dim_pcd ${dim_pcd} --side ${num_side} --intensity ${num_intensity} --radius ${val_radius} --sample ${num_sample}

if [ $name_data = "lattice" ]; then
    list_measure=("square" "square" "square" "gauss")
    list_radius=("014" "017" "020" "010")
    for j in `seq 0 3`
        do
        temp_measure=${list_measure[$j\]}
        temp_radius=${list_radius[$j\]}
        date
        echo "computing ${num_pd} persistence diagrams of ${temp_measure}_${temp_radius}"
        cd ${name_dir}/${name_data}/pcd${dim_pcd}_side${num_side}_${temp_measure}${temp_radius}_num${num_pd}/pcd_pd
        for i in `seq 0 $temp_pd`
            do
            if [ $(($i % 10)) == 0 ]; then
                echo "pd_$i"
            fi
            python3 -m homcloud.pc2diphacomplex -I -D -d ${dim_pcd} pcd_$i\.txt pd_$i\.idiagram
            for d in `seq 0 $temp_pcd`
                do
                python3 -m homcloud.diagram_to_text -d $d pd_$i\.idiagram -o dim$d\_$i\.txt
                done
            done
        done

elif [ $name_data = "matern" ]; then
    for k in `seq 0 2`
        do
        date
        echo "computing ${num_pd} persistence diagrams of type_$k"
        cd ${name_dir}/${name_data}/pcd${dim_pcd}_intensity${num_intensity}_radius${val_radius/./}_num${num_pd}/type$k\/pcd_pd
        for i in `seq 0 $temp_pd`
            do
            if [ $(($i % 10)) == 0 ]; then
                echo "pd_$i"
            fi
            python3 -m homcloud.pc2diphacomplex -I -D -d ${dim_pcd} pcd_$i\.txt pd_$i\.idiagram
            for d in `seq 0 $temp_pcd`
                do
                python3 -m homcloud.diagram_to_text -d $d pd_$i\.idiagram -o dim$d\_$i\.txt
                done
            done
        done

elif [ $name_data = "circle" ]; then
    date
    echo "computing ${num_pd} persistence diagrams of circle_svm"
    cd ${name_dir}/${name_data}/pcd${dim_pcd}_num${num_pd}/pcd_pd
    for i in `seq 0 $temp_pd`
        do
        if [ $(($i % 10)) == 0 ]; then
            echo "pd_$i"
        fi
        python3 -m homcloud.pc2diphacomplex -I -D -d ${dim_pcd} pcd_$i\.txt pd_$i\.idiagram
        for d in `seq 0 $temp_pcd`
            do
            python3 -m homcloud.diagram_to_text -d $d pd_$i\.idiagram -o dim$d\_$i\.txt
            done
        done

elif [ $name_data = "torus" ]; then
    date
    echo "computing ${num_pd} persistence diagrams of torus"
    cd ${name_dir}/${name_data}/pcd${dim_pcd}_sample${num_sample}_num${num_pd}/pcd_pd
    for i in `seq 0 $temp_pd`
        do
        if [ $(($i % 10)) == 0 ]; then
            echo "pd_$i"
        fi
        python3 -m homcloud.pc2diphacomplex -I -D -d ${dim_pcd} pcd_$i\.txt pd_$i\.idiagram
        for d in `seq 0 $temp_pcd`
            do
            python3 -m homcloud.diagram_to_text -d $d pd_$i\.idiagram -o dim$d\_$i\.txt
            done
        done

else
    echo "error massage: data must be selected from {lattice, matern, circle_svm, torus}"
    exit 1
fi

cd ${name_sh}
python3 visualize_pd.py --path ${name_dir} --data ${name_data} --num_pd ${num_pd} --dim_pcd ${dim_pcd} --side ${num_side} --intensity ${num_intensity} --radius ${val_radius} --sample ${num_sample} --dim_pd ${dim_pd} --num_plot ${num_plot}
