from cefpython3 import cefpython as cef
import platform
import sys


def main():
    # check_versions()
    sys.excepthook = cef.ExceptHook  # To shutdown all CEF processes on error
    _script, port, endpoint = sys.argv
    cef.Initialize()
    cef.CreateBrowserSync(settings=dict(universal_access_from_file_urls_allowed=True,
                                        javascript_disabled=False,
                                        javascript_close_windows_disallowed=False,
                                        webgl_disabled=False,
                                        plugins_disabled=False,
                                        local_storage_disabled=False,
                                        web_security_disabled=True),
                        url="http://localhost:{PORT}/#/{ENDPOINT}".format(PORT=port, ENDPOINT=endpoint),
                        window_title="Warehouse")
    cef.MessageLoop()
    cef.Shutdown()
    

def check_versions():
    ver = cef.GetVersion()
    print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
    print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
    print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
    print("[hello_world.py] Python {ver} {arch}".format(
           ver=platform.python_version(),
           arch=platform.architecture()[0]))
    assert cef.__version__ >= "57.0", "CEF Python v57.0+ required to run this"

if __name__ == '__main__':
    main()