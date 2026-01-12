import os
import requests
import zipfile
import subprocess
import json

def download_zenodo_files(record_id='11502840', save_dir='./root/data'):
    """
    Download all files from a Zenodo record into a specified directory and unzip if any zipped file is present.

    :param record_id: The Zenodo record ID to download files from.
    :param save_dir: The directory where files will be saved. Defaults to './root/data'.
    """
    # Construct the Zenodo API endpoint for the record
    url = f'https://zenodo.org/api/records/{record_id}'

    # Set headers
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }

    try:
        # Make a request to get the record data using curl (to avoid 403 error with requests)
        print(f"Fetching record information for {record_id}...")
        result = subprocess.run(
            ['curl', '-s', url],
            capture_output=True,
            text=True,
            check=True
        )

        # Parse the JSON response
        data = json.loads(result.stdout)

        # Ensure the save directory exists
        os.makedirs(save_dir, exist_ok=True)

        # Get files list from the record
        files_list = data.get('files', [])

        if not files_list:
            print(f"No files found in record {record_id}")
            return

        print(f"Found {len(files_list)} files to download")

        # Iterate through all files in the record
        for file in files_list:
            # Get file information from the new API structure
            file_name = file.get('key')
            file_url = file.get('links', {}).get('self')
            file_path = os.path.join(save_dir, file_name)

            # Check if the file already exists
            if os.path.exists(file_path):
                print(f'{file_name} already exists. Skipping download.')
                continue

            # Download each file using curl
            print(f'Downloading {file_name}...')

            # Use curl for downloading to avoid 403 errors
            download_result = subprocess.run(
                ['curl', '-L', '-o', file_path, '--progress-bar', file_url],
                check=True
            )

            print(f'Downloaded {file_name}')

            # Check if the file is a zip file and unzip it
            if zipfile.is_zipfile(file_path):
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(save_dir)
                # os.remove(file_path)  # Remove the zip file after extracting

        print('All files downloaded and unzipped successfully.')

    except subprocess.CalledProcessError as e:
        print(f"An error occurred with subprocess: {e}")
    except json.JSONDecodeError as e:
        print(f"An error occurred parsing JSON: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
download_zenodo_files()
