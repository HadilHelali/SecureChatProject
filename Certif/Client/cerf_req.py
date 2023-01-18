from cryptography import x509
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives.serialization import (Encoding,PrivateFormat,NoEncryption)
import cons

def gen_cert_req(login,firstname):

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    builder = x509.CertificateSigningRequestBuilder()
    builder = builder.subject_name(
        x509.Name([
            x509.NameAttribute(NameOID.SURNAME, u'LOGIN:'+login),
            x509.NameAttribute(NameOID.GIVEN_NAME,u''+firstname)
        ])
    )
    builder = builder.add_extension(
        x509.BasicConstraints(ca=False,path_length=None),critical=True,
    )

    request = builder.sign(
        private_key, hashes.SHA256(), default_backend()
    )

    with open(cons.dest_req+'/'+login+'_req.csr','wb') as f:
        f.write(request.public_bytes(Encoding.PEM))

    with open(cons.dest_key_cert+'/'+login+'.key','wb') as f:
        f.write(private_key.private_bytes(Encoding.PEM,PrivateFormat.TraditionalOpenSSL,NoEncryption()))

# test :
#gen_cert_req("guest1","Foulen")