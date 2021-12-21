"""
Backs up and restores a settings file to Dropbox.
This is an example app for API v2.
"""
import os
import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

# Add OAuth2 access token here.
# You can generate one for yourself in the App Console.
# See <https://blogs.dropbox.com/developers/2014/05/generate-an-access-token-for-your-own-account/>
from tqdm import tqdm

# TOKEN = 'liifgMMYRkUAAAAAAAAAAQnhEnwjFsWmp_ZiAOgXp4cxA6fpYN5nkP8vHK-Fvuhp'
TOKEN = 'OAt0iYRp0hQAAAAAAAAAAfR5rHKLsR19bnKgMVObsbn32tOb6AjewDZXYuXenedA'

LOCALFILE = '07-10-2021.sql'
# BACKUPPATH = 'User/junaidtariq/PycharmProjects/Tesseract/my-file-backup.txt'


def upload(chunk_size=4 * 1024 * 1024,):
    dbx = dropbox.Dropbox(TOKEN, timeout=10000)
    with open(LOCALFILE, "rb") as f:
        file_size = os.path.getsize(LOCALFILE)
        chunk_size = 4 * 1024 * 1024
        if file_size <= chunk_size:
            print(dbx.files_upload(f.read(), '/'+LOCALFILE))
        else:
            with tqdm(total=file_size, desc="Uploaded") as pbar:
                upload_session_start_result = dbx.files_upload_session_start(
                    f.read(chunk_size)
                )
                pbar.update(chunk_size)
                cursor = dropbox.files.UploadSessionCursor(
                    session_id=upload_session_start_result.session_id,
                    offset=f.tell(),
                )
                commit = dropbox.files.CommitInfo(path='/'+LOCALFILE)
                while f.tell() < file_size:
                    if (file_size - f.tell()) <= chunk_size:
                        print(
                            dbx.files_upload_session_finish(
                                f.read(chunk_size), cursor, commit
                            )
                        )
                    else:
                        dbx.files_upload_session_append(
                            f.read(chunk_size),
                            cursor.session_id,
                            cursor.offset,
                        )
                        cursor.offset = f.tell()
                    pbar.update(chunk_size)


# Uploads contents of LOCALFILE to Dropbox
def backup():
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as 07-10-2021.sql ...")
        try:
            dbx.files_upload(f.read(), '/07-10-2021.sql', mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

# Change the text string in LOCALFILE to be new_content
# @param new_content is a string
def change_local_file(new_content):
    print("Changing contents of " + LOCALFILE + " on local machine...")
    with open(LOCALFILE, 'wb') as f:
        f.write(new_content)

# Restore the local and Dropbox files to a certain revision
def restore(rev=None):
    # Restore the file on Dropbox to a certain revision
    print("Restoring my-file-backup.txt to revision " + rev + " on Dropbox...")
    dbx.files_restore('/my-file-backup.txt', rev)

    # Download the specific revision of the file at BACKUPPATH to LOCALFILE
    print("Downloading current " + 'my-file-backup.txt' + " from Dropbox, overwriting " + LOCALFILE + "...")
    dbx.files_download_to_file(LOCALFILE, '/my-file-backup.txt', rev)

# Look at all of the available revisions on Dropbox, and return the oldest one
def select_revision():
    # Get the revisions for a file (and sort by the datetime object, "server_modified")
    print("Finding available revisions on Dropbox...")
    entries = dbx.files_list_revisions('/my-file-backup.txt', limit=30).entries
    revisions = sorted(entries, key=lambda entry: entry.server_modified)

    for revision in revisions:
        print(revision.rev, revision.server_modified)

    # Return the oldest revision (first entry, because revisions was sorted oldest:newest)
    return revisions[0].rev

if __name__ == '__main__':
    # Check for an access token
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. "
            "Open up backup-and-restore-example.py in a text editor and "
            "paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    with dropbox.Dropbox(TOKEN, timeout=900) as dbx:

        # Check that the access token is valid
        try:
            dbx.users_get_current_account()
        except AuthError:
            sys.exit("ERROR: Invalid access token; try re-generating an "
                "access token from the app console on the web.")

        # Create a backup of the current settings file
        # backup()
        upload()

        # Change the user's file, create another backup
        # change_local_file(b"updated")
        # backup()

        # Restore the local and Dropbox files to a certain revision
        # to_rev = select_revision()
        # restore(to_rev)

        print("Done!")