from cefpython3 import cefpython as cef
import sys


def main():
    sys.excepthook = cef.ExceptHook
    _script, port, endpoint = sys.argv
    cef.Initialize()
    browser = cef.CreateBrowserSync(settings=dict(universal_access_from_file_urls_allowed=True,
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


if __name__ == '__main__':
    main()