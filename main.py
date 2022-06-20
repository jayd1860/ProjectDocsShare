import sys
import dropbox
from dropbox import DropboxOAuth2FlowNoRedirect

if __name__ == '__main__':
    APP_KEY = "3h3ft83fmamys5f"

    auth_flow = DropboxOAuth2FlowNoRedirect(APP_KEY, use_pkce=True, token_access_type='offline')
    authorize_url = auth_flow.start()
    print("1. Go to: " + authorize_url)
    print("2. Click \"Allow\" (you might have to log in first).")
    print("3. Copy the authorization code.")
    auth_code = input("Enter the authorization code here: ").strip()

    try:
        oauth_result = auth_flow.finish(auth_code)
    except Exception as e:
        print('Error: %s' % (e,))
        exit(1)

    dbx = dropbox.Dropbox(oauth2_refresh_token=oauth_result.refresh_token, app_key=APP_KEY)
    sys.stdout.write('\n\n')
    response = dbx.files_list_folder("/Customers", recursive=True)
    for entry in response.entries:
         print(entry.name)

