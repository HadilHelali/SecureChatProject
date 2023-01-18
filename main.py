# This is a sample Python script.
import multiprocessing

from Certif.CA.Cert import gen_ca_cert_key
from interface.Pages.App import App

def run_script():
    gen_ca_cert_key()
    app = App()
    app.mainloop()

if __name__ == '__main__':
    ## TODO : remove #
    #gen_ca_cert_key()
    app = App()
    app.mainloop()
    #p1 = multiprocessing.Process(target=run_script)
    #p2 = multiprocessing.Process(target=run_script)
    #p1.start()
    #p2.start()
    #p1.join()
    #p2.join()



