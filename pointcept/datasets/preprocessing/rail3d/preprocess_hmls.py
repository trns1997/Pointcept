# ------------------------------------------------------------------------------
# Hungarian MLS Dataset Preprocessing
#
# This script provides preprocessing utilities for the Hungarian MLS dataset.
#
# Dataset License:
#   The Hungarian MLS dataset is licensed under the Creative Commons 
#   Attribution–NonCommercial 3.0 (CC BY-NC 3.0) License.
#   You are free to:
#     - Share: copy and redistribute the material in any medium or format,
#     - Adapt: remix, transform, and build upon the material,
#   Under the following terms:
#     - Attribution: You must give appropriate credit, provide a link to the
#       license, and indicate if changes were made.
#     - NonCommercial: You may not use the material for commercial purposes.
#
# IMPORTANT:
#   - The dataset itself is NOT included in this repository.
#   - To access the dataset:
#       • Official Mendeley Data page:
#         https://data.mendeley.com/datasets/ccxpzhx9dj/1
#       • Dataset reference (Hungarian MLS data, used in Rail3D framework)
#         via Mendeley Data.
#
# By using this script, you agree to comply with the CC BY-NC 3.0 license terms
# when accessing and using the Hungarian MLS dataset.
# ------------------------------------------------------------------------------

import os
import argparse
from pathlib import Path
from tqdm import tqdm
from pointcept.datasets.preprocessing.rail3d.utils import save_tiles_and_infos

# Dataset split
SPLITS = {
    "train": [
        "hmls_01.ply", "hmls_03.ply", "hmls_06.ply", "hmls_07.ply",
        "hmls_09.ply", "hmls_10.ply", "hmls_11.ply", "hmls_13.ply",
        "hmls_14.ply", "hmls_15.ply", "hmls_16.ply", "hmls_17.ply",
        "hmls_19.ply", "hmls_21.ply", "hmls_23.ply", "hmls_28.ply",
        "hmls_29.ply",
    ],
    "val": [
        "hmls_02.ply", "hmls_05.ply", "hmls_08.ply", "hmls_18.ply",
        "hmls_26.ply", "hmls_27.ply",
    ],
    "test": [
        "hmls_04.ply", "hmls_12.ply", "hmls_20.ply", "hmls_22.ply",
        "hmls_24.ply", "hmls_25.ply",
    ],
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset_root",
        required=True,
        help="Path to the Hungarian MLS dataset containing scene folders.",
    )
    parser.add_argument(
        "--output_root",
        required=True,
        help="Output path where train/val folders will be located.",
    )
    parser.add_argument(
        "--tile_size",
        type=float,
        default=30.0,
        help="Size of each tile (in meters). Default: 30.0",
    )
    parser.add_argument(
        "--overlap",
        type=float,
        default=5.0,
        help="Overlap between tiles (in meters). Default: 5.0",
    )

    config = parser.parse_args()

    # Create output directories and process each split
    for split, files in SPLITS.items():
        print(f"Processing {split} set with {len(files)} files...")
        os.makedirs(os.path.join(config.output_root, split), exist_ok=True)
        for ply_name in tqdm(files):
            ply_path = Path(config.dataset_root) / ply_name
            save_tiles_and_infos(
                ply_file=ply_path,
                split=split,
                output_root=config.output_root,
                tile_size=config.tile_size,
                overlap=config.overlap
            )
