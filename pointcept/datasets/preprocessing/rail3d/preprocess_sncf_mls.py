# ------------------------------------------------------------------------------
# SNCF MLS Dataset Preprocessing
#
# This script provides preprocessing utilities for the SNCF MLS dataset.
#
# Dataset License:
#   The SNCF MLS dataset is licensed under the Open Database License (ODbL).
#   You are free to use, share, and adapt the data as long as you:
#     - Attribute the source (SNCF, via the official open data platform),
#     - Share any public modifications to the database under ODbL,
#     - Keep the data open if redistributed.
#
# IMPORTANT:
#   - The dataset itself is NOT included in this repository.
#   - To access the dataset:
#       • Raw point cloud data:
#         https://ressources.data.sncf.com/explore/dataset/nuage-points-3d
#       • Annotated point cloud data (via data request form):
#         https://github.com/akharroubi/Rail3D
#
# By using this script, you agree to comply with the ODbL terms when accessing
# and using the SNCF MLS dataset.
# ------------------------------------------------------------------------------

import os
import argparse
from pathlib import Path
from tqdm import tqdm
from pointcept.datasets.preprocessing.rail3d.utils import save_tiles_and_infos

# Dataset split
SPLITS = {
    "train": [
        "sncf_01.ply", "sncf_02.ply", "sncf_03.ply", "sncf_05.ply",
        "sncf_06.ply", "sncf_10.ply", "sncf_12.ply", "sncf_14.ply",
        "sncf_15.ply", "sncf_16.ply",
    ],
    "val": ["sncf_09.ply", "sncf_11.ply", "sncf_13.ply"],
    "test": ["sncf_04.ply", "sncf_07.ply", "sncf_08.ply"],
}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset_root",
        required=True,
        help="Path to the SNCF MLS dataset containing scene folders.",
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
