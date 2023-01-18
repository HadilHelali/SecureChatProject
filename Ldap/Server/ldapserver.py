import hashlib
import ldap
import sys
import cons

### user : username (pseudo/login) , firstname , lastname, pwd , num_carte

def login(pseudo,pwd):
    msg = ""
    l = ldap.initialize(cons.LDAP_HOST)
    # search for specific user
    search_filter = "cn=" + pseudo
    user_dn="cn="+pseudo+","+cons.USERS_DN
    print(user_dn)

    # hashing the password
    #password = pwd.encode()
    hash_object = hashlib.sha256()
    hash_object.update(pwd.encode("UTF-8"))
    hashed_password = hash_object.hexdigest().encode("UTF-8")
    print(hashed_password)

    try:
        l.bind_s(user_dn,hashed_password)
        result = l.search_s(user_dn,ldap.SCOPE_SUBTREE,search_filter)
        print(result)
        msg = "Authentification succeeded"
    except (ldap.INVALID_CREDENTIALS):
        msg = "Authentification failed : username or password invalid"

    l.unbind_s()
    return msg

def getallUsers():
    # connect to host with admin
    l = ldap.initialize(cons.LDAP_HOST)
    l.simple_bind_s(cons.ADMIN_DN, cons.ADMIN_PWD)
    # Search for all users
    result = l.search_s(cons.USERS_DN, ldap.SCOPE_SUBTREE, "(objectClass=person)")
    logins=[]
    # Print the results
    for dn, entry in result:
        logins.append(entry['cn'][0].decode("UTF-8"))

    return logins


def register(user):
    dn="cn="+user['username']+','+cons.USERS_DN

    hash_object = hashlib.sha256()
    hash_object.update(user['password'].encode("UTF-8"))
    hashed_password = hash_object.hexdigest()

    entry=[]
    entry.extend([
        ('objectClass', [b"top", b"person", b"organizationalPerson", b"inetOrgPerson"]),
        ('givenname', user['firstname'].encode("UTF-8")),
        ('sn', user['lastname'].encode("UTF-8")),
        ('uid', user['numCarte'].encode("UTF-8")),
        ('userPassword', hashed_password.encode("UTF-8") ) ])

    # connect to host with admin
    l = ldap.initialize(cons.LDAP_HOST)
    l.simple_bind_s(cons.ADMIN_DN, cons.ADMIN_PWD)

    try:
        # add entry in the directory
        l.add_s(dn, entry)
        print("success")
        return None
    except Exception:
        return sys.exc_info()[0]
    finally:
        # disconnect and free memory
        l.unbind_s()

user_obj = {
    'username': 'guest1',
    'password': '0010',
    'numCarte': '1601222',  # student card
    'firstname':'Foulen',
    'lastname':'Fouleni'
}

#register(user_obj)
#msg = login(user_obj['username'],'0000')
#print(msg)
#getallUsers()