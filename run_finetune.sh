#!/bin/bash
#SBATCH --job-name=gv-rep-finetune
#SBATCH --account=def-mahadeva
#SBATCH --time=12:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gpus-per-node=h100:1
#SBATCH --chdir=/scratch/ranaab
#SBATCH --output=%x-%j.out
#SBATCH --error=%x-%j.err
#SBATCH --mail-type=BEGIN,END,FAIL
#SBATCH --mail-user=ranamoneim@gmail.com

# Print job information
echo "Job started at: $(date)"
echo "Running on node: $(hostname)"
echo "Job ID: $SLURM_JOB_ID"
echo "Working directory: $(pwd)"

# Create a working directory in SCRATCH for this job
WORK_DIR=/scratch/ranaab/job_${SLURM_JOB_ID}
mkdir -p ${WORK_DIR}
cd ${WORK_DIR}

# Copy necessary files to scratch (optional, for speed)
# We'll run from project but save outputs to scratch

# Load required modules (must be loaded BEFORE activating venv)
module load StdEnv/2023
module load gcc/12.3
module load cuda/12.6
module load arrow/21.0.0
module load faiss

# Activate virtual environment
source /project/def-mahadeva/ranaab/genomic-FM/venv/bin/activate

# Verify GPU is available
nvidia-smi

# Set environment variables
export CUDA_VISIBLE_DEVICES=0
export WANDB_MODE=offline
export WANDB_DIR=${WORK_DIR}
export WANDB_CACHE_DIR=${WORK_DIR}/wandb_cache
export WANDB_DATA_DIR=${WORK_DIR}/wandb_data
export WANDB_CONFIG_DIR=${WORK_DIR}/wandb_config
mkdir -p ${WANDB_DIR} ${WANDB_CACHE_DIR} ${WANDB_DATA_DIR} ${WANDB_CONFIG_DIR}

# Symlink data directory to scratch to avoid read-only issues
cd ${WORK_DIR}
ln -s /project/def-mahadeva/ranaab/genomic-FM/root ./root
ln -s /project/def-mahadeva/ranaab/genomic-FM/src ./src
ln -s /project/def-mahadeva/ranaab/genomic-FM/configs ./configs
ln -s /project/def-mahadeva/ranaab/genomic-FM/finetune.py ./finetune.py

# Run the training from the work directory
python finetune.py \
    --dataset='sqtl_pval_dnabert2' \
    --epochs=100 \
    --gpus=1 \
    --num_workers=8 \
    --config=configs/finetune_dnabert2.yaml \
    --seed=0 \
    --project='GV-Rep'

# Print completion time
echo "Job finished at: $(date)"
echo "Results saved in: ${WORK_DIR}"
echo "Job finished at: $(date)"
