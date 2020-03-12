import os
import platform

def create_home_dir():
    """Create the home directory for this repo"""

    current_platform = platform.system().lower()
    if current_platform != 'windows':
        import pwd  # pylint: disable=E0401

    # create the necessary directory structure for storing scripts/raw_data
    # in the ~/.REPONAME directory
    required_dirs = [os.path.join(HOME_DIR, dirs) for dirs in ['', 'models', 'raw_data']]
    for dir in required_dirs:
        if not os.path.exists(dir):
            try:
                os.makedirs(dir)
                if (current_platform != 'windows') and os.getenv("SUDO_USER"):
                    # owner of .REPONAME should be user even when installing
                    # w/sudo
                    pw = pwd.getpwnam(os.getenv("SUDO_USER"))
                    os.chown(dir, pw.pw_uid, pw.pw_gid)
            except OSError:
                print("The REPONAME lacks permission to "
                      "access the ~/.REPONAME/ directory.")
                raise